"""Unit-Tests für ValidationEngine Modul.

Testet die Validierungslogik:
- Schwellwertprüfungen (min/max)
- Regelbasierte Validierung
- Fehlerberichterstattung
- Integration mit ImageAnalyzer
"""

import os
import sys
import pytest
from PIL import Image

# Füge Projektroot zum Python-Pfad hinzu
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.image_analyzer import ImageAnalyzer
from src.validation_engine import ValidationEngine

# Pfade relativ zum Projektroot
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
TEST_IMAGE_PATH = os.path.join(BASE_DIR, "tests", "fixtures", "test_images", "test1.jpg")
CONFIG_PATH = os.path.join(BASE_DIR, "configs", "default_rules.yaml")


@pytest.fixture
def sample_image():
    """Erstellt ein temporäres Testbild falls keines existiert."""
    if not os.path.exists(TEST_IMAGE_PATH):
        os.makedirs(os.path.dirname(TEST_IMAGE_PATH), exist_ok=True)
        # Erstelle Bild mit mittlerer Helligkeit
        img = Image.new('RGB', (256, 256), color=(128, 128, 128))
        img.save(TEST_IMAGE_PATH)
    return TEST_IMAGE_PATH


def test_validation_engine_returns_tuple(sample_image):
    """Test: ValidationEngine gibt Tupel (bool, dict) zurück."""
    analyzer = ImageAnalyzer(CONFIG_PATH)
    validator = ValidationEngine(CONFIG_PATH)
    
    result = analyzer.analyze_image(sample_image)
    valid, report = validator.validate(result)
    
    assert isinstance(valid, bool), "Validierungsergebnis ist kein Boolean"
    assert isinstance(report, dict), "Bericht ist kein Dictionary"
    assert 'status' in report, "Statusfeld fehlt im Bericht"


def test_validation_with_mock_data():
    """Test: Validierung mit Mock-Daten (sollte bestehen)."""
    validator = ValidationEngine(CONFIG_PATH)
    
    # Mock-Daten die alle Regeln erfüllen
    mock_result = {
        'brightness': 120,  # Zwischen 50 und 200
        'sharpness': 150.0,  # Über 100
        'dominant_color_ratio': 0.35  # Über 0.2
    }
    
    valid, report = validator.validate(mock_result)
    assert valid is True, f"Validierung sollte bestehen, Report: {report}"
    assert report['status'] == 'Validierung bestanden.'


def test_validation_brightness_too_low():
    """Test: Validierung schlägt fehl bei zu niedriger Helligkeit."""
    validator = ValidationEngine(CONFIG_PATH)
    
    mock_result = {
        'brightness': 30,  # Unter 50 (min_value)
        'sharpness': 150.0,
        'dominant_color_ratio': 0.35
    }
    
    valid, report = validator.validate(mock_result)
    assert valid is False, "Validierung sollte fehlschlagen"
    assert 'brightness' in report, "Helligkeitsfehler fehlt im Bericht"
    assert 'zu niedrig' in report['brightness'], "Fehlermeldung nicht korrekt"


def test_validation_brightness_too_high():
    """Test: Validierung schlägt fehl bei zu hoher Helligkeit."""
    validator = ValidationEngine(CONFIG_PATH)
    
    mock_result = {
        'brightness': 250,  # Über 200 (max_value)
        'sharpness': 150.0,
        'dominant_color_ratio': 0.35
    }
    
    valid, report = validator.validate(mock_result)
    assert valid is False, "Validierung sollte fehlschlagen"
    assert 'brightness' in report, "Helligkeitsfehler fehlt im Bericht"
    assert 'zu hoch' in report['brightness'], "Fehlermeldung nicht korrekt"


def test_validation_sharpness_too_low():
    """Test: Validierung schlägt fehl bei zu niedriger Schärfe."""
    validator = ValidationEngine(CONFIG_PATH)
    
    mock_result = {
        'brightness': 120,
        'sharpness': 50.0,  # Unter 100 (min_value)
        'dominant_color_ratio': 0.35
    }
    
    valid, report = validator.validate(mock_result)
    assert valid is False, "Validierung sollte fehlschlagen"
    assert 'sharpness' in report, "Schärfefehler fehlt im Bericht"


def test_validation_missing_field():
    """Test: Validierung behandelt fehlende Felder korrekt."""
    validator = ValidationEngine(CONFIG_PATH)
    
    # Unvollständige Daten
    mock_result = {
        'brightness': 120
        # sharpness fehlt
    }
    
    valid, report = validator.validate(mock_result)
    assert valid is False, "Validierung sollte fehlschlagen bei fehlenden Feldern"
    assert 'sharpness' in report, "Fehler für fehlendes Feld nicht im Bericht"


def test_validation_multiple_failures():
    """Test: Validierung erkennt mehrere Regelverletzungen."""
    validator = ValidationEngine(CONFIG_PATH)
    
    mock_result = {
        'brightness': 20,  # Zu niedrig
        'sharpness': 30.0,  # Zu niedrig
        'dominant_color_ratio': 0.1  # Zu niedrig
    }
    
    valid, report = validator.validate(mock_result)
    assert valid is False, "Validierung sollte fehlschlagen"
    
    # Prüfe dass mehrere Fehler erkannt wurden
    error_count = sum(1 for key in report if key != 'status')
    assert error_count >= 2, f"Nicht alle Fehler erkannt, Report: {report}"
