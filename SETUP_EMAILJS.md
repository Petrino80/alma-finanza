# 📧 Setup EmailJS per Newsletter Alma Finanza

## Step 1: Crea Account EmailJS (GRATIS)

1. Vai su **https://www.emailjs.com/**
2. Clicca "Sign Up" (registrati con Google o email)
3. **Gratuito**: 200 email/mese gratis

---

## Step 2: Aggiungi Email Service

1. Dashboard EmailJS → **"Email Services"** → **"Add New Service"**
2. Scegli **Gmail** (più semplice)
3. Clicca **"Connect Account"** e autorizza con il tuo Gmail
4. Copia il **Service ID** (tipo: `service_abc123`)

---

## Step 3: Crea Email Template

1. Dashboard → **"Email Templates"** → **"Create New Template"**
2. Imposta così:

**Template Name**: `newsletter_signup`

**Subject**: `Nuova iscrizione Newsletter Alma Finanza`

**Content** (corpo email):
```
Nuova iscrizione alla newsletter!

Email iscritto: {{from_email}}

Messaggio: {{message}}

---
Alma Finanza Newsletter System
```

3. Salva e copia il **Template ID** (tipo: `template_xyz789`)

---

## Step 4: Ottieni Public Key

1. Dashboard → **Account** → **General**
2. Trova **"Public Key"** (tipo: `AbCdEfGhIjKlMnOp`)
3. Copia questa chiave

---

## Step 5: Aggiorna index.html

Apri `index.html` e sostituisci questi 3 valori nello script:

```javascript
emailjs.init("YOUR_PUBLIC_KEY"); // ← Metti la tua Public Key

emailjs.send('YOUR_SERVICE_ID', 'YOUR_TEMPLATE_ID', templateParams)
//           ↑                  ↑
//   Service ID (Step 2)    Template ID (Step 3)
```

**Esempio:**
```javascript
emailjs.init("AbCdEfGhIjKlMnOp");
emailjs.send('service_abc123', 'template_xyz789', templateParams)
```

---

## Step 6: Testa!

1. Vai su www.almafinanza.com
2. Inserisci una email nel form newsletter
3. Clicca "Iscriviti"
4. Dovresti ricevere l'email a `ferrarapetrino@gmail.com`

---

## ✅ Cosa succede quando qualcuno si iscrive?

1. Utente inserisce email nel form
2. EmailJS invia email a **newsletter@almafinanza.com**
3. Ricevi: "Nuova iscrizione da: nome@example.com"
4. Puoi copiare le email e aggiungerle manualmente a una lista

---

## 💡 Pro Tip: Crea un Google Sheet automatico

Se vuoi automatizzare la raccolta:
1. Usa **Zapier** o **Make.com** (gratis fino a 100/mese)
2. Trigger: "Nuova email ricevuta da EmailJS"
3. Action: "Aggiungi riga a Google Sheets"
4. Tutte le iscrizioni vanno automaticamente nel foglio!

---

## 🚨 Importante

- Limite gratuito: **200 email/mese**
- Se superi, passa a piano pagamento ($9/mese per 1000 email)
- Per ora 200/mese sono più che sufficienti!

---

**Domande?** Dimmi se hai problemi con la configurazione! 🚀
