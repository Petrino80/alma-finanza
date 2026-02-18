/**
 * Alma Finanza - Quote Page Real-Time Data
 * Visualizza dati real-time con grafici interattivi
 * Usa Twelve Data API (demo key - gratuita, CORS abilitato)
 */

const TWELVEDATA_KEY = 'demo';
const REFRESH_INTERVAL = 60000; // 60 secondi
let priceChart = null;
let currentSymbol = null;

/**
 * Legge il simbolo dal parametro URL
 */
function getSymbolFromURL() {
    const params = new URLSearchParams(window.location.search);
    return params.get('symbol') || params.get('s') || 'NVDA';
}

/**
 * Formatta numero con separatori migliaia
 */
function formatNumber(num) {
    return new Intl.NumberFormat('it-IT').format(num);
}

/**
 * Formatta prezzo in dollari
 */
function formatCurrency(num, decimals = 2) {
    if (!num || isNaN(num)) return '$-';
    return '$' + parseFloat(num).toFixed(decimals);
}

/**
 * Fetch dati quote da Twelve Data
 * Campi restituiti: open, high, low, close, volume, previous_close, change, percent_change
 */
async function fetchQuoteData(symbol) {
    try {
        const url = `https://api.twelvedata.com/quote?symbol=${encodeURIComponent(symbol)}&apikey=${TWELVEDATA_KEY}`;
        const response = await fetch(url);

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        const data = await response.json();

        // Errore API
        if (data.code || data.status === 'error') {
            throw new Error(data.message || 'Simbolo non trovato');
        }

        if (data.close && parseFloat(data.close) > 0) {
            return {
                symbol: data.symbol || symbol,
                name: data.name || symbol,
                price: parseFloat(data.close),
                open: parseFloat(data.open) || 0,
                high: parseFloat(data.high) || 0,
                low: parseFloat(data.low) || 0,
                previousClose: parseFloat(data.previous_close) || 0,
                change: parseFloat(data.change) || 0,
                changePercent: parseFloat(data.percent_change) || 0,
                volume: parseInt(data.volume) || 0,
            };
        }

        throw new Error('Dati non disponibili per ' + symbol);
    } catch (error) {
        console.error('Error fetching quote:', error);
        throw error;
    }
}

/**
 * Fetch dati candela (ultimi 30 giorni, risoluzione giornaliera)
 * Twelve Data /time_series: restituisce OHLCV giornaliero
 */
async function fetchChartData(symbol) {
    try {
        const url = `https://api.twelvedata.com/time_series?symbol=${encodeURIComponent(symbol)}&interval=1day&outputsize=30&apikey=${TWELVEDATA_KEY}`;
        const response = await fetch(url);

        if (!response.ok) {
            console.warn('Chart data not available');
            return null;
        }

        const data = await response.json();

        if (data.code || data.status === 'error') {
            console.warn('Chart API error:', data.message);
            return null;
        }

        if (data.values && data.values.length > 0) {
            // I dati arrivano in ordine inverso (più recente prima)
            const reversed = [...data.values].reverse();

            const labels = reversed.map(item => {
                const d = new Date(item.datetime);
                return d.toLocaleDateString('it-IT', { day: '2-digit', month: '2-digit' });
            });

            const prices = reversed.map(item => parseFloat(item.close));

            return { labels, prices };
        }

        return null;
    } catch (error) {
        console.error('Error fetching chart data:', error);
        return null;
    }
}

/**
 * Aggiorna la pagina con i dati quote
 */
function updateQuotePage(quoteData) {
    const set = (id, val) => {
        const el = document.getElementById(id);
        if (el) el.textContent = val;
    };

    // Titolo pagina
    document.title = `${quoteData.symbol} - Alma Finanza`;
    set('page-title', `${quoteData.symbol} - Alma Finanza`);
    set('stock-name', quoteData.name || quoteData.symbol);
    set('stock-symbol', quoteData.symbol);

    // Prezzo corrente
    set('stock-price', formatCurrency(quoteData.price));

    // Variazione
    const changeEl = document.getElementById('stock-change');
    if (changeEl) {
        const isPositive = quoteData.change >= 0;
        const sign = isPositive ? '+' : '';
        const cls = isPositive ? 'positive' : 'negative';
        changeEl.innerHTML = `<span class="${cls}">${sign}${formatCurrency(quoteData.change)} (${sign}${quoteData.changePercent.toFixed(2)}%)</span>`;
    }

    // Stats
    set('stock-open', formatCurrency(quoteData.open));
    set('stock-high', formatCurrency(quoteData.high));
    set('stock-low', formatCurrency(quoteData.low));
    set('stock-prev-close', formatCurrency(quoteData.previousClose));
    set('stock-volume', quoteData.volume > 0 ? formatNumber(quoteData.volume) : '-');

    // Timestamp
    set('last-update', new Date().toLocaleTimeString('it-IT'));

    // Mostra contenuto, nascondi loading
    const loadingEl = document.getElementById('loading');
    if (loadingEl) loadingEl.classList.add('hidden');

    const contentEl = document.getElementById('quote-content');
    if (contentEl) contentEl.classList.remove('hidden');
}

/**
 * Crea grafico prezzi (ultimi 30 giorni)
 */
function createPriceChart(chartData) {
    if (!chartData || !chartData.prices.length) return;

    const chartEl = document.getElementById('price-chart');
    if (!chartEl) return;

    const ctx = chartEl.getContext('2d');

    if (priceChart) priceChart.destroy();

    const firstPrice = chartData.prices[0];
    const lastPrice = chartData.prices[chartData.prices.length - 1];
    const isUp = lastPrice >= firstPrice;
    const lineColor = isUp ? '#10b981' : '#ef4444';

    const gradient = ctx.createLinearGradient(0, 0, 0, 400);
    gradient.addColorStop(0, isUp ? 'rgba(16, 185, 129, 0.3)' : 'rgba(239, 68, 68, 0.3)');
    gradient.addColorStop(1, 'rgba(255,255,255,0)');

    priceChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: chartData.labels,
            datasets: [{
                label: 'Prezzo ($)',
                data: chartData.prices,
                borderColor: lineColor,
                backgroundColor: gradient,
                borderWidth: 2,
                fill: true,
                tension: 0.3,
                pointRadius: 0,
                pointHoverRadius: 5,
                pointHoverBackgroundColor: lineColor
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            interaction: { intersect: false, mode: 'index' },
            plugins: {
                legend: { display: false },
                tooltip: {
                    backgroundColor: 'rgba(0,0,0,0.85)',
                    titleColor: '#fff',
                    bodyColor: '#fff',
                    borderColor: lineColor,
                    borderWidth: 1,
                    padding: 12,
                    displayColors: false,
                    callbacks: {
                        label: ctx => 'Prezzo: $' + ctx.parsed.y.toFixed(2)
                    }
                }
            },
            scales: {
                x: {
                    grid: { display: false },
                    ticks: { maxTicksLimit: 8 }
                },
                y: {
                    grid: { color: 'rgba(0,0,0,0.05)' },
                    ticks: { callback: v => '$' + v.toFixed(2) }
                }
            }
        }
    });
}

/**
 * Carica widget TradingView
 */
function loadTradingViewWidget(symbol) {
    const container = document.getElementById('tradingview-widget');
    if (!container) return;

    container.innerHTML = `
        <iframe
            src="https://www.tradingview.com/widgetembed/?frameElementId=tradingview&symbol=${encodeURIComponent(symbol)}&interval=D&hidesidetoolbar=0&symboledit=1&saveimage=1&toolbarbg=f1f3f6&studies=[]&theme=light&style=1&timezone=Europe/Rome&withdateranges=1&showpopupbutton=1&locale=it"
            style="width: 100%; height: 100%; border: none;"
            allowtransparency="true"
            frameborder="0">
        </iframe>
    `;
}

/**
 * Mostra stato di errore
 */
function showError(message) {
    const loadingEl = document.getElementById('loading');
    if (loadingEl) loadingEl.classList.add('hidden');

    const errorEl = document.getElementById('error-state');
    if (errorEl) {
        errorEl.classList.remove('hidden');
        const msgEl = errorEl.querySelector('p');
        if (msgEl && message) msgEl.textContent = message;
    }
}

/**
 * Inizializza pagina quote
 */
async function initQuotePage() {
    currentSymbol = getSymbolFromURL();
    console.log('📊 Loading quote for:', currentSymbol);

    try {
        // Carica dati quote
        const quoteData = await fetchQuoteData(currentSymbol);
        updateQuotePage(quoteData);

        // Carica widget TradingView
        loadTradingViewWidget(currentSymbol);

        // Carica grafico storico (con piccolo delay)
        setTimeout(async () => {
            const chartData = await fetchChartData(currentSymbol);
            if (chartData) {
                createPriceChart(chartData);
            }
        }, 1500);

        // Auto-refresh ogni 60 secondi
        setInterval(async () => {
            try {
                const updated = await fetchQuoteData(currentSymbol);
                updateQuotePage(updated);
                console.log('🔄 Quote refreshed:', currentSymbol);
            } catch (err) {
                console.warn('Refresh failed:', err.message);
            }
        }, REFRESH_INTERVAL);

    } catch (error) {
        console.error('Error initializing quote page:', error);
        showError(error.message);
    }
}

// Avvia al caricamento DOM
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initQuotePage);
} else {
    initQuotePage();
}
