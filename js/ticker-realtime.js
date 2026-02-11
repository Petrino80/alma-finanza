/**
 * Alma Finanza - Ticker Real-Time con Alpha Vantage API
 * Aggiorna automaticamente i dati del ticker ogni 60 secondi
 */

const ALPHA_VANTAGE_API_KEY = '6WCELVI7XTDMD2E5';
const UPDATE_INTERVAL = 60000; // 60 secondi
const CACHE_DURATION = 300000; // 5 minuti cache

// Mapping simboli ticker -> Alpha Vantage symbols
const TICKER_SYMBOLS = {
    'dow': { symbol: 'DIA', type: 'ETF', name: 'Dow Jones' }, // DIA ETF traccia il Dow
    'sp500': { symbol: 'SPY', type: 'ETF', name: 'S&P 500' }, // SPY ETF traccia S&P 500
    'nasdaq': { symbol: 'QQQ', type: 'ETF', name: 'Nasdaq' }, // QQQ ETF traccia Nasdaq
    'ftsemib': { symbol: 'FTSEMIB.MI', type: 'INDEX', name: 'FTSE MIB' },
    'nvda': { symbol: 'NVDA', type: 'STOCK', name: 'Nvidia' },
    'race': { symbol: 'RACE', type: 'STOCK', name: 'Ferrari' },
    'kd': { symbol: 'KD', type: 'STOCK', name: 'Kyndryl' },
    'stm': { symbol: 'STM', type: 'STOCK', name: 'STMicroelectronics' },
    'gev': { symbol: 'GEV', type: 'STOCK', name: 'GE Vernova' },
    'rr': { symbol: 'RR.L', type: 'STOCK', name: 'Rolls-Royce' }
};

// Cache per ridurre chiamate API
const priceCache = {};

/**
 * Fetch prezzo da Alpha Vantage API
 */
async function fetchQuote(symbol) {
    // Check cache
    const cached = priceCache[symbol];
    if (cached && (Date.now() - cached.timestamp) < CACHE_DURATION) {
        console.log(`📦 Cache hit for ${symbol}`);
        return cached.data;
    }

    try {
        const url = `https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=${symbol}&apikey=${ALPHA_VANTAGE_API_KEY}`;
        const response = await fetch(url);
        const data = await response.json();

        if (data['Global Quote']) {
            const quote = data['Global Quote'];
            const result = {
                price: parseFloat(quote['05. price']),
                change: parseFloat(quote['09. change']),
                changePercent: parseFloat(quote['10. change percent'].replace('%', '')),
                volume: parseInt(quote['06. volume']),
                timestamp: Date.now()
            };

            // Salva in cache
            priceCache[symbol] = {
                data: result,
                timestamp: Date.now()
            };

            console.log(`✅ Fetched ${symbol}: $${result.price} (${result.changePercent > 0 ? '+' : ''}${result.changePercent.toFixed(2)}%)`);
            return result;
        } else if (data['Note']) {
            console.warn('⚠️ API limit reached:', data['Note']);
            return null;
        } else {
            console.error('❌ Error fetching quote:', data);
            return null;
        }
    } catch (error) {
        console.error(`❌ Error fetching ${symbol}:`, error);
        return null;
    }
}

/**
 * Formatta numero con separatori migliaia
 */
function formatNumber(num) {
    if (num >= 1000) {
        return (num / 1000).toFixed(3).replace('.', '.');
    }
    return num.toFixed(2);
}

/**
 * Aggiorna singolo elemento ticker nel DOM
 */
function updateTickerElement(elementId, data, indexName) {
    const elements = document.querySelectorAll(`[data-ticker="${elementId}"]`);

    elements.forEach(element => {
        if (!data) return;

        const isPositive = data.changePercent >= 0;
        const sign = isPositive ? '+' : '';
        const changeClass = isPositive ? 'positive' : 'negative';

        // Aggiorna il contenuto
        const priceFormatted = formatNumber(data.price);
        const changeFormatted = `${sign}${data.changePercent.toFixed(2)}%`;

        element.innerHTML = `${indexName} <span class="${changeClass}">${priceFormatted} (${changeFormatted})</span>`;

        // Animazione flash quando aggiorna
        element.style.backgroundColor = isPositive ? 'rgba(16, 185, 129, 0.2)' : 'rgba(239, 68, 68, 0.2)';
        setTimeout(() => {
            element.style.backgroundColor = 'transparent';
        }, 500);
    });
}

/**
 * Aggiorna tutti i ticker
 */
async function updateAllTickers() {
    console.log('🔄 Updating all tickers...');

    // Aggiorna Dow Jones (DIA ETF)
    const dowData = await fetchQuote(TICKER_SYMBOLS.dow.symbol);
    if (dowData) {
        updateTickerElement('dow', dowData, '🇺🇸 Dow');
    }

    // Pausa tra chiamate per non saturare API
    await sleep(1000);

    // Aggiorna S&P 500 (SPY ETF)
    const sp500Data = await fetchQuote(TICKER_SYMBOLS.sp500.symbol);
    if (sp500Data) {
        updateTickerElement('sp500', sp500Data, '🇺🇸 S&P 500');
    }

    await sleep(1000);

    // Aggiorna Nasdaq (QQQ ETF)
    const nasdaqData = await fetchQuote(TICKER_SYMBOLS.nasdaq.symbol);
    if (nasdaqData) {
        updateTickerElement('nasdaq', nasdaqData, '🇺🇸 Nasdaq');
    }

    await sleep(1000);

    // Aggiorna Nvidia
    const nvdaData = await fetchQuote(TICKER_SYMBOLS.nvda.symbol);
    if (nvdaData) {
        updateTickerElement('nvda', nvdaData, 'Nvidia');
    }

    await sleep(1000);

    // Aggiorna Ferrari
    const raceData = await fetchQuote(TICKER_SYMBOLS.race.symbol);
    if (raceData) {
        updateTickerElement('race', raceData, '🏎️ Ferrari RACE');
    }

    await sleep(1000);

    // Aggiorna Kyndryl
    const kdData = await fetchQuote(TICKER_SYMBOLS.kd.symbol);
    if (kdData) {
        updateTickerElement('kd', kdData, '🚨 Kyndryl');
    }

    await sleep(1000);

    // Aggiorna STMicroelectronics
    const stmData = await fetchQuote(TICKER_SYMBOLS.stm.symbol);
    if (stmData) {
        updateTickerElement('stm', stmData, 'STMicroelectronics');
    }

    await sleep(1000);

    // Aggiorna GE Vernova
    const gevData = await fetchQuote(TICKER_SYMBOLS.gev.symbol);
    if (gevData) {
        updateTickerElement('gev', gevData, 'GE Vernova');
    }

    console.log('✅ All tickers updated!');
}

/**
 * Sleep utility
 */
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

/**
 * Inizializza ticker real-time
 */
function initRealtimeTicker() {
    console.log('🚀 Initializing real-time ticker...');
    console.log(`⏱️ Update interval: ${UPDATE_INTERVAL / 1000} seconds`);
    console.log(`💾 Cache duration: ${CACHE_DURATION / 1000} seconds`);

    // Aggiorna immediatamente al caricamento
    updateAllTickers();

    // Aggiorna ogni 60 secondi
    setInterval(updateAllTickers, UPDATE_INTERVAL);

    console.log('✅ Real-time ticker initialized!');
}

// Auto-start quando il DOM è pronto
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initRealtimeTicker);
} else {
    initRealtimeTicker();
}

// Esporta funzioni per uso esterno
window.AlmaFinanza = {
    fetchQuote,
    updateAllTickers,
    TICKER_SYMBOLS
};
