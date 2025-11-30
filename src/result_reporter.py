from typing import Dict, Any

class ResultReporter:
    """
    Erstellt Protokolle und Ausgaben der Analysemodelle.
    """
    def generate_report(self, results: Dict[str, Any], is_valid: bool, report: Dict[str, str]):
        print("Analyseergebnisse:")
        for key, value in results.items():
            print(f"  {key}: {value}")
        print("\nValidierungsreport:")
        for key, msg in report.items():
            print(f"  {key}: {msg}")
        print(f"Gesamtstatus: {'OK' if is_valid else 'FEHLER'}")
