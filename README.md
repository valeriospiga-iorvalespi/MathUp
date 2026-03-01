# Mate+ 🚀 — Matematica 2ª Media per studenti con DSA

[![License: MIT](https://img.shields.io/badge/License-MIT-orange.svg)](LICENSE)
[![PWA](https://img.shields.io/badge/PWA-ready-blue.svg)](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps)

> **Autore:** Valerio Spiga  
> **Versione:** 1.0 — 2026

Una **Progressive Web App (PWA)** pensata per studenti di **2ª Media** con **discalculia e disgrafia**, basata sulle indicazioni pedagogiche per i Disturbi Specifici dell'Apprendimento (DSA) — Legge 170/2010.

---

## 🎯 Obiettivi pedagogici

L'app segue i principi delle linee guida Erickson / MIUR per la didattica DSA:

- **Piccoli passi progressivi** — ogni argomento è introdotto visivamente prima degli esercizi
- **Zero scrittura a mano** — tutte le risposte si danno con un clic (ideale per disgrafia)
- **Strumenti compensativi sempre visibili** — calcolatrice, tavola pitagorica, foglio formule
- **Feedback immediato e positivo** — rinforzo visivo e sonoro (opzionale)
- **Formule inverse** — fondamentali ma spesso trascurate nella didattica tradizionale
- **Accessibilità** — testo grande, alto contrasto, font DSA (Nunito)

---

## 📚 Argomenti coperti (programma 2ª Media MIUR)

| Argomento | N° esercizi | Sessione | Formule inverse |
|-----------|-------------|----------|-----------------|
| Numeri Relativi | 100 | 20 a rotazione | — |
| Frazioni | 100 | 20 a rotazione | Reciproco, divisione |
| Geometria & Aree | 100 | 20 a rotazione | ✅ Trovare base, altezza, lato |
| Teorema di Pitagora | 100 | 20 a rotazione | ✅ Trovare un cateto |
| Algebra (intro) | 100 | 20 a rotazione | Equazioni di 1° grado |
| Statistica | 100 | 20 a rotazione | Media, Moda, Mediana |
| Potenze & Radicali | 100 | 20 a rotazione | ✅ Radice quadrata |

> Ogni sessione propone **20 esercizi scelti casualmente** tra i 100 disponibili per argomento, per un totale di **700 esercizi** nel database.

---

## 📲 Installazione su telefono

### iPhone / iPad (Safari)
1. Apri il sito su GitHub Pages
2. Tocca il pulsante **Condividi** (↑)
3. Seleziona **"Aggiungi alla schermata Home"**
4. Apparirà l'icona arancione **Mate+** sulla schermata Home

### Android (Chrome)
1. Apri il sito
2. Tocca i **tre puntini** ⋮ in alto a destra
3. Seleziona **"Aggiungi alla schermata Home"** oppure **"Installa app"**

> 📴 L'app funziona anche **offline** grazie al Service Worker!

---

## 🚀 Deploy su GitHub Pages

1. Fai fork di questo repository
2. Vai in **Settings → Pages**
3. Source: **Deploy from branch** → `main` → `/ (root)`
4. L'app sarà disponibile su: `https://[tuousername].github.io/mateplus/`

---

## 🗂 Struttura del progetto

```
mateplus/
├── index.html          # App principale (single-file PWA)
├── manifest.json       # Manifest PWA
├── sw.js               # Service Worker (cache offline)
├── favicon.ico         # Favicon 16/32/48px
├── icons/
│   ├── icon-72.png
│   ├── icon-96.png
│   ├── icon-128.png
│   ├── icon-144.png
│   ├── icon-152.png
│   ├── icon-192.png
│   ├── icon-384.png
│   └── icon-512.png
└── README.md
```

---

## ⚙️ Funzionalità tecniche

- **PWA completa**: installabile su home screen, offline support via `sw.js`
- **No framework**: HTML5 + CSS3 + Vanilla JS puro (nessuna dipendenza)
- **700 esercizi**: 100 per argomento, randomizzati con algoritmo Fisher-Yates
- **Sessioni da 20**: ogni sessione pesca 20 esercizi casuali dal database, con nuova selezione ad ogni riavvio
- **Ripasso Generale**: modalità che mescola tutte le categorie, con storico del miglior risultato
- **Canvas interattivi**: visualizzazioni di triangoli e figure geometriche
- **Calcolatrice integrata**: con pallottoliere visivo per numeri 1–20, memoria del risultato precedente
- **Progresso salvato**: usa `localStorage` per ricordare i punti tra sessioni
- **Font ottimizzato**: Nunito (arrotondato, leggibile per DSA)
- **Safe area insets**: compatibile con i notch degli iPhone

---

## 📖 Riferimenti pedagogici

- Legge 170/2010 — Nuove norme in materia di DSA
- Linee Guida MIUR per il diritto allo studio degli alunni e degli studenti con DSA
- Erickson — "Discalculia: riconoscimento e strategie"
- Pearson Academy — "Come affrontare la discalculia evolutiva a scuola"

---

## 📄 Licenza

MIT License — libero uso, modifica e distribuzione con attribuzione all'autore.

---

*Creato con 🧡 da **Valerio Spiga** — Head of Innovation Management, Allianz Italia*
