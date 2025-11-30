from src.config_manager import ConfigManager

CONFIG_PATH = "configs/default_rules.yaml"

def test_load_config():
    manager = ConfigManager(CONFIG_PATH)
    rules = manager.get_rules()
    assert 'brightness' in rules
    assert 'sharpness' in rules
