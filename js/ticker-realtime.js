/**
 * Alma Finanza - Ticker Real-Time con Alpha Vantage API
 * Aggiorna automaticamente TUTTI i dati del ticker ogni 60 secondi
 */

const ALPHA_VANTAGE_API_KEY = '6WCELVI7XTDMD2E5';
const UPDATE_INTERVAL = 60000;   // 60 secondi tra refresh completi
const CACHE_DURATION  = 300000;  // 5 minuti cache per non sprecare quota API
const API_DELAY       = 1200;    // 1.2 secondi tra chiamate (max 5 req/min free tier)

// Tutti i simboli da aggiornare nel ticker
const TICKER_SYMBOLS = [
    { id: 'dow',    symbol: 'DIA',        label: '🇺🇸 Dow',              prefix: '' },
    { id: 'sp500',  symbol: 'SPY',        label: '🇺🇸 S&P 500',          prefix: '' },
    { id: 'nasdaq', symbol: 'QQQ',        label: '🇺🇸 Nasdaq',           prefix: '' },
    { id: 'ftsemib',symbol: 'FTSEMIB.MI', label: '🇮🇹 FTSE MIB',         prefix: '' },
    { id: 'nikkei', symbol: 'EWJ',        label: '🇯🇵 Nikkei',           prefix: '' },  // EWJ ETF Giappone
    { id: 'nvda',   symbol: 'NVDA',       label: 'Nvidia',               prefix: '$' },
    { id: 'race',   symbol: 'RACE',       label: '🏎️ Ferrari',           prefix: '$' },
    { id: 'kd',     symbol: 'KD',         label: '🚨 Kyndryl',           prefix: '$' },
    { id: 'stm',    symbol: 'STM',        label: 'STMicro',              prefix: '$' },
    { id: 'gev',    symbol: 'GEV',        label: 'GE Vernova',           prefix: '$' },
    { id: 'rr',     symbol: 'RR.L',       label: 'Rolls-Royce',         prefix: '£' },
    { id: 'gold',   symbol: 'GLD',        label: 'Oro',                  prefix: '$' },  // GLD ETF oro
    { id: 'btc',    symbol: 'IBIT',       label: 'Bitcoin',              prefix: '$' },  // IBIT ETF Bitcoin
];

// Cache locale
const priceCache = {};

/* ── Utility ────────────────────────────────────────────────── */

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function formatPrice(num) {
    if (num >= 10000) return num.toLocaleString('it-IT', { maximumFractionDigits: 0 });
    if (num >= 100)   return num.toLocaleString('it-IT', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
    return num.toLocaleString('it-IT', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
}

/* ── Alpha Vantage fetch ─────────────────────────────────────── */

async function fetchQuote(symbol) {
    const cached = priceCache[symbol];
    if (cached && (Date.now() - cached.timestamp) < CACHE_DURATION) {
        return cached.data;
    }

    try {
        const url = `https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=${encodeURIComponent(symbol)}&apikey=${ALPHA_VANTAGE_API_KEY}`;
        const response = await fetch(url);
        const data = await response.json();

        const q = data['Global Quote'];
        if (q && q['05. price']) {
            const result = {
                price:         parseFloat(q['05. price']),
                change:        parseFloat(q['09. change']),
                changePercent: parseFloat(q['10. change percent'].replace('%', '')),
                volume:        parseInt(q['06. volume']),
            };
            priceCache[symbol] = { data: result, timestamp: Date.now() };
            console.log(`✅ ${symbol}: ${result.price} (${result.changePercent > 0 ? '+' : ''}${result.changePercent.toFixed(2)}%)`);
            return result;
        }

        if (data['Note'] || data['Information']) {
            console.warn(`⚠️ API rate limit per ${symbol} - limite 25 chiamate/giorno raggiunto`);
        }
        return null; // mantieni valori statici HTML se API non risponde
    } catch (err) {
        console.error(`❌ Fetch error ${symbol}:`, err);
        return null;
    }
}

/* ── DOM update ──────────────────────────────────────────────── */

function updateTickerElement(id, data, label, prefix) {
    if (!data) return;

    const els = document.querySelectorAll(`[data-ticker="${id}"]`);
    if (els.length === 0) return;

    const isPositive   = data.changePercent >= 0;
    const sign         = isPositive ? '+' : '';
    const changeClass  = isPositive ? 'positive' : 'negative';
    const priceStr     = prefix + formatPrice(data.price);
    const changeStr    = `${sign}${data.changePercent.toFixed(2)}%`;

    els.forEach(el => {
        // Preserva il link <a> se presente
        const link = el.querySelector('a');
        const inner = `${label} <span class="${changeClass}">${priceStr} (${changeStr})</span>`;

        if (link) {
            link.innerHTML = inner;
        } else {
            el.innerHTML = inner;
        }

        // Flash animation
        el.style.transition = 'background-color 0.3s';
        el.style.backgroundColor = isPositive ? 'rgba(16,185,129,0.25)' : 'rgba(239,68,68,0.25)';
        setTimeout(() => { el.style.backgroundColor = 'transparent'; }, 600);
    });
}

/* ── Main update loop ────────────────────────────────────────── */

async function updateAllTickers() {
    console.log('🔄 Updating tickers via Alpha Vantage API...');

    for (const t of TICKER_SYMBOLS) {
        const data = await fetchQuote(t.symbol);
        updateTickerElement(t.id, data, t.label, t.prefix);
        await sleep(API_DELAY);
    }

    // Aggiorna orario ultimo refresh visibile
    const el = document.getElementById('ticker-last-update');
    if (el) {
        const now = new Date();
        el.textContent = `Aggiornato: ${now.toLocaleTimeString('it-IT', { hour: '2-digit', minute: '2-digit' })}`;
    }

    console.log('✅ All tickers updated!');
}

/* ── Init ────────────────────────────────────────────────────── */

function initRealtimeTicker() {
    console.log('🚀 Alma Finanza Ticker Real-Time avviato');

    // Prima chiamata immediata
    updateAllTickers();

    // Aggiorna ogni 60 secondi
    setInterval(updateAllTickers, UPDATE_INTERVAL);
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initRealtimeTicker);
} else {
    initRealtimeTicker();
}

window.AlmaFinanza = { fetchQuote, updateAllTickers, TICKER_SYMBOLS };
