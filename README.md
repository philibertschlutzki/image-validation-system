# 🖼️ Image Validation System

**Automatische Bildqualitätsprüfung** - Analysiert Bilder und prüft sie gegen konfigurierbare Qualitätskriterien.

---

## 📋 Was macht dieses Tool?

Dieses Tool überprüft automatisch, ob Bilder bestimmte Qualitätsstandards erfüllen:
- ✅ **Helligkeit**: Ist das Bild zu dunkel oder zu hell?
- ✅ **Schärfe**: Ist das Bild scharf genug?
- ✅ **Farbverteilung**: Sind die Farben ausgewogen?

Du legst die Regeln fest - das System prüft automatisch!

---

## 🚀 Schnellstart (für Anfänger)

### Option 1: GitHub Codespaces (Empfohlen - kein Setup nötig!)

**Was ist Codespaces?** Ein Online-Computer direkt im Browser - keine Installation nötig!

#### Schritt-für-Schritt:

1. **Gehe zum Repository**: [https://github.com/philibertschlutzki/image-validation-system](https://github.com/philibertschlutzki/image-validation-system)

2. **Klicke auf den grünen "Code" Button** (oben rechts)

3. **Wähle "Codespaces" Tab** → Klicke auf **"Create codespace on main"**

4. **Warte 2-3 Minuten** - Ein Online-Editor öffnet sich automatisch

5. **Installiere die Software** (nur beim ersten Mal):
   ```bash
   bash setup.sh
   ```
   Kopiere diese Zeile, füge sie unten im Terminal ein und drücke Enter.

6. **Lade dein Testbild hoch**:
   - Klicke links auf den Ordner `tests/fixtures/test_images/`
   - Rechtsklick → "Upload" → Wähle dein Bild (benenne es `test1.jpg`)

7. **Starte die Analyse**:
   ```bash
   python src/main.py
   ```
   Kopiere diese Zeile ins Terminal und drücke Enter.

8. **Fertig!** 🎉 Du siehst jetzt die Analyseergebnisse!

---

### Option 2: Auf deinem Computer (für Fortgeschrittene)

#### Voraussetzungen
- Python 3.8 oder neuer installiert ([Download hier](https://www.python.org/downloads/))
- Git installiert ([Download hier](https://git-scm.com/downloads))

#### Installation

1. **Terminal/Kommandozeile öffnen**:
   - **Windows**: Drücke `Win + R`, tippe `cmd`, drücke Enter
   - **Mac**: Drücke `Cmd + Leertaste`, tippe `Terminal`, drücke Enter
   - **Linux**: Drücke `Ctrl + Alt + T`

2. **Projekt herunterladen**:
   ```bash
   git clone https://github.com/philibertschlutzki/image-validation-system.git
   cd image-validation-system
   ```

3. **Software installieren**:
   ```bash
   bash setup.sh
   ```
   Oder manuell:
   ```bash
   pip install -r requirements.txt
   ```

4. **Testbild hinzufügen**:
   - Lege ein Bild in den Ordner: `tests/fixtures/test_images/`
   - Benenne es: `test1.jpg`

5. **Analyse starten**:
   ```bash
   python src/main.py
   ```

---

## 📊 Ergebnisse verstehen

Nach der Analyse siehst du einen Bericht wie diesen:

```
============================================================
IMAGE VALIDATION SYSTEM
============================================================
Konfiguration: configs/default_rules.yaml
Bild: tests/fixtures/test_images/test1.jpg

[1/3] Bildanalyse wird durchgeführt...
✓ Bildanalyse abgeschlossen

[2/3] Validierung gegen Steuerparameter...
✓ Validierung abgeschlossen

[3/3] Bericht wird erstellt...
============================================================
Analyseergebnisse:
  brightness: 128.5          ← Helligkeit (0=schwarz, 255=weiß)
  sharpness: 245.8           ← Schärfe (höher = schärfer)
  dominant_color: [0.6, 0.4, 0.3]  ← Hauptfarbe (RGB)
  dominant_color_ratio: 0.35 ← Anteil der Hauptfarbe

Validierungsreport:
  status: Validierung bestanden.  ← ✅ ALLES OK!

Gesamtstatus: OK
============================================================
```

### Was bedeuten die Werte?

- **brightness** (Helligkeit): 0 = komplett schwarz, 255 = komplett weiß
  - Standard: 50-200 ist OK
  
- **sharpness** (Schärfe): Je höher, desto schärfer
  - Standard: Mindestens 100 ist OK
  
- **dominant_color_ratio**: Wie dominant ist die Hauptfarbe?
  - 0.2 = 20% des Bildes hat diese Farbe
  - Standard: Mindestens 0.2 (20%) ist OK

---

## ⚙️ Einstellungen anpassen

Du kannst die Qualitätskriterien selbst festlegen!

### Schritt-für-Schritt:

1. **Öffne die Konfigurationsdatei**: `configs/default_rules.yaml`

2. **Passe die Werte an**:

```yaml
validation_rules:
  brightness:                    # Helligkeit
    min_value: 50               # ← Minimale Helligkeit (ändere auf z.B. 30)
    max_value: 200              # ← Maximale Helligkeit (ändere auf z.B. 220)
  
  sharpness:                     # Schärfe
    min_value: 100.0            # ← Minimale Schärfe (ändere auf z.B. 150.0)
  
  dominant_color_ratio:          # Farbverteilung
    dominant_color_threshold: 0.2  # ← Min. Anteil (ändere auf z.B. 0.3)
```

3. **Speichern** und erneut `python src/main.py` ausführen

---

## 🧪 Tests ausführen (Optional)

Möchtest du prüfen, ob alles korrekt funktioniert?

```bash
# Alle Tests ausführen
pytest tests/ -v

# Detaillierter Bericht mit Coverage
pytest --cov=src tests/
```

**Was sind Tests?** Automatische Prüfungen, die sicherstellen, dass der Code richtig funktioniert.

---

## 📁 Projektstruktur erklärt

```
image-validation-system/
├── src/                      ← Hauptprogramm (hier liegt die Logik)
│   ├── image_analyzer.py     ← Analysiert Bilder
│   ├── validation_engine.py  ← Prüft gegen Regeln
│   ├── config_manager.py     ← Lädt Einstellungen
│   ├── result_reporter.py    ← Erstellt Berichte
│   └── main.py              ← STARTE HIER!
│
├── tests/                    ← Testdateien (zum Prüfen)
│   └── fixtures/
│       └── test_images/      ← LEGE HIER DEINE BILDER AB!
│
├── configs/                  ← Einstellungen
│   └── default_rules.yaml    ← PASSE HIER REGELN AN!
│
├── requirements.txt          ← Liste benötigter Software
└── setup.sh                 ← Automatisches Installations-Script
```

---

## 🆘 Häufige Probleme

### Problem: `ModuleNotFoundError: No module named 'cv2'`

**Lösung**: Software wurde nicht installiert.
```bash
pip install -r requirements.txt
```

### Problem: `FileNotFoundError: tests/fixtures/test_images/test1.jpg`

**Lösung**: Kein Testbild vorhanden.
1. Erstelle den Ordner: `tests/fixtures/test_images/`
2. Lege ein Bild dort ab und benenne es `test1.jpg`

### Problem: `python: command not found`

**Lösung**: Python ist nicht installiert.
- Lade Python herunter: [python.org/downloads](https://www.python.org/downloads/)
- Wähle bei Installation: "Add Python to PATH" ✅

### Problem: Tests schlagen fehl

**Lösung**: Testbild wird automatisch erstellt, aber:
```bash
# Lösche alte Test-Caches
find . -type d -name "__pycache__" -exec rm -r {} +
find . -type d -name ".pytest_cache" -exec rm -r {} +

# Tests neu ausführen
pytest tests/ -v
```

---

## 🔧 Erweiterte Nutzung

### Eigenes Bild analysieren

```python
from src.image_analyzer import ImageAnalyzer
from src.validation_engine import ValidationEngine
from src.result_reporter import ResultReporter

# Pfad zu deinem Bild
image_path = "pfad/zu/deinem/bild.jpg"

# Analysiere
analyzer = ImageAnalyzer("configs/default_rules.yaml")
results = analyzer.analyze_image(image_path)

# Validiere
validator = ValidationEngine("configs/default_rules.yaml")
is_valid, report = validator.validate(results)

# Zeige Ergebnisse
reporter = ResultReporter()
reporter.generate_report(results, is_valid, report)
```

### Mehrere Bilder auf einmal

```python
import os
from src.image_analyzer import ImageAnalyzer
from src.validation_engine import ValidationEngine

analyzer = ImageAnalyzer("configs/default_rules.yaml")
validator = ValidationEngine("configs/default_rules.yaml")

# Alle JPG-Bilder im Ordner
image_folder = "tests/fixtures/test_images/"
for filename in os.listdir(image_folder):
    if filename.endswith(".jpg"):
        image_path = os.path.join(image_folder, filename)
        print(f"\nAnalysiere: {filename}")
        results = analyzer.analyze_image(image_path)
        is_valid, report = validator.validate(results)
        print(f"Status: {'✅ OK' if is_valid else '❌ FEHLER'}")
```

---

## 💡 Zukünftige Erweiterungen

- 🤖 **Objekterkennung**: Erkenne Personen, Autos, Tiere im Bild
- 📊 **Batch-Verarbeitung**: Analysiere hunderte Bilder auf einmal
- 🌐 **Web-Interface**: Bilder per Drag & Drop hochladen
- 📧 **E-Mail-Benachrichtigung**: Automatische Berichte per E-Mail

---

## 📞 Hilfe & Support

**Fragen?** Erstelle ein Issue auf GitHub:
[https://github.com/philibertschlutzki/image-validation-system/issues](https://github.com/philibertschlutzki/image-validation-system/issues)

---

## 📄 Lizenz

MIT License - Du darfst den Code frei verwenden und anpassen!
