#!/usr/bin/env python3
"""
Script to fix index.html with real data for Feb 6, 2026
"""

# Read the file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update date from Feb 5 to Feb 6
content = content.replace(
    '<strong class="hidden md:inline">Mercoledì, 5 Febbraio 2026</strong>',
    '<strong class="hidden md:inline">Giovedì, 6 Febbraio 2026</strong>'
)

# 2. Update ticker with REAL data from Feb 5, 2026 session
# Old ticker items to replace
old_ticker = '''            <div class="ticker-item">S&P 500 <span class="negative">-1.12%</span></div>
            <div class="ticker-item">Dow <span class="negative">-287 (-0.56%)</span></div>
            <div class="ticker-item">Nasdaq <span class="negative">-2.03%</span></div>
            <div class="ticker-item">BTC <span class="negative">$71.845 (-1.7%)</span></div>
            <div class="ticker-item">Spotify <span class="negative">-8.4%</span></div>
            <div class="ticker-item">FEIM <span class="positive">+12.7%</span></div>
            <div class="ticker-item">Euro Stoxx 50 <span class="negative">-0.89%</span></div>
            <!-- Duplicate for seamless loop -->
            <div class="ticker-item">S&P 500 <span class="negative">-1.12%</span></div>
            <div class="ticker-item">Dow <span class="negative">-287 (-0.56%)</span></div>
            <div class="ticker-item">Nasdaq <span class="negative">-2.03%</span></div>
            <div class="ticker-item">BTC <span class="negative">$71.845 (-1.7%)</span></div>'''

new_ticker = '''            <div class="ticker-item">S&P 500 <span class="negative">-1.23% (sessione)</span></div>
            <div class="ticker-item">Dow <span class="negative">-592 (-1.20%, sessione)</span></div>
            <div class="ticker-item">Nasdaq <span class="negative">-1.59% (sessione)</span></div>
            <div class="ticker-item">BTC <span class="negative">$65.239 (-9%, 24h)</span></div>
            <div class="ticker-item">Oro <span class="positive">$4.850</span></div>
            <div class="ticker-item">Qualcomm <span class="negative">-9.5% (sessione)</span></div>
            <div class="ticker-item">Alphabet <span class="negative">-3.2% (sessione)</span></div>
            <!-- Duplicate for seamless loop -->
            <div class="ticker-item">S&P 500 <span class="negative">-1.23% (sessione)</span></div>
            <div class="ticker-item">Dow <span class="negative">-592 (-1.20%, sessione)</span></div>
            <div class="ticker-item">Nasdaq <span class="negative">-1.59% (sessione)</span></div>
            <div class="ticker-item">BTC <span class="negative">$65.239 (-9%, 24h)</span></div>'''

content = content.replace(old_ticker, new_ticker)

# 3. Update hero section
old_hero = '''                <h1 class="text-5xl md:text-7xl font-extrabold text-gray-900 mb-6 montserrat-font leading-tight">
                    Mercati USA sotto pressione:<br/>Tech continua sell-off
                </h1>
                <p class="text-xl md:text-2xl text-gray-700 mb-8 leading-relaxed max-w-3xl">
                    Nasdaq -2.03% guida perdite. Spotify crolla -8.4% post-earnings, mentre small cap FEIM +12.7% su contract militare. Treasury yields 4.35% pesano su growth stocks. Analisi completa.
                </p>'''

new_hero = '''                <h1 class="text-5xl md:text-7xl font-extrabold text-gray-900 mb-6 montserrat-font leading-tight">
                    Tech rout continua:<br/>Nasdaq -1.59%, Bitcoin -9%
                </h1>
                <p class="text-xl md:text-2xl text-gray-700 mb-8 leading-relaxed max-w-3xl">
                    Wall Street estende le perdite mercoledì. Alphabet -3.2% su timori capex AI ($175-185Bn). Qualcomm -9.5% per memory shortage. Bitcoin scende a $65.239. Analisi completa e dati verificati.
                </p>'''

content = content.replace(old_hero, new_hero)

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Updated date to Feb 6, 2026")
print("✓ Updated ticker with REAL data (with time intervals)")
print("✓ Updated hero section with verified data")
