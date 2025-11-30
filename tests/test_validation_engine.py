import pytest
from src.image_analyzer import ImageAnalyzer
from src.validation_engine import ValidationEngine

TEST_IMAGE_PATH = "tests/fixtures/test_images/test1.jpg"
CONFIG_PATH = "configs/default_rules.yaml"

def test_validation_engine_pass():
    analyzer = ImageAnalyzer(CONFIG_PATH)
    validator = ValidationEngine(CONFIG_PATH)
    result = analyzer.analyze_image(TEST_IMAGE_PATH)
    valid, report = validator.validate(result)
    assert isinstance(valid, bool)
    assert 'status' in report
