import yaml
from typing import Dict, Any, Tuple

class ValidationEngine:
    """
    Validiert die Analyseergebnisse nach Steuerparametern.
    """
    def __init__(self, config_path: str):
        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)

    def validate(self, analysis_result: Dict[str, Any]) -> Tuple[bool, Dict[str, str]]:
        rules = self.config.get('validation_rules', {})
        report = {}
        valid = True

        for key, params in rules.items():
            value = analysis_result.get(key)
            if value is None:
                report[key] = "Fehlt im Ergebnis."
                valid = False
                continue
            if 'min_value' in params and value < params['min_value']:
                report[key] = f"Wert zu niedrig: {value} < {params['min_value']}"
                valid = False
            if 'max_value' in params and value > params['max_value']:
                report[key] = f"Wert zu hoch: {value} > {params['max_value']}"
                valid = False
            if key == 'dominant_color_ratio' and value < params.get('dominant_color_threshold', 0):
                report[key] = f"Dominante Farbe zu schwach: {value}" 
                valid = False
            # Erweiterbar mit weiteren Logiken (Objekterkennung etc.)
        if valid:
            report['status'] = 'Validierung bestanden.'
        else:
            report['status'] = 'Validierung fehlgeschlagen.'
        return valid, report
