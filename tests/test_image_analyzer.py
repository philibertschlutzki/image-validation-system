import os
import pytest
from src.image_analyzer import ImageAnalyzer

TEST_IMAGE_PATH = "tests/fixtures/test_images/test1.jpg"
CONFIG_PATH = "configs/default_rules.yaml"

def test_analyze_image_basic():
    analyzer = ImageAnalyzer(CONFIG_PATH)
    result = analyzer.analyze_image(TEST_IMAGE_PATH)
    assert 'brightness' in result
    assert 'sharpness' in result
    assert 'dominant_color' in result
    assert 'dominant_color_ratio' in result
