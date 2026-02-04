#!/bin/bash

# Script per aggiungere Google Analytics a tutti i file HTML

GA_CODE='<!-- Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-E88FFDTPMP"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('\''js'\'', new Date());
        gtag('\''config'\'', '\''G-E88FFDTPMP'\'');
    </script>

    '

# Lista di tutti i file HTML da aggiornare (escludendo index.html già fatto)
files=(
    "articolo-sp500-6921.html"
    "articolo-oro-crash-816.html"
    "articolo-ppi-05.html"
    "articolo-bitcoin-83463.html"
    "in-costruzione.html"
    "articolo-southwest-airlines-19.html"
    "articolo-microsoft-stabilizza.html"
    "articolo-kevin-warsh-fed.html"
    "articolo-ftse-mib-45847.html"
    "categoria-borsa-milano.html"
    "categoria-commodities.html"
    "categoria-crypto.html"
    "categoria-wall-street.html"
    "articolo-argento-crash-30.html"
    "articolo-bitcoin-74570.html"
    "articolo-palantir-surge.html"
    "articolo-salesforce-crash-ai.html"
    "articolo-novo-nordisk-crash.html"
    "articolo-tesla-produzione-q1.html"
    "articolo-spacex-xai-ecosistema.html"
    "articolo-unity-software-gaming.html"
    "articolo-sell-off-tech.html"
    "articolo-missione-alma-finanza.html"
    "impara-finanza.html"
)

echo "Aggiunta Google Analytics a ${#files[@]} file..."

for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        # Verifica se Google Analytics è già presente
        if grep -q "G-E88FFDTPMP" "$file"; then
            echo "✓ $file - Analytics già presente, skip"
        else
            # Aggiungi GA dopo il tag <head>
            sed -i '' "/<head>/a\\
$GA_CODE
" "$file"
            echo "✓ $file - Analytics aggiunto"
        fi
    else
        echo "✗ $file - File non trovato"
    fi
done

echo ""
echo "Completato! Google Analytics aggiunto a tutti i file."
