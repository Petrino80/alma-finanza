/**
 * Alma Finanza - Quote Page Real-Time Data
 * Visualizza dati real-time con grafici interattivi
 */

const ALPHA_VANTAGE_API_KEY = '6WCELVI7XTDMD2E5';
const REFRESH_INTERVAL = 60000; // 60 secondi
let priceChart = null;
let currentSymbol = null;

/**
 * Get symbol from URL parameter
 */
function getSymbolFromURL() {
    const params = new URLSearchParams(window.location.search);
    return params.get('symbol') || params.get('s') || 'NVDA'; // Default: Nvidia
}

/**
 * Format number with thousand separators
 */
function formatNumber(num) {
    return new Intl.NumberFormat('it-IT').format(num);
}

/**
 * Format currency
 */
function formatCurrency(num, decimals = 2) {
    return '$' + num.toFixed(decimals);
}

/**
 * Fetch quote data from Alpha Vantage
 */
async function fetchQuoteData(symbol) {
    try {
        const url = `https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=${symbol}&apikey=${ALPHA_VANTAGE_API_KEY}`;
        const response = await fetch(url);
        const data = await response.json();

        if (data['Global Quote'] && Object.keys(data['Global Quote']).length > 0) {
            const quote = data['Global Quote'];
            return {
                symbol: quote['01. symbol'],
                price: parseFloat(quote['05. price']),
                open: parseFloat(quote['02. open']),
                high: parseFloat(quote['03. high']),
                low: parseFloat(quote['04. low']),
                volume: parseInt(quote['06. volume']),
                previousClose: parseFloat(quote['08. previous close']),
                change: parseFloat(quote['09. change']),
                changePercent: parseFloat(quote['10. change percent'].replace('%', ''))
            };
        } else if (data['Note']) {
            throw new Error('API limit raggiunto. Riprova tra qualche minuto.');
        } else {
            throw new Error('Simbolo non trovato o dati non disponibili');
        }
    } catch (error) {
        console.error('Error fetching quote:', error);
        throw error;
    }
}

/**
 * Fetch intraday data for chart
 */
async function fetchIntradayData(symbol) {
    try {
        const url = `https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=${symbol}&interval=5min&apikey=${ALPHA_VANTAGE_API_KEY}`;
        const response = await fetch(url);
        const data = await response.json();

        if (data['Time Series (5min)']) {
            const timeSeries = data['Time Series (5min)'];
            const labels = [];
            const prices = [];

            // Get last 50 data points (circa 4 ore di trading)
            Object.keys(timeSeries).slice(0, 50).reverse().forEach(timestamp => {
                const time = new Date(timestamp);
                labels.push(time.toLocaleTimeString('it-IT', { hour: '2-digit', minute: '2-digit' }));
                prices.push(parseFloat(timeSeries[timestamp]['4. close']));
            });

            return { labels, prices };
        } else {
            console.warn('Intraday data not available');
            return null;
        }
    } catch (error) {
        console.error('Error fetching intraday data:', error);
        return null;
    }
}

/**
 * Update page with quote data
 */
function updateQuotePage(quoteData) {
    // Update title
    document.getElementById('page-title').textContent = `${quoteData.symbol} - Alma Finanza`;
    document.getElementById('stock-name').textContent = quoteData.symbol;
    document.getElementById('stock-symbol').textContent = quoteData.symbol;

    // Update price
    document.getElementById('stock-price').textContent = formatCurrency(quoteData.price);

    // Update change
    const changeElement = document.getElementById('stock-change');
    const isPositive = quoteData.change >= 0;
    const sign = isPositive ? '+' : '';
    const changeClass = isPositive ? 'positive' : 'negative';
    changeElement.innerHTML = `<span class="${changeClass}">${sign}${formatCurrency(quoteData.change)} (${sign}${quoteData.changePercent.toFixed(2)}%)</span>`;

    // Update stats
    document.getElementById('stock-open').textContent = formatCurrency(quoteData.open);
    document.getElementById('stock-high').textContent = formatCurrency(quoteData.high);
    document.getElementById('stock-low').textContent = formatCurrency(quoteData.low);
    document.getElementById('stock-volume').textContent = formatNumber(quoteData.volume);

    // Update timestamp
    const now = new Date();
    document.getElementById('last-update').textContent = now.toLocaleTimeString('it-IT');

    // Show content
    document.getElementById('loading').classList.add('hidden');
    document.getElementById('quote-content').classList.remove('hidden');
}

/**
 * Create price chart
 */
function createPriceChart(chartData) {
    if (!chartData) return;

    const ctx = document.getElementById('price-chart').getContext('2d');

    // Destroy existing chart
    if (priceChart) {
        priceChart.destroy();
    }

    const gradient = ctx.createLinearGradient(0, 0, 0, 400);
    gradient.addColorStop(0, 'rgba(20, 184, 166, 0.3)');
    gradient.addColorStop(1, 'rgba(20, 184, 166, 0.0)');

    priceChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: chartData.labels,
            datasets: [{
                label: 'Prezzo ($)',
                data: chartData.prices,
                borderColor: '#14b8a6',
                backgroundColor: gradient,
                borderWidth: 3,
                fill: true,
                tension: 0.4,
                pointRadius: 0,
                pointHoverRadius: 6,
                pointHoverBackgroundColor: '#14b8a6'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            interaction: {
                intersect: false,
                mode: 'index'
            },
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    backgroundColor: 'rgba(0, 0, 0, 0.8)',
                    titleColor: '#fff',
                    bodyColor: '#fff',
                    borderColor: '#14b8a6',
                    borderWidth: 1,
                    padding: 12,
                    displayColors: false,
                    callbacks: {
                        label: function(context) {
                            return 'Prezzo: $' + context.parsed.y.toFixed(2);
                        }
                    }
                }
            },
            scales: {
                x: {
                    grid: {
                        display: false
                    },
                    ticks: {
                        maxTicksLimit: 10
                    }
                },
                y: {
                    grid: {
                        color: 'rgba(0, 0, 0, 0.05)'
                    },
                    ticks: {
                        callback: function(value) {
                            return '$' + value.toFixed(2);
                        }
                    }
                }
            }
        }
    });
}

/**
 * Load TradingView widget
 */
function loadTradingViewWidget(symbol) {
    const container = document.getElementById('tradingview-widget');
    container.innerHTML = `
        <iframe
            src="https://www.tradingview.com/widgetembed/?frameElementId=tradingview&symbol=${symbol}&interval=D&hidesidetoolbar=0&symboledit=1&saveimage=1&toolbarbg=f1f3f6&studies=[]&theme=light&style=1&timezone=Europe/Rome&withdateranges=1&showpopupbutton=1&studies_overrides={}&overrides={}&enabled_features=[]&disabled_features=[]&showpopupbutton=1&locale=it"
            style="width: 100%; height: 100%; border: none;">
        </iframe>
    `;
}

/**
 * Show error state
 */
function showError() {
    document.getElementById('loading').classList.add('hidden');
    document.getElementById('error-state').classList.remove('hidden');
}

/**
 * Initialize quote page
 */
async function initQuotePage() {
    currentSymbol = getSymbolFromURL();
    console.log('📊 Loading quote for:', currentSymbol);

    try {
        // Fetch quote data
        const quoteData = await fetchQuoteData(currentSymbol);
        updateQuotePage(quoteData);

        // Load TradingView widget
        loadTradingViewWidget(currentSymbol);

        // Fetch and display chart (con delay per non saturare API)
        setTimeout(async () => {
            const chartData = await fetchIntradayData(currentSymbol);
            if (chartData) {
                createPriceChart(chartData);
            }
        }, 2000);

        // Auto-refresh every 60 seconds
        setInterval(async () => {
            try {
                const updatedQuote = await fetchQuoteData(currentSymbol);
                updateQuotePage(updatedQuote);
                console.log('🔄 Quote refreshed');
            } catch (error) {
                console.error('Error refreshing quote:', error);
            }
        }, REFRESH_INTERVAL);

    } catch (error) {
        console.error('Error initializing quote page:', error);
        showError();
    }
}

// Start when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initQuotePage);
} else {
    initQuotePage();
}
