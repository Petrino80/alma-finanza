# 📘 Come Aggiornare Alma Finanza

## 🚀 Metodo Rapido (Consigliato)

Dopo che Claude ha modificato i file, esegui semplicemente:

```bash
./aggiorna.sh
```

Lo script farà automaticamente:
- ✅ Aggiungerà tutti i file modificati
- ✅ Creerà un commit con data/ora automatica
- ✅ Invierà tutto su GitHub
- ✅ Il sito si aggiornerà in 1-2 minuti

---

## 📝 Con Messaggio Personalizzato

Se vuoi un messaggio di commit personalizzato:

```bash
./aggiorna.sh "Aggiunti 3 nuovi articoli su Tesla e SpaceX"
```

---

## 🔧 Metodo Manuale (Alternativo)

Se preferisci fare tutto manualmente:

```bash
# 1. Aggiungi file
git add .

# 2. Crea commit
git commit -m "Descrizione modifiche"

# 3. Invia su GitHub
git push
```

---

## 🌐 Verificare l'Aggiornamento

Dopo 1-2 minuti, controlla:

**Sito live:**
- https://petrino80.github.io/alma-finanza/
- www.almafinanza.com (quando DNS configurato)

**Stato deployment GitHub:**
- https://github.com/Petrino80/alma-finanza/actions

---

## 💡 Workflow Completo

### Quando vuoi aggiornare il sito:

1. **Chiedi a Claude:** "Aggiorna gli articoli ad oggi"
2. **Claude modificherà** i file HTML nella cartella
3. **Tu esegui:** `./aggiorna.sh`
4. **Aspetta 1-2 minuti** e il sito è aggiornato! 🎉

---

## ❓ Domande Frequenti

### Lo script non funziona?

Assicurati di essere nella cartella corretta:

```bash
cd ~/Downloads/files-2
./aggiorna.sh
```

### Come vedo cosa è stato modificato?

Prima di eseguire lo script:

```bash
git status          # Vedi file modificati
git diff index.html # Vedi differenze in un file
```

### Come annullo modifiche non volute?

Se hai modificato file ma non hai ancora fatto push:

```bash
git checkout index.html  # Ripristina un file specifico
git reset --hard         # Ripristina tutto (ATTENZIONE!)
```

---

## 🔐 Sicurezza

- ✅ Tutti i file hanno backup su GitHub
- ✅ Puoi vedere la cronologia completa su GitHub
- ✅ Puoi tornare a versioni precedenti se necessario

---

**Creato con ❤️ per Alma Finanza**
