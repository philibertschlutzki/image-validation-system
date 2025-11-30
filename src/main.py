from src.image_analyzer import ImageAnalyzer
from src.validation_engine import ValidationEngine
from src.result_reporter import ResultReporter

if __name__ == "__main__":
    CONFIG_PATH = "configs/default_rules.yaml"
    IMAGE_PATH = "tests/fixtures/test_images/test1.jpg"

    analyzer = ImageAnalyzer(CONFIG_PATH)
    results = analyzer.analyze_image(IMAGE_PATH)
    validator = ValidationEngine(CONFIG_PATH)
    is_valid, report = validator.validate(results)
    reporter = ResultReporter()
    reporter.generate_report(results, is_valid, report)
