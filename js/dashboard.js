/**
 * Alma Finanza - Dashboard Mercati v4
 * Heatmap, Top Gainers, Top Losers
 *
 * Yahoo Finance v8 chart API via allorigins.win (wrapped JSON — più affidabile)
 * - Borse aperte: dati real-time, refresh ogni 60s
 * - Borse chiuse/weekend: ultimo dato di chiusura disponibile
 */

const REFRESH_OPEN = 60000;    // 1 minuto durante apertura
const REFRESH_CLOSED = 300000; // 5 minuti a mercato chiuso

// Proxy: allorigins.win/get wrappa la risposta → bypass CORS affidabile
const PROXY_GET = 'https://api.allorigins.win/get?url=';

// Simboli per categoria (25-30 per garantire top 10 gainers + losers)
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
        { symbol: 'BRK-B', name: 'Berkshire' },
        { symbol: 'UNH',   name: 'UnitedHealth' },
        { symbol: 'V',     name: 'Visa' },
        { symbol: 'JNJ',   name: 'J&J' },
        { symbol: 'WMT',   name: 'Walmart' },
        { symbol: 'PG',    name: 'P&G' },
        { symbol: 'MA',    name: 'Mastercard' },
        { symbol: 'HD',    name: 'Home Depot' },
        { symbol: 'DIS',   name: 'Disney' },
        { symbol: 'BAC',   name: 'BofA' },
        { symbol: 'KO',    name: 'Coca-Cola' },
        { symbol: 'PEP',   name: 'PepsiCo' },
        { symbol: 'NFLX',  name: 'Netflix' },
        { symbol: 'CRM',   name: 'Salesforce' },
        { symbol: 'ADBE',  name: 'Adobe' },
        { symbol: 'BA',    name: 'Boeing' },
        { symbol: 'GS',    name: 'Goldman Sachs' },
        { symbol: 'CAT',   name: 'Caterpillar' },
        { symbol: 'NKE',   name: 'Nike' },
        { symbol: 'MCD',   name: "McDonald's" },
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
        { symbol: 'CRM',   name: 'Salesforce' },
        { symbol: 'ADBE',  name: 'Adobe' },
        { symbol: 'ORCL',  name: 'Oracle' },
        { symbol: 'NOW',   name: 'ServiceNow' },
        { symbol: 'PLTR',  name: 'Palantir' },
        { symbol: 'UBER',  name: 'Uber' },
        { symbol: 'SHOP',  name: 'Shopify' },
        { symbol: 'SNOW',  name: 'Snowflake' },
        { symbol: 'SQ',    name: 'Block' },
        { symbol: 'NET',   name: 'Cloudflare' },
        { symbol: 'CRWD',  name: 'CrowdStrike' },
        { symbol: 'PANW',  name: 'Palo Alto' },
        { symbol: 'MU',    name: 'Micron' },
        { symbol: 'MRVL',  name: 'Marvell' },
        { symbol: 'COIN',  name: 'Coinbase' },
        { symbol: 'DELL',  name: 'Dell' },
        { symbol: 'ARM',   name: 'ARM Holdings' },
    ],
    energy: [
        { symbol: 'XOM',   name: 'Exxon' },
        { symbol: 'CVX',   name: 'Chevron' },
        { symbol: 'GEV',   name: 'GE Vernova' },
        { symbol: 'NEE',   name: 'NextEra' },
        { symbol: 'BP',    name: 'BP' },
        { symbol: 'SHEL',  name: 'Shell' },
        { symbol: 'COP',   name: 'ConocoPhillips' },
        { symbol: 'EOG',   name: 'EOG Resources' },
        { symbol: 'SLB',   name: 'Schlumberger' },
        { symbol: 'MPC',   name: 'Marathon Petrol' },
        { symbol: 'PSX',   name: 'Phillips 66' },
        { symbol: 'VLO',   name: 'Valero' },
        { symbol: 'OXY',   name: 'Occidental' },
        { symbol: 'HAL',   name: 'Halliburton' },
        { symbol: 'DVN',   name: 'Devon Energy' },
        { symbol: 'FANG',  name: 'Diamondback' },
        { symbol: 'BKR',   name: 'Baker Hughes' },
        { symbol: 'WMB',   name: 'Williams Cos' },
        { symbol: 'KMI',   name: 'Kinder Morgan' },
        { symbol: 'OKE',   name: 'ONEOK' },
        { symbol: 'ENPH',  name: 'Enphase' },
        { symbol: 'SEDG',  name: 'SolarEdge' },
        { symbol: 'FSLR',  name: 'First Solar' },
        { symbol: 'CEG',   name: 'Constellation' },
        { symbol: 'D',     name: 'Dominion' },
    ],
    europe: [
        { symbol: 'RACE',  name: 'Ferrari' },
        { symbol: 'STM',   name: 'STMicro' },
        { symbol: 'ASML',  name: 'ASML' },
        { symbol: 'SAP',   name: 'SAP' },
        { symbol: 'NVO',   name: 'Novo Nordisk' },
        { symbol: 'LVMUY', name: 'LVMH' },
        { symbol: 'AZN',   name: 'AstraZeneca' },
        { symbol: 'UL',    name: 'Unilever' },
        { symbol: 'HSBC',  name: 'HSBC' },
        { symbol: 'SNY',   name: 'Sanofi' },
        { symbol: 'DEO',   name: 'Diageo' },
        { symbol: 'RIO',   name: 'Rio Tinto' },
        { symbol: 'BHP',   name: 'BHP Group' },
        { symbol: 'GSK',   name: 'GSK' },
        { symbol: 'SAN',   name: 'Santander' },
        { symbol: 'STLA',  name: 'Stellantis' },
        { symbol: 'PHG',   name: 'Philips' },
        { symbol: 'NXPI',  name: 'NXP Semi' },
        { symbol: 'ING',   name: 'ING Group' },
        { symbol: 'DB',    name: 'Deutsche Bank' },
        { symbol: 'E',     name: 'ENI' },
        { symbol: 'EQNR',  name: 'Equinor' },
        { symbol: 'ABB',   name: 'ABB' },
        { symbol: 'WPP',   name: 'WPP' },
        { symbol: 'SPOT',  name: 'Spotify' },
    ],
    asia: [
        { symbol: 'TSM',   name: 'TSMC' },
        { symbol: 'SONY',  name: 'Sony' },
        { symbol: 'TM',    name: 'Toyota' },
        { symbol: 'BABA',  name: 'Alibaba' },
        { symbol: 'TCEHY', name: 'Tencent' },
        { symbol: 'PDD',   name: 'PDD Holdings' },
        { symbol: 'JD',    name: 'JD.com' },
        { symbol: 'BIDU',  name: 'Baidu' },
        { symbol: 'NIO',   name: 'NIO' },
        { symbol: 'XPEV',  name: 'XPeng' },
        { symbol: 'LI',    name: 'Li Auto' },
        { symbol: 'SE',    name: 'Sea Ltd' },
        { symbol: 'GRAB',  name: 'Grab' },
        { symbol: 'MELI',  name: 'MercadoLibre' },
        { symbol: 'HDB',   name: 'HDFC Bank' },
        { symbol: 'IBN',   name: 'ICICI Bank' },
        { symbol: 'INFY',  name: 'Infosys' },
        { symbol: 'WIT',   name: 'Wipro' },
        { symbol: 'KB',    name: 'KB Financial' },
        { symbol: 'SHG',   name: 'Shinhan' },
        { symbol: 'MFG',   name: 'Mizuho' },
        { symbol: 'SMFG',  name: 'Sumitomo' },
        { symbol: 'HMC',   name: 'Honda' },
        { symbol: 'NTDOY', name: 'Nintendo' },
        { symbol: 'SNE',   name: 'Sony Group' },
    ]
};

let currentMarket = 'us';
let marketData = {};
let isLoading = false;
let refreshTimer = null;
let marketIsOpen = false;

/**
 * Controlla se il mercato USA è aperto (lun-ven 9:30-16:00 ET)
 */
function isUSMarketOpen() {
    const now = new Date();
    const et = new Date(now.toLocaleString('en-US', { timeZone: 'America/New_York' }));
    const day = et.getDay(); // 0=dom, 6=sab
    const h = et.getHours();
    const m = et.getMinutes();
    const minutes = h * 60 + m;
    // Lun-Ven, 9:30 (570) - 16:00 (960)
    return day >= 1 && day <= 5 && minutes >= 570 && minutes < 960;
}

/**
 * Fetch singolo simbolo via allorigins.win/get (wrapped JSON)
 * Usa range=5d per avere sempre dati anche nel weekend
 */
async function fetchQuote(symbol) {
    const yahooUrl = `https://query2.finance.yahoo.com/v8/finance/chart/${symbol}?range=5d&interval=1d&includePrePost=false`;
    const url = PROXY_GET + encodeURIComponent(yahooUrl);

    try {
        const resp = await fetch(url, { signal: AbortSignal.timeout(12000) });
        if (!resp.ok) throw new Error(`HTTP ${resp.status}`);

        const wrapper = await resp.json();
        if (!wrapper.contents) throw new Error('No contents in wrapper');

        const data = JSON.parse(wrapper.contents);
        if (!data.chart || !data.chart.result || !data.chart.result[0]) return null;

        const result = data.chart.result[0];
        const meta = result.meta;
        const price = meta.regularMarketPrice || 0;

        // Raggruppa chiusure per data unica (Yahoo può dare 2 entry/giorno)
        const timestamps = result.timestamp || [];
        const closes = result.indicators?.quote?.[0]?.close || [];
        const dailyCloses = {};
        for (let i = 0; i < timestamps.length; i++) {
            if (closes[i] !== null && closes[i] !== undefined) {
                const dateKey = new Date(timestamps[i] * 1000).toISOString().split('T')[0];
                dailyCloses[dateKey] = closes[i];
            }
        }
        const sortedDays = Object.keys(dailyCloses).sort();
        let prevClose;
        if (sortedDays.length >= 2) {
            prevClose = dailyCloses[sortedDays[sortedDays.length - 2]];
        } else {
            prevClose = meta.chartPreviousClose || price;
        }
        const change = price - prevClose;
        const pct = prevClose > 0 ? (change / prevClose) * 100 : 0;

        return {
            symbol,
            price,
            change,
            changePercent: pct,
            high: meta.regularMarketDayHigh || price,
            low: meta.regularMarketDayLow || price,
            open: meta.regularMarketOpen || price,
            previousClose: prevClose,
            volume: meta.regularMarketVolume || 0,
            marketState: meta.marketState || 'CLOSED',
            exchangeTimezoneName: meta.exchangeTimezoneName || '',
        };
    } catch (e) {
        console.warn(`⚠️ ${symbol}: ${e.message}`);
        return null;
    }
}

/**
 * Colore heatmap
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
 * Cella heatmap
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
 * Riga gainer/loser
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
 * Carica dati — fetch parallelo
 */
async function loadMarketData(market) {
    if (isLoading) return;
    isLoading = true;

    const symbols = MARKET_SYMBOLS[market];
    const container = document.getElementById('heatmap-container');
    container.innerHTML = '<div class="col-span-full text-center py-8 text-gray-600">⏳ Caricamento dati da Yahoo Finance...</div>';

    const nameMap = {};
    symbols.forEach(s => { nameMap[s.symbol] = s.name; });

    // Fetch parallelo
    console.log(`📊 Loading ${market}: ${symbols.length} simboli...`);
    const results = await Promise.allSettled(symbols.map(s => fetchQuote(s.symbol)));

    marketData[market] = [];
    results.forEach(r => {
        if (r.status === 'fulfilled' && r.value) {
            r.value.name = nameMap[r.value.symbol] || r.value.symbol;
            marketData[market].push(r.value);
        }
    });

    console.log(`✅ ${market}: ${marketData[market].length}/${symbols.length} caricati`);

    // Determina stato mercato
    const firstStock = marketData[market][0];
    if (firstStock) {
        marketIsOpen = firstStock.marketState === 'REGULAR';
    } else {
        marketIsOpen = isUSMarketOpen();
    }

    if (marketData[market].length > 0) {
        renderHeatmap(market);
        renderGainersLosers(market);
    } else {
        container.innerHTML = `
            <div class="col-span-full text-center py-12">
                <p class="text-2xl mb-2">⚠️</p>
                <p class="text-gray-600 font-semibold mb-1">Dati non disponibili</p>
                <p class="text-gray-400 text-sm mb-4">Il servizio potrebbe essere temporaneamente non raggiungibile.</p>
                <button onclick="retryLoad()" class="px-6 py-2 bg-teal-500 text-white rounded-lg hover:bg-teal-600 transition text-sm">🔄 Riprova</button>
            </div>`;
    }

    updateStats(market);
    updateMarketStatus();
    updateTimestamp();

    // Imposta refresh rate in base allo stato del mercato
    setupRefreshTimer();

    isLoading = false;
}

/**
 * Mostra badge stato mercato
 */
function updateMarketStatus() {
    const el = document.getElementById('market-status');
    if (!el) return;

    if (marketIsOpen) {
        el.innerHTML = '<span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold bg-green-100 text-green-700"><span class="w-2 h-2 rounded-full bg-green-500 animate-pulse"></span>Mercato aperto — Dati real-time</span>';
    } else {
        el.innerHTML = '<span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold bg-gray-100 text-gray-600"><span class="w-2 h-2 rounded-full bg-gray-400"></span>Mercato chiuso — Ultima chiusura</span>';
    }
}

/**
 * Refresh timer: 60s se aperto, 5min se chiuso
 */
function setupRefreshTimer() {
    if (refreshTimer) clearInterval(refreshTimer);
    const interval = marketIsOpen ? REFRESH_OPEN : REFRESH_CLOSED;
    console.log(`⏱️ Refresh ogni ${interval / 1000}s (mercato ${marketIsOpen ? 'aperto' : 'chiuso'})`);
    refreshTimer = setInterval(async () => {
        console.log('🔄 Auto-refresh...');
        marketData[currentMarket] = [];
        await loadMarketData(currentMarket);
    }, interval);
}

async function retryLoad() {
    marketData[currentMarket] = [];
    await loadMarketData(currentMarket);
}

function renderHeatmap(market) {
    const container = document.getElementById('heatmap-container');
    const data = marketData[market] || [];
    if (!data.length) return;
    container.innerHTML = [...data].sort((a, b) => b.changePercent - a.changePercent).map(s => createHeatmapCell(s)).join('');
}

function renderGainersLosers(market) {
    const data = marketData[market] || [];
    if (!data.length) return;

    const gainers = [...data].filter(s => s.changePercent > 0).sort((a, b) => b.changePercent - a.changePercent).slice(0, 10);
    const losers  = [...data].filter(s => s.changePercent < 0).sort((a, b) => a.changePercent - b.changePercent).slice(0, 10);

    document.getElementById('top-gainers').innerHTML = gainers.map((s, i) => createStockRow(s, i + 1)).join('');
    document.getElementById('top-losers').innerHTML = losers.map((s, i) => createStockRow(s, i + 1)).join('');
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
    console.log('🚀 Alma Finanza Dashboard v4 (Yahoo Finance via allorigins)');
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

            if (!marketData[market] || !marketData[market].length) {
                await loadMarketData(market);
            } else {
                renderHeatmap(market);
                renderGainersLosers(market);
                updateStats(market);
            }
        });
    });
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initDashboard);
} else {
    initDashboard();
}
