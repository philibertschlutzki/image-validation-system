"""Hauptausführungsskript für Bildvalidierung.

Dieses Skript demonstriert die End-to-End-Ausführung:
1. Bildanalyse mit konfigurierbaren Parametern
2. Validierung gegen definierte Schwellwerte
3. Detaillierte Berichtserstellung

Verwendung:
    python src/main.py
"""

import sys
import os

# Füge Projektroot zum Python-Pfad hinzu
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.image_analyzer import ImageAnalyzer
from src.validation_engine import ValidationEngine
from src.result_reporter import ResultReporter


def main():
    """Hauptfunktion zur Ausführung der Bildvalidierung."""
    # Konfigurationspfade relativ zum Projektroot
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    config_path = os.path.join(base_dir, "configs", "default_rules.yaml")
    image_path = os.path.join(base_dir, "tests", "fixtures", "test_images", "test1.jpg")

    # Prüfe ob Testbild existiert, sonst Hinweis
    if not os.path.exists(image_path):
        print(f"HINWEIS: Testbild nicht gefunden: {image_path}")
        print("Bitte legen Sie ein Testbild unter tests/fixtures/test_images/test1.jpg ab.")
        return

    # Initialisiere Komponenten
    print("=" * 60)
    print("IMAGE VALIDATION SYSTEM")
    print("=" * 60)
    print(f"Konfiguration: {config_path}")
    print(f"Bild: {image_path}")
    print("\n[1/3] Bildanalyse wird durchgeführt...")
    
    analyzer = ImageAnalyzer(config_path)
    results = analyzer.analyze_image(image_path)
    print("✓ Bildanalyse abgeschlossen")
    
    print("\n[2/3] Validierung gegen Steuerparameter...")
    validator = ValidationEngine(config_path)
    is_valid, report = validator.validate(results)
    print("✓ Validierung abgeschlossen")
    
    print("\n[3/3] Bericht wird erstellt...")
    print("=" * 60)
    reporter = ResultReporter()
    reporter.generate_report(results, is_valid, report)
    print("=" * 60)


if __name__ == "__main__":
    main()
