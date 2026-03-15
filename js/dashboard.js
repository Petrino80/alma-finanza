/**
 * Alma Finanza - Dashboard Mercati
 * Heatmap, Top Gainers, Top Losers
 * Fonte dati: Yahoo Finance (via CORS proxy)
 */

const REFRESH_INTERVAL = 300000; // 5 minuti
const CORS_PROXIES = [
    'https://corsproxy.io/?',
    'https://api.allorigins.win/raw?url='
];
let activeProxy = 0;

// Simboli per categoria
const MARKET_SYMBOLS = {
    us: [
        { symbol: 'AAPL',  name: 'Apple' },
        { symbol: 'MSFT',  name: 'Microsoft' },
        { symbol: 'NVDA',  name: 'Nvidia' },
        { symbol: 'META',  name: 'Meta' },
        { symbol: 'TSLA',  name: 'Tesla' },
        { symbol: 'JPM',   name: 'JPMorgan' },
        { symbol: 'AMZN',  name: 'Amazon' },
        { symbol: 'GOOGL', name: 'Alphabet' },
    ],
    tech: [
        { symbol: 'NVDA',  name: 'Nvidia' },
        { symbol: 'AAPL',  name: 'Apple' },
        { symbol: 'MSFT',  name: 'Microsoft' },
        { symbol: 'META',  name: 'Meta' },
        { symbol: 'AMD',   name: 'AMD' },
        { symbol: 'AVGO',  name: 'Broadcom' },
        { symbol: 'INTC',  name: 'Intel' },
        { symbol: 'QCOM',  name: 'Qualcomm' },
    ],
    energy: [
        { symbol: 'XOM',   name: 'Exxon' },
        { symbol: 'CVX',   name: 'Chevron' },
        { symbol: 'GEV',   name: 'GE Vernova' },
        { symbol: 'NEE',   name: 'NextEra' },
        { symbol: 'BP',    name: 'BP' },
        { symbol: 'SHEL',  name: 'Shell' },
    ],
    europe: [
        { symbol: 'RACE',  name: 'Ferrari' },
        { symbol: 'STM',   name: 'STMicro' },
        { symbol: 'ASML',  name: 'ASML' },
        { symbol: 'SAP',   name: 'SAP' },
        { symbol: 'NVO',   name: 'Novo Nordisk' },
        { symbol: 'LVMUY', name: 'LVMH' },
    ],
    asia: [
        { symbol: 'TSM',   name: 'TSMC' },
        { symbol: 'SONY',  name: 'Sony' },
        { symbol: 'TM',    name: 'Toyota' },
        { symbol: 'BABA',  name: 'Alibaba' },
        { symbol: 'TCEHY', name: 'Tencent' },
    ]
};

let currentMarket = 'us';
let marketData = {};
let isLoading = false;

/**
 * Fetch quotes da Yahoo Finance (batch, via CORS proxy)
 */
async function fetchQuotes(symbols) {
    const symbolList = symbols.map(s => s.symbol).join(',');
    const yahooUrl = `https://query1.finance.yahoo.com/v7/finance/quote?symbols=${symbolList}&fields=symbol,regularMarketPrice,regularMarketChange,regularMarketChangePercent,regularMarketOpen,regularMarketDayHigh,regularMarketDayLow,regularMarketPreviousClose,regularMarketVolume`;

    for (let p = 0; p < CORS_PROXIES.length; p++) {
        const proxyIdx = (activeProxy + p) % CORS_PROXIES.length;
        const proxyUrl = CORS_PROXIES[proxyIdx] + encodeURIComponent(yahooUrl);

        try {
            console.log(`📡 Tentativo proxy ${proxyIdx + 1}...`);
            const response = await fetch(proxyUrl, { signal: AbortSignal.timeout(10000) });

            if (!response.ok) {
                console.warn(`⚠️ Proxy ${proxyIdx + 1}: HTTP ${response.status}`);
                continue;
            }

            const data = await response.json();

            if (data.quoteResponse && data.quoteResponse.result) {
                activeProxy = proxyIdx;
                return data.quoteResponse.result;
            }

            console.warn('⚠️ Risposta Yahoo non valida:', data);
        } catch (error) {
            console.warn(`⚠️ Proxy ${proxyIdx + 1} fallito:`, error.message);
        }
    }

    return null;
}

/**
 * Trasforma risposta Yahoo in formato dashboard
 */
function parseYahooQuote(quote, nameMap) {
    const price = quote.regularMarketPrice || 0;
    const change = quote.regularMarketChange || 0;
    const changePercent = quote.regularMarketChangePercent || 0;

    return {
        symbol: quote.symbol,
        name: nameMap[quote.symbol] || quote.shortName || quote.symbol,
        price: price,
        change: change,
        changePercent: changePercent,
        high: quote.regularMarketDayHigh || price,
        low: quote.regularMarketDayLow || price,
        open: quote.regularMarketOpen || price,
        previousClose: quote.regularMarketPreviousClose || price,
        volume: quote.regularMarketVolume || 0,
    };
}

/**
 * Colore celle heatmap in base alla variazione
 */
function getColorClass(changePercent) {
    if (changePercent >= 5)  return 'gain-strong';
    if (changePercent >= 2)  return 'gain-moderate';
    if (changePercent > 0)   return 'gain-light';
    if (changePercent > -2)  return 'loss-light';
    if (changePercent > -5)  return 'loss-moderate';
    return 'loss-strong';
}

/**
 * Crea cella heatmap
 */
function createHeatmapCell(stock) {
    const colorClass = getColorClass(stock.changePercent);
    const isPositive = stock.changePercent >= 0;
    const sign = isPositive ? '+' : '';

    return `
        <a href="https://finance.yahoo.com/quote/${stock.symbol}" target="_blank"
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
 * Crea riga gainer/loser
 */
function createStockRow(stock, rank) {
    const isPositive = stock.changePercent >= 0;
    const sign = isPositive ? '+' : '';
    const changeClass = isPositive ? 'positive' : 'negative';
    const bgClass = isPositive ? 'bg-green-50' : 'bg-red-50';

    return `
        <a href="https://finance.yahoo.com/quote/${stock.symbol}" target="_blank"
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
 * Carica dati mercato
 */
async function loadMarketData(market) {
    if (isLoading) return;
    isLoading = true;

    console.log(`📊 Loading ${market} via Yahoo Finance...`);

    const symbols = MARKET_SYMBOLS[market];
    const container = document.getElementById('heatmap-container');
    container.innerHTML = '<div class="col-span-full text-center py-8 text-gray-600">⏳ Caricamento dati da Yahoo Finance...</div>';

    // Mappa nome per simbolo
    const nameMap = {};
    symbols.forEach(s => { nameMap[s.symbol] = s.name; });

    // Fetch batch da Yahoo Finance
    const quotes = await fetchQuotes(symbols);

    if (quotes && quotes.length > 0) {
        marketData[market] = quotes.map(q => parseYahooQuote(q, nameMap));
        console.log(`✅ ${market}: ${marketData[market].length} simboli caricati`);
    } else {
        marketData[market] = [];
        container.innerHTML = `
            <div class="col-span-full text-center py-12">
                <p class="text-2xl mb-2">⚠️</p>
                <p class="text-gray-600 font-semibold mb-1">Nessun dato disponibile</p>
                <p class="text-gray-400 text-sm mb-4">I mercati potrebbero essere chiusi o i dati non ancora aggiornati.</p>
                <button onclick="retryLoad()" class="px-6 py-2 bg-teal-500 text-white rounded-lg hover:bg-teal-600 transition text-sm">
                    🔄 Riprova
                </button>
            </div>
        `;
    }

    if (marketData[market].length > 0) {
        renderHeatmap(market);
        renderGainersLosers(market);
    }
    updateStats(market);
    updateTimestamp();

    isLoading = false;
}

/**
 * Riprova caricamento
 */
async function retryLoad() {
    activeProxy = (activeProxy + 1) % CORS_PROXIES.length;
    marketData[currentMarket] = [];
    await loadMarketData(currentMarket);
}

/**
 * Render heatmap
 */
function renderHeatmap(market) {
    const container = document.getElementById('heatmap-container');
    const data = marketData[market] || [];
    if (data.length === 0) return;

    const sorted = [...data].sort((a, b) => b.changePercent - a.changePercent);
    container.innerHTML = sorted.map(stock => createHeatmapCell(stock)).join('');
}

/**
 * Render gainers e losers
 */
function renderGainersLosers(market) {
    const data = marketData[market] || [];
    if (data.length === 0) return;

    const gainers = [...data].filter(s => s.changePercent > 0)
        .sort((a, b) => b.changePercent - a.changePercent).slice(0, 5);

    const losers = [...data].filter(s => s.changePercent < 0)
        .sort((a, b) => a.changePercent - b.changePercent).slice(0, 5);

    const gainersContainer = document.getElementById('top-gainers');
    gainersContainer.innerHTML = gainers.length > 0
        ? gainers.map((s, i) => createStockRow(s, i + 1)).join('')
        : '<p class="text-gray-500 text-center py-8">Nessun titolo in rialzo</p>';

    const losersContainer = document.getElementById('top-losers');
    losersContainer.innerHTML = losers.length > 0
        ? losers.map((s, i) => createStockRow(s, i + 1)).join('')
        : '<p class="text-gray-500 text-center py-8">Nessun titolo in ribasso</p>';
}

/**
 * Aggiorna statistiche mercato
 */
function updateStats(market) {
    const data = marketData[market] || [];

    document.getElementById('advancing-count').textContent = data.filter(s => s.changePercent > 0).length;
    document.getElementById('declining-count').textContent = data.filter(s => s.changePercent < 0).length;
    document.getElementById('unchanged-count').textContent = data.filter(s => s.changePercent === 0).length;

    const totalVolume = data.reduce((sum, s) => sum + (s.volume || 0), 0);
    const volEl = document.getElementById('total-volume');
    if (volEl) volEl.textContent = formatVolume(totalVolume);
}

/**
 * Formatta volume
 */
function formatVolume(v) {
    if (v >= 1e9) return (v / 1e9).toFixed(2) + 'B';
    if (v >= 1e6) return (v / 1e6).toFixed(2) + 'M';
    if (v >= 1e3) return (v / 1e3).toFixed(2) + 'K';
    return v > 0 ? v.toString() : '-';
}

/**
 * Aggiorna timestamp
 */
function updateTimestamp() {
    const el = document.getElementById('last-update');
    if (el) el.textContent = new Date().toLocaleString('it-IT');
}

/**
 * Inizializza dashboard
 */
async function initDashboard() {
    console.log('🚀 Alma Finanza Dashboard avviata (Yahoo Finance)');

    await loadMarketData(currentMarket);

    // Setup filtri mercato
    document.querySelectorAll('.market-filter').forEach(btn => {
        btn.addEventListener('click', async (e) => {
            const market = e.currentTarget.dataset.market;
            if (!market || isLoading) return;

            // Aggiorna stile pulsanti
            document.querySelectorAll('.market-filter').forEach(b => {
                b.classList.remove('active');
                b.style.background = '';
                b.style.color = '';
                b.classList.add('bg-gray-100', 'hover:bg-gray-200');
            });
            e.currentTarget.classList.add('active');
            e.currentTarget.classList.remove('bg-gray-100', 'hover:bg-gray-200');
            e.currentTarget.style.background = '#14b8a6';
            e.currentTarget.style.color = 'white';

            currentMarket = market;

            if (!marketData[market] || marketData[market].length === 0) {
                await loadMarketData(market);
            } else {
                renderHeatmap(market);
                renderGainersLosers(market);
                updateStats(market);
            }
        });
    });

    // Auto-refresh ogni 5 minuti
    setInterval(async () => {
        console.log('🔄 Auto-refresh dashboard...');
        marketData[currentMarket] = [];
        await loadMarketData(currentMarket);
    }, REFRESH_INTERVAL);

    console.log('✅ Dashboard pronta!');
}

// Avvia al caricamento DOM
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initDashboard);
} else {
    initDashboard();
}
