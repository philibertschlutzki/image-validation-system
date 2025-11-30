# Image Validation System

Konfigurierbare Bildinterpretation mit Validierung - Parametrisiertes System zur Bildanalyse

## Übersicht

Dieses System analysiert Bilder anhand konfigurierbarer Steuerparameter und validiert die Ergebnisse gegen definierte Schwellwerte. Es ist vollständig für GitHub Codespaces optimiert und beinhaltet umfassende Tests.

## Features

- **Bildanalyse**: Helligkeits-, Schärfe- und Farbverteilungsmessung
- **Konfigurierbare Validierung**: YAML-basierte Regelkonfiguration
- **Umfassende Tests**: pytest-basierte Unit- und Integrationstests
- **GitHub Codespaces Ready**: Vorkonfigurierte Entwicklungsumgebung

## Installation

### In GitHub Codespaces (empfohlen)

1. Öffne das Repository in GitHub
2. Klicke auf "Code" → "Codespaces" → "Create codespace on develop"
3. Warte bis die Umgebung geladen ist (Dependencies werden automatisch installiert)

### Lokal

```bash
git clone https://github.com/philibertschlutzki/image-validation-system.git
cd image-validation-system
pip install -r requirements.txt
```

## Verwendung

### Bildvalidierung ausführen

```bash
python src/main.py
```

### Tests ausführen

```bash
# Alle Tests
pytest

# Mit Coverage-Report
pytest --cov=src tests/

# Einzelne Testdatei
pytest tests/test_image_analyzer.py -v
```

## Projektstruktur

```
image-validation-system/
├── .devcontainer/          # Codespaces-Konfiguration
│   └── devcontainer.json
├── src/                    # Hauptmodule
│   ├── __init__.py
│   ├── image_analyzer.py   # Bildanalyse-Engine
│   ├── validation_engine.py # Validierungslogik
│   ├── config_manager.py   # Konfigurationsverwaltung
│   ├── result_reporter.py  # Berichtserstellung
│   └── main.py            # Hauptausführung
├── tests/                  # Testsuiten
│   ├── __init__.py
│   ├── test_image_analyzer.py
│   ├── test_validation_engine.py
│   ├── test_config_manager.py
│   └── fixtures/          # Testdaten
│       └── test_images/
├── configs/               # Konfigurationsdateien
│   └── default_rules.yaml
├── requirements.txt
└── README.md
```

## Konfiguration

Passe die Validierungsregeln in `configs/default_rules.yaml` an:

```yaml
validation_rules:
  brightness:
    min_value: 50      # Minimale Helligkeit (0-255)
    max_value: 200     # Maximale Helligkeit (0-255)
  sharpness:
    min_value: 100.0   # Minimale Schärfe (Laplacian-Varianz)
  dominant_color_ratio:
    dominant_color_threshold: 0.2  # Min. Anteil dominanter Farbe
```

## Testbild hinzufügen

Lege ein Testbild unter folgendem Pfad ab:
```
tests/fixtures/test_images/test1.jpg
```

## Erweiterungsmöglichkeiten

- **Objekterkennung**: Integration von YOLO/Faster R-CNN
- **Weitere Metriken**: Rauschen, Kompression, Artefakte
- **Batch-Verarbeitung**: Multiple Bilder parallel analysieren
- **API-Endpunkt**: Flask/FastAPI-Integration

## Lizenz

MIT
