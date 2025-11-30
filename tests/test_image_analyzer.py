"""Unit-Tests für ImageAnalyzer Modul.

Testet die Bildanalysefunktionen:
- Helligkeitsmessung
- Schärfeberechnung (Laplacian-Varianz)
- Farbverteilungsanalyse (K-Means Clustering)
- Robustheit gegen fehlerhafte Eingaben
"""

import os
import sys
import pytest
import numpy as np
from PIL import Image

# Füge Projektroot zum Python-Pfad hinzu
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.image_analyzer import ImageAnalyzer

# Pfade relativ zum Projektroot
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
TEST_IMAGE_PATH = os.path.join(BASE_DIR, "tests", "fixtures", "test_images", "test1.jpg")
CONFIG_PATH = os.path.join(BASE_DIR, "configs", "default_rules.yaml")


@pytest.fixture
def sample_image():
    """Erstellt ein temporäres Testbild falls keines existiert."""
    if not os.path.exists(TEST_IMAGE_PATH):
        os.makedirs(os.path.dirname(TEST_IMAGE_PATH), exist_ok=True)
        # Erstelle einfaches RGB-Bild (256x256)
        img = Image.new('RGB', (256, 256), color=(128, 128, 128))
        img.save(TEST_IMAGE_PATH)
    return TEST_IMAGE_PATH


def test_analyze_image_basic(sample_image):
    """Test: Grundlegende Bildanalyse liefert alle erwarteten Metriken."""
    analyzer = ImageAnalyzer(CONFIG_PATH)
    result = analyzer.analyze_image(sample_image)
    
    # Prüfe ob alle erwarteten Keys vorhanden sind
    assert 'brightness' in result, "Helligkeit fehlt in Analyseergebnis"
    assert 'sharpness' in result, "Schärfe fehlt in Analyseergebnis"
    assert 'dominant_color' in result, "Dominante Farbe fehlt in Analyseergebnis"
    assert 'dominant_color_ratio' in result, "Farbverteilungsratio fehlt in Analyseergebnis"
    assert 'object_detection' in result, "Objekterkennung fehlt in Analyseergebnis"


def test_brightness_range(sample_image):
    """Test: Helligkeit liegt im gültigen Bereich [0, 255]."""
    analyzer = ImageAnalyzer(CONFIG_PATH)
    result = analyzer.analyze_image(sample_image)
    
    brightness = result['brightness']
    assert 0 <= brightness <= 255, f"Helligkeit außerhalb des gültigen Bereichs: {brightness}"


def test_sharpness_positive(sample_image):
    """Test: Schärfewert ist nicht-negativ."""
    analyzer = ImageAnalyzer(CONFIG_PATH)
    result = analyzer.analyze_image(sample_image)
    
    sharpness = result['sharpness']
    assert sharpness >= 0, f"Schärfewert ist negativ: {sharpness}"


def test_dominant_color_format(sample_image):
    """Test: Dominante Farbe ist Liste mit 3 Werten im Bereich [0, 1]."""
    analyzer = ImageAnalyzer(CONFIG_PATH)
    result = analyzer.analyze_image(sample_image)
    
    dominant_color = result['dominant_color']
    assert isinstance(dominant_color, list), "Dominante Farbe ist keine Liste"
    assert len(dominant_color) == 3, f"Dominante Farbe hat nicht 3 Komponenten: {len(dominant_color)}"
    
    for val in dominant_color:
        assert 0 <= val <= 1, f"Farbwert außerhalb [0, 1]: {val}"


def test_invalid_image_path():
    """Test: Fehlerbehandlung bei ungültigem Bildpfad."""
    analyzer = ImageAnalyzer(CONFIG_PATH)
    
    with pytest.raises(ValueError, match="Ungültiges Bild"):
        analyzer.analyze_image("non_existent_image.jpg")


def test_color_ratio_range(sample_image):
    """Test: Farbverteilungsratio liegt im Bereich [0, 1]."""
    analyzer = ImageAnalyzer(CONFIG_PATH)
    result = analyzer.analyze_image(sample_image)
    
    ratio = result['dominant_color_ratio']
    assert 0 <= ratio <= 1, f"Farbverteilungsratio außerhalb [0, 1]: {ratio}"
