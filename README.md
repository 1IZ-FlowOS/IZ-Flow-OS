# IZ-Flow OS

**IZ-Flow** ist ein experimentelles Betriebssystem-Konzept und eine eigene Script-Programmiersprache.
Das Ziel von IZ-Flow ist es, **komplexe Programmierung einfacher und chronologischer darzustellen**, damit neue Entwickler schneller verstehen können, wie Programme und Prozesse funktionieren.

Die Sprache nutzt **kurze Funktionskürzel und Hex-Werte**, um Systemprozesse, Logik und Ressourcen direkt zu steuern.

---

# 🧠 Grundidee

IZ-Flow basiert auf einer **linearen Prozesslogik**.

Statt verschachtelter Syntax beschreibt der Code einfach den Ablauf:

```
Befehl → Wert → Befehl → Wert
```

Beispiel:

```
syp{iz{1f{dr{04{wt{05{L{1
```

Bedeutung:

* **syp** → Systemprozess starten
* **iz{1f** → Wert setzen (Hex 1F)
* **dr{04** → Richtung rechts
* **wt{05** → 0,5 Sekunden warten
* **L{1** → Status aktiv

---

# 🌍 Zwei Sprachvarianten

IZ-Flow unterstützt zwei Kurzformen:

| Englisch | Deutsch | Bedeutung            |
| -------- | ------- | -------------------- |
| dr       | rg      | direction / Richtung |
| wt       | wt      | wait / warten        |
| if       | bj      | if / Bedingung       |

Beide Varianten führen zum **gleichen internen Befehl**.

---

# 🧱 Beispielprogramm

```
Z_↓

syp{L{1
dr{04
wt{05
dr{03

Z-
```

Ablauf:

1. Prozess starten
2. Bewegung nach rechts
3. Pause
4. Bewegung nach links
5. Prozess beenden

---

# 📦 Modul-System

IZ-Flow unterstützt **erweiterbare Module**, damit Entwickler neue Funktionen hinzufügen können.

Beispiel Modul:

```
# sound.iz
snd{01
```

Verwendung:

```
include sound.iz

syp{L{1
snd{01
wt{05

Z-
```

---

# 📁 Projektstruktur

Empfohlene Ordnerstruktur:

```
IZFlow_Project
│
├── main.iz
│
├── modules
│   ├── sound.iz
│   ├── graphics.iz
│   └── network.iz
│
└── docs
    └── language_spec.md
```

---

# ⚙ Lokales Setup

Du kannst ein Projekt lokal erstellen mit einem einfachen Script.

Windows Batch Beispiel:

```
@echo off
mkdir IZFlow_Project\modules
mkdir IZFlow_Project\programs

echo syp{L{1 > IZFlow_Project\programs\main.iz
```

---

# 🤝 Contributing

IZ-Flow ist ein **Open-Source Projekt**.
Andere Entwickler können neue Ideen und Module beitragen.

Beispiele für Erweiterungen:

* neue Systembefehle
* Grafikmodule
* Netzwerkmodule
* Interpreter Verbesserungen

Bitte:

1. Fork erstellen
2. Modul oder Verbesserung hinzufügen
3. Pull Request senden

---

# 🚀 Zukunft

Geplante Erweiterungen:

* Interpreter für `.iz` Dateien
* grafische Entwicklungsumgebung
* visuelle Flow-Diagramme aus Code
* Plugin-System

---

**Developed by: IZ-FLOW ADMIN**

Status: `L{1}` – System Online
