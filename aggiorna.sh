#!/bin/bash

# Script per aggiornare Alma Finanza su GitHub Pages
# Uso: ./aggiorna.sh "messaggio del commit"

# Colori per output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}🚀 Alma Finanza - Script di Aggiornamento${NC}"
echo "=========================================="
echo ""

# Verifica se è stato fornito un messaggio di commit
if [ -z "$1" ]; then
    # Se non c'è messaggio, usa uno di default con la data
    MESSAGGIO="Aggiornamento articoli del $(date '+%d/%m/%Y alle %H:%M')"
else
    MESSAGGIO="$1"
fi

echo -e "${BLUE}📝 Messaggio commit:${NC} $MESSAGGIO"
echo ""

# 1. Aggiungi tutti i file modificati
echo -e "${BLUE}📦 Aggiunta file modificati...${NC}"
git add .

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Errore nell'aggiunta dei file${NC}"
    exit 1
fi

echo -e "${GREEN}✅ File aggiunti${NC}"
echo ""

# 2. Verifica se ci sono modifiche da committare
if git diff --staged --quiet; then
    echo -e "${BLUE}ℹ️  Nessuna modifica da pubblicare${NC}"
    exit 0
fi

# 3. Crea il commit
echo -e "${BLUE}💾 Creazione commit...${NC}"
git commit -m "$MESSAGGIO"

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Errore nella creazione del commit${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Commit creato${NC}"
echo ""

# 4. Push su GitHub
echo -e "${BLUE}☁️  Invio modifiche a GitHub...${NC}"
git push

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Errore nel push su GitHub${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Modifiche inviate a GitHub${NC}"
echo ""

# 5. Messaggio finale
echo "=========================================="
echo -e "${GREEN}🎉 Aggiornamento completato!${NC}"
echo ""
echo -e "${BLUE}📍 Il tuo sito sarà aggiornato tra 1-2 minuti su:${NC}"
echo "   https://petrino80.github.io/alma-finanza/"
echo "   www.almafinanza.com (quando DNS configurato)"
echo ""
echo -e "${BLUE}💡 Per vedere lo stato del deployment:${NC}"
echo "   https://github.com/Petrino80/alma-finanza/actions"
echo ""
