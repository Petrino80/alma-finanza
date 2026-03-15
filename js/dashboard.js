/**
 * Alma Finanza - Dashboard Mercati
 * Heatmap, Top Gainers, Top Losers
 * Fonte dati: Yahoo Finance v8 chart API (no auth required)
 * Strategia: richieste parallele per simbolo via CORS proxy
 */

const REFRESH_INTERVAL = 300000; // 5 minuti

// CORS proxy list — si provano in ordine, con fallback
const CORS_PROXIES = [
    { prefix: 'https://corsproxy.io/?url=', encode: true },
    { prefix: 'https://api.allorigins.win/raw?url=', encode: true },
    { prefix: 'https://thingproxy.freeboard.io/fetch/', encode: false },
];
let workingProxy = null; // cache del proxy funzionante

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
 * Costruisce URL del proxy
 */
function buildProxyUrl(proxy, targetUrl) {
    return proxy.prefix + (proxy.encode ? encodeURIComponent(targetUrl) : targetUrl);
}

/**
 * Trova un proxy funzionante testando AAPL
 */
async function findWorkingProxy() {
    const testUrl = 'https://query2.finance.yahoo.com/v8/finance/chart/AAPL?range=1d&interval=1d&includePrePost=false';

    for (let i = 0; i < CORS_PROXIES.length; i++) {
        const proxy = CORS_PROXIES[i];
        const url = buildProxyUrl(proxy, testUrl);
        try {
            console.log(`🔍 Test proxy ${i + 1}: ${proxy.prefix.substring(0, 40)}...`);
            const resp = await fetch(url, { signal: AbortSignal.timeout(8000) });
            if (!resp.ok) continue;
            const data = await resp.json();
            if (data.chart && data.chart.result && data.chart.result.length > 0) {
                console.log(`✅ Proxy ${i + 1} funzionante!`);
                return proxy;
            }
        } catch (e) {
            console.warn(`❌ Proxy ${i + 1} fallito: ${e.message}`);
        }
    }

    // Tentativo diretto (senza proxy, funziona da alcune reti)
    try {
        console.log('🔍 Test connessione diretta Yahoo Finance...');
        const resp = await fetch(testUrl, { signal: AbortSignal.timeout(8000) });
        if (resp.ok) {
            const data = await resp.json();
            if (data.chart && data.chart.result) {
                console.log('✅ Connessione diretta funzionante!');
                return { prefix: '', encode: false };
            }
        }
    } catch (e) {
        console.warn('❌ Connessione diretta fallita');
    }

    return null;
}

/**
 * Fetch singolo simbolo da Yahoo v8 chart
 */
async function fetchSingleQuote(symbol, proxy) {
    const yahooUrl = `https://query2.finance.yahoo.com/v8/finance/chart/${symbol}?range=1d&interval=1d&includePrePost=false`;
    const url = proxy.prefix ? buildProxyUrl(proxy, yahooUrl) : yahooUrl;

    try {
        const resp = await fetch(url, { signal: AbortSignal.timeout(10000) });
        if (!resp.ok) return null;

        const data = await resp.json();
        if (!data.chart || !data.chart.result || data.chart.result.length === 0) return null;

        const result = data.chart.result[0];
        const meta = result.meta;

        const price = meta.regularMarketPrice || 0;
        const prevClose = meta.chartPreviousClose || meta.previousClose || price;
        const change = price - prevClose;
        const changePercent = prevClose > 0 ? (change / prevClose) * 100 : 0;

        return {
            symbol: symbol,
            price: price,
            change: change,
            changePercent: changePercent,
            high: meta.regularMarketDayHigh || price,
            low: meta.regularMarketDayLow || price,
            open: meta.regularMarketOpen || price,
            previousClose: prevClose,
            volume: meta.regularMarketVolume || 0,
        };
    } catch (e) {
        console.warn(`⚠️ ${symbol}: ${e.message}`);
        return null;
    }
}

/**
 * Colore celle heatmap
 */
function getColorClass(cp) {
    if (cp >= 5)  return 'gain-strong';
    if (cp >= 2)  return 'gain-moderate';
    if (cp > 0)   return 'gain-light';
    if (cp > -2)  return 'loss-light';
    if (cp > -5)  return 'loss-moderate';
    return 'loss-strong';
}

/**
 * Crea cella heatmap
 */
function createHeatmapCell(stock) {
    const cc = getColorClass(stock.changePercent);
    const sign = stock.changePercent >= 0 ? '+' : '';
    return `
        <a href="https://finance.yahoo.com/quote/${stock.symbol}" target="_blank"
           class="heatmap-cell ${cc} rounded-xl p-4 text-white shadow-lg flex flex-col justify-between h-32">
            <div>
                <div class="text-xs opacity-80">${stock.name}</div>
                <div class="text-lg font-bold">${stock.symbol}</div>
            </div>
            <div class="text-right">
                <div class="text-2xl font-bold">${sign}${stock.changePercent.toFixed(2)}%</div>
                <div class="text-sm opacity-90">$${stock.price.toFixed(2)}</div>
            </div>
        </a>`;
}

/**
 * Crea riga gainer/loser
 */
function createStockRow(stock, rank) {
    const pos = stock.changePercent >= 0;
    const sign = pos ? '+' : '';
    return `
        <a href="https://finance.yahoo.com/quote/${stock.symbol}" target="_blank"
           class="${pos ? 'bg-green-50' : 'bg-red-50'} hover:bg-opacity-80 rounded-lg p-4 flex items-center justify-between transition">
            <div class="flex items-center gap-4">
                <div class="text-2xl font-bold text-gray-400">#${rank}</div>
                <div>
                    <div class="font-bold text-gray-900">${stock.name}</div>
                    <div class="text-sm text-gray-500">${stock.symbol}</div>
                </div>
            </div>
            <div class="text-right">
                <div class="text-xl font-bold ${pos ? 'positive' : 'negative'}">${sign}${stock.changePercent.toFixed(2)}%</div>
                <div class="text-sm text-gray-600">$${stock.price.toFixed(2)}</div>
            </div>
        </a>`;
}

/**
 * Carica dati mercato — richieste parallele
 */
async function loadMarketData(market) {
    if (isLoading) return;
    isLoading = true;

    const symbols = MARKET_SYMBOLS[market];
    const container = document.getElementById('heatmap-container');
    container.innerHTML = '<div class="col-span-full text-center py-8 text-gray-600">⏳ Connessione a Yahoo Finance...</div>';

    // Trova proxy funzionante (o usa cache)
    if (!workingProxy) {
        workingProxy = await findWorkingProxy();
    }

    if (!workingProxy) {
        container.innerHTML = `
            <div class="col-span-full text-center py-12">
                <p class="text-2xl mb-2">🔌</p>
                <p class="text-gray-600 font-semibold mb-1">Impossibile connettersi a Yahoo Finance</p>
                <p class="text-gray-400 text-sm mb-4">Tutti i proxy CORS sono irraggiungibili. Riprova tra qualche minuto.</p>
                <button onclick="retryLoad()" class="px-6 py-2 bg-teal-500 text-white rounded-lg hover:bg-teal-600 transition text-sm">🔄 Riprova</button>
            </div>`;
        isLoading = false;
        return;
    }

    container.innerHTML = '<div class="col-span-full text-center py-8 text-gray-600">⏳ Caricamento dati di mercato...</div>';

    // Nome mappa
    const nameMap = {};
    symbols.forEach(s => { nameMap[s.symbol] = s.name; });

    // Fetch parallelo di tutti i simboli
    console.log(`📊 Loading ${market}: ${symbols.length} simboli in parallelo...`);
    const promises = symbols.map(s => fetchSingleQuote(s.symbol, workingProxy));
    const results = await Promise.allSettled(promises);

    marketData[market] = [];
    results.forEach((r, i) => {
        if (r.status === 'fulfilled' && r.value) {
            r.value.name = nameMap[r.value.symbol] || r.value.symbol;
            marketData[market].push(r.value);
        }
    });

    console.log(`✅ ${market}: ${marketData[market].length}/${symbols.length} simboli caricati`);

    if (marketData[market].length > 0) {
        renderHeatmap(market);
        renderGainersLosers(market);
    } else {
        container.innerHTML = `
            <div class="col-span-full text-center py-12">
                <p class="text-2xl mb-2">⚠️</p>
                <p class="text-gray-600 font-semibold mb-1">Nessun dato disponibile</p>
                <p class="text-gray-400 text-sm mb-4">I mercati potrebbero essere chiusi. Riprova più tardi.</p>
                <button onclick="retryLoad()" class="px-6 py-2 bg-teal-500 text-white rounded-lg hover:bg-teal-600 transition text-sm">🔄 Riprova</button>
            </div>`;
    }

    updateStats(market);
    updateTimestamp();
    isLoading = false;
}

/**
 * Riprova: resetta proxy cache e ricarica
 */
async function retryLoad() {
    workingProxy = null;
    marketData[currentMarket] = [];
    await loadMarketData(currentMarket);
}

function renderHeatmap(market) {
    const container = document.getElementById('heatmap-container');
    const data = marketData[market] || [];
    if (data.length === 0) return;
    const sorted = [...data].sort((a, b) => b.changePercent - a.changePercent);
    container.innerHTML = sorted.map(s => createHeatmapCell(s)).join('');
}

function renderGainersLosers(market) {
    const data = marketData[market] || [];
    if (data.length === 0) return;

    const gainers = [...data].filter(s => s.changePercent > 0).sort((a, b) => b.changePercent - a.changePercent).slice(0, 5);
    const losers = [...data].filter(s => s.changePercent < 0).sort((a, b) => a.changePercent - b.changePercent).slice(0, 5);

    document.getElementById('top-gainers').innerHTML = gainers.length > 0
        ? gainers.map((s, i) => createStockRow(s, i + 1)).join('')
        : '<p class="text-gray-500 text-center py-8">Nessun titolo in rialzo</p>';

    document.getElementById('top-losers').innerHTML = losers.length > 0
        ? losers.map((s, i) => createStockRow(s, i + 1)).join('')
        : '<p class="text-gray-500 text-center py-8">Nessun titolo in ribasso</p>';
}

function updateStats(market) {
    const data = marketData[market] || [];
    document.getElementById('advancing-count').textContent = data.filter(s => s.changePercent > 0).length;
    document.getElementById('declining-count').textContent = data.filter(s => s.changePercent < 0).length;
    document.getElementById('unchanged-count').textContent = data.filter(s => s.changePercent === 0).length;
    const vol = data.reduce((sum, s) => sum + (s.volume || 0), 0);
    const volEl = document.getElementById('total-volume');
    if (volEl) volEl.textContent = formatVolume(vol);
}

function formatVolume(v) {
    if (v >= 1e9) return (v / 1e9).toFixed(2) + 'B';
    if (v >= 1e6) return (v / 1e6).toFixed(2) + 'M';
    if (v >= 1e3) return (v / 1e3).toFixed(2) + 'K';
    return v > 0 ? v.toString() : '-';
}

function updateTimestamp() {
    const el = document.getElementById('last-update');
    if (el) el.textContent = new Date().toLocaleString('it-IT');
}

async function initDashboard() {
    console.log('🚀 Alma Finanza Dashboard (Yahoo Finance v8)');
    await loadMarketData(currentMarket);

    document.querySelectorAll('.market-filter').forEach(btn => {
        btn.addEventListener('click', async (e) => {
            const market = e.currentTarget.dataset.market;
            if (!market || isLoading) return;

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

    setInterval(async () => {
        console.log('🔄 Auto-refresh...');
        marketData[currentMarket] = [];
        await loadMarketData(currentMarket);
    }, REFRESH_INTERVAL);
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initDashboard);
} else {
    initDashboard();
}
