/**
 * Alma Finanza - Dashboard Mercati
 * Heatmap, Top Gainers, Top Losers con Alpha Vantage API
 */

const ALPHA_VANTAGE_API_KEY = '6WCELVI7XTDMD2E5';
const REFRESH_INTERVAL = 600000; // 10 minuti per dashboard (risparmia quota API)
const API_DELAY = 13000; // 13 secondi tra chiamate (max 5/min = 1 ogni 12s)

// Market symbols by category - RIDOTTI per rispettare limite 25 chiamate/giorno
const MARKET_SYMBOLS = {
    us: [
        { symbol: 'AAPL', name: 'Apple' },
        { symbol: 'MSFT', name: 'Microsoft' },
        { symbol: 'NVDA', name: 'Nvidia' },
        { symbol: 'META', name: 'Meta' },
        { symbol: 'TSLA', name: 'Tesla' },
        { symbol: 'JPM', name: 'JPMorgan' },
    ],
    tech: [
        { symbol: 'NVDA', name: 'Nvidia' },
        { symbol: 'AAPL', name: 'Apple' },
        { symbol: 'MSFT', name: 'Microsoft' },
        { symbol: 'META', name: 'Meta' },
        { symbol: 'AMD', name: 'AMD' },
        { symbol: 'AVGO', name: 'Broadcom' }
    ],
    energy: [
        { symbol: 'XOM', name: 'Exxon' },
        { symbol: 'CVX', name: 'Chevron' },
        { symbol: 'GEV', name: 'GE Vernova' },
        { symbol: 'NEE', name: 'NextEra' }
    ],
    europe: [
        { symbol: 'RACE', name: 'Ferrari' },
        { symbol: 'STM', name: 'STMicro' },
        { symbol: 'ASML', name: 'ASML' }
    ],
    asia: [
        { symbol: 'TSM', name: 'TSMC' },
        { symbol: 'SONY', name: 'Sony' },
        { symbol: 'TM', name: 'Toyota' }
    ]
};

let currentMarket = 'us';
let marketData = {};

/**
 * Sleep utility
 */
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

/**
 * Fetch quote from Alpha Vantage
 */
async function fetchQuote(symbol) {
    try {
        const url = `https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=${symbol}&apikey=${ALPHA_VANTAGE_API_KEY}`;
        const response = await fetch(url);
        const data = await response.json();

        if (data['Global Quote'] && Object.keys(data['Global Quote']).length > 0) {
            const quote = data['Global Quote'];
            return {
                symbol: quote['01. symbol'],
                name: symbol,
                price: parseFloat(quote['05. price']),
                change: parseFloat(quote['09. change']),
                changePercent: parseFloat(quote['10. change percent'].replace('%', '')),
                volume: parseInt(quote['06. volume'])
            };
        }

        // API limit raggiunto - mostra avviso
        if (data['Note'] || data['Information']) {
            console.warn(`⚠️ API limit raggiunto per ${symbol}`);
            showApiLimitWarning();
        }
        return null;
    } catch (error) {
        console.error(`Error fetching ${symbol}:`, error);
        return null;
    }
}

/**
 * Mostra avviso limite API
 */
function showApiLimitWarning() {
    const existing = document.getElementById('api-limit-warning');
    if (existing) return; // già mostrato

    const warning = document.createElement('div');
    warning.id = 'api-limit-warning';
    warning.className = 'fixed bottom-4 right-4 bg-yellow-100 border-l-4 border-yellow-500 text-yellow-800 p-4 rounded-lg shadow-lg z-50 max-w-sm';
    warning.innerHTML = `
        <div class="flex items-start gap-3">
            <span class="text-2xl">⚠️</span>
            <div>
                <p class="font-bold">Limite API raggiunto</p>
                <p class="text-sm mt-1">Alpha Vantage: max 25 chiamate/giorno (piano gratuito). I dati si aggiorneranno domani o aggiorna la key.</p>
                <button onclick="this.parentElement.parentElement.parentElement.remove()" class="mt-2 text-xs underline">Chiudi</button>
            </div>
        </div>
    `;
    document.body.appendChild(warning);
}

/**
 * Get color class based on change percent
 */
function getColorClass(changePercent) {
    if (changePercent >= 5) return 'gain-strong';
    if (changePercent >= 2) return 'gain-moderate';
    if (changePercent > 0) return 'gain-light';
    if (changePercent > -2) return 'loss-light';
    if (changePercent > -5) return 'loss-moderate';
    return 'loss-strong';
}

/**
 * Create heatmap cell
 */
function createHeatmapCell(stock) {
    const colorClass = getColorClass(stock.changePercent);
    const isPositive = stock.changePercent >= 0;
    const sign = isPositive ? '+' : '';

    return `
        <a href="quote.html?symbol=${stock.symbol}" target="_blank"
           class="heatmap-cell ${colorClass} rounded-xl p-4 text-white shadow-lg flex flex-col justify-between h-32">
            <div>
                <div class="text-xs opacity-80">${stock.name}</div>
                <div class="text-lg font-bold">${stock.symbol}</div>
            </div>
            <div class="text-right">
                <div class="text-2xl font-bold">
                    ${sign}${stock.changePercent.toFixed(2)}%
                </div>
                <div class="text-sm opacity-90">
                    $${stock.price.toFixed(2)}
                </div>
            </div>
        </a>
    `;
}

/**
 * Create gainer/loser row
 */
function createStockRow(stock, rank) {
    const isPositive = stock.changePercent >= 0;
    const sign = isPositive ? '+' : '';
    const changeClass = isPositive ? 'positive' : 'negative';
    const bgClass = isPositive ? 'bg-green-50' : 'bg-red-50';

    return `
        <a href="quote.html?symbol=${stock.symbol}" target="_blank"
           class="${bgClass} hover:bg-opacity-80 rounded-lg p-4 flex items-center justify-between transition">
            <div class="flex items-center gap-4">
                <div class="text-2xl font-bold text-gray-400">#${rank}</div>
                <div>
                    <div class="font-bold text-gray-900">${stock.name}</div>
                    <div class="text-sm text-gray-500">${stock.symbol}</div>
                </div>
            </div>
            <div class="text-right">
                <div class="text-xl font-bold ${changeClass}">
                    ${sign}${stock.changePercent.toFixed(2)}%
                </div>
                <div class="text-sm text-gray-600">
                    $${stock.price.toFixed(2)}
                </div>
            </div>
        </a>
    `;
}

/**
 * Load market data
 */
async function loadMarketData(market) {
    console.log(`📊 Loading ${market} market data...`);

    const symbols = MARKET_SYMBOLS[market];
    const container = document.getElementById('heatmap-container');
    container.innerHTML = '<div class="col-span-full text-center py-8 text-gray-600">Caricamento dati...</div>';

    marketData[market] = [];

    // Fetch all stocks with delay between calls
    for (let i = 0; i < symbols.length; i++) {
        const stock = symbols[i];
        const quote = await fetchQuote(stock.symbol);

        if (quote) {
            marketData[market].push({
                ...quote,
                name: stock.name
            });

            // Update heatmap progressively
            renderHeatmap(market);
        }

        // Delay between API calls (except last one)
        if (i < symbols.length - 1) {
            await sleep(API_DELAY);
        }
    }

    // Sort and render gainers/losers
    renderGainersLosers(market);
    updateStats(market);
    updateTimestamp();

    console.log(`✅ ${market} market data loaded!`);
}

/**
 * Render heatmap
 */
function renderHeatmap(market) {
    const container = document.getElementById('heatmap-container');
    const data = marketData[market] || [];

    if (data.length === 0) return;

    // Sort by change percent (descending)
    const sorted = [...data].sort((a, b) => b.changePercent - a.changePercent);

    container.innerHTML = sorted.map(stock => createHeatmapCell(stock)).join('');
}

/**
 * Render gainers and losers
 */
function renderGainersLosers(market) {
    const data = marketData[market] || [];

    if (data.length === 0) return;

    // Top 5 gainers
    const gainers = [...data]
        .filter(s => s.changePercent > 0)
        .sort((a, b) => b.changePercent - a.changePercent)
        .slice(0, 5);

    // Top 5 losers
    const losers = [...data]
        .filter(s => s.changePercent < 0)
        .sort((a, b) => a.changePercent - b.changePercent)
        .slice(0, 5);

    // Render gainers
    const gainersContainer = document.getElementById('top-gainers');
    if (gainers.length > 0) {
        gainersContainer.innerHTML = gainers.map((stock, i) => createStockRow(stock, i + 1)).join('');
    } else {
        gainersContainer.innerHTML = '<p class="text-gray-500 text-center py-8">Nessun gainer disponibile</p>';
    }

    // Render losers
    const losersContainer = document.getElementById('top-losers');
    if (losers.length > 0) {
        losersContainer.innerHTML = losers.map((stock, i) => createStockRow(stock, i + 1)).join('');
    } else {
        losersContainer.innerHTML = '<p class="text-gray-500 text-center py-8">Nessun loser disponibile</p>';
    }
}

/**
 * Update market stats
 */
function updateStats(market) {
    const data = marketData[market] || [];

    const advancing = data.filter(s => s.changePercent > 0).length;
    const declining = data.filter(s => s.changePercent < 0).length;
    const unchanged = data.filter(s => s.changePercent === 0).length;
    const totalVolume = data.reduce((sum, s) => sum + s.volume, 0);

    document.getElementById('advancing-count').textContent = advancing;
    document.getElementById('declining-count').textContent = declining;
    document.getElementById('unchanged-count').textContent = unchanged;
    document.getElementById('total-volume').textContent = formatVolume(totalVolume);
}

/**
 * Format volume
 */
function formatVolume(volume) {
    if (volume >= 1e9) return (volume / 1e9).toFixed(2) + 'B';
    if (volume >= 1e6) return (volume / 1e6).toFixed(2) + 'M';
    if (volume >= 1e3) return (volume / 1e3).toFixed(2) + 'K';
    return volume.toString();
}

/**
 * Update timestamp
 */
function updateTimestamp() {
    const now = new Date();
    document.getElementById('last-update').textContent = now.toLocaleString('it-IT');
}

/**
 * Initialize dashboard
 */
async function initDashboard() {
    console.log('🚀 Initializing dashboard...');

    // Load default market
    await loadMarketData(currentMarket);

    // Setup market filter buttons
    document.querySelectorAll('.market-filter').forEach(btn => {
        btn.addEventListener('click', async (e) => {
            const market = e.target.dataset.market;

            // Update active button
            document.querySelectorAll('.market-filter').forEach(b => {
                b.classList.remove('active');
                b.style.background = '';
                b.style.color = '';
                b.classList.add('bg-gray-100', 'hover:bg-gray-200');
            });
            e.target.classList.add('active');
            e.target.classList.remove('bg-gray-100', 'hover:bg-gray-200');
            e.target.style.background = '#14b8a6';
            e.target.style.color = 'white';

            currentMarket = market;

            // Load new market data if not cached
            if (!marketData[market] || marketData[market].length === 0) {
                await loadMarketData(market);
            } else {
                renderHeatmap(market);
                renderGainersLosers(market);
                updateStats(market);
            }
        });
    });

    // Auto-refresh every 5 minutes
    setInterval(async () => {
        console.log('🔄 Auto-refreshing dashboard...');
        await loadMarketData(currentMarket);
    }, REFRESH_INTERVAL);

    console.log('✅ Dashboard initialized!');
}

// Start when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initDashboard);
} else {
    initDashboard();
}
