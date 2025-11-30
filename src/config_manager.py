import yaml
from typing import Dict, Any

class ConfigManager:
    """
    Lädt und verwaltet Steuerparameter aus YAML-Konfiguration.
    """
    def __init__(self, config_path: str):
        self.config_path = config_path
        self.config = self.load_config()

    def load_config(self) -> Dict[str, Any]:
        with open(self.config_path, 'r') as file:
            return yaml.safe_load(file)

    def get_rules(self) -> Dict[str, Any]:
        return self.config.get('validation_rules', {})
