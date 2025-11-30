"""Unit-Tests für ConfigManager Modul.

Testet die Konfigurationsverwaltung:
- Laden von YAML-Dateien
- Zugriff auf Validierungsregeln
- Fehlerbehandlung bei ungültigen Configs
"""

import os
import sys
import pytest
import yaml

# Füge Projektroot zum Python-Pfad hinzu
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.config_manager import ConfigManager

# Pfade relativ zum Projektroot
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
CONFIG_PATH = os.path.join(BASE_DIR, "configs", "default_rules.yaml")


def test_load_config():
    """Test: Konfiguration wird erfolgreich geladen."""
    manager = ConfigManager(CONFIG_PATH)
    rules = manager.get_rules()
    
    assert isinstance(rules, dict), "Geladene Regeln sind kein Dictionary"
    assert 'brightness' in rules, "Helligkeitsregel fehlt in Konfiguration"
    assert 'sharpness' in rules, "Schärferegel fehlt in Konfiguration"


def test_config_structure():
    """Test: Konfigurationsstruktur ist korrekt."""
    manager = ConfigManager(CONFIG_PATH)
    rules = manager.get_rules()
    
    # Prüfe Helligkeitsregel
    assert 'min_value' in rules['brightness'], "min_value fehlt in brightness-Regel"
    assert 'max_value' in rules['brightness'], "max_value fehlt in brightness-Regel"
    
    # Prüfe Schärferegel
    assert 'min_value' in rules['sharpness'], "min_value fehlt in sharpness-Regel"


def test_config_value_types():
    """Test: Konfigurationswerte haben korrekte Typen."""
    manager = ConfigManager(CONFIG_PATH)
    rules = manager.get_rules()
    
    # Helligkeit sollte numerische Werte haben
    assert isinstance(rules['brightness']['min_value'], (int, float)), \
        "brightness min_value ist nicht numerisch"
    assert isinstance(rules['brightness']['max_value'], (int, float)), \
        "brightness max_value ist nicht numerisch"
    
    # Schärfe sollte numerischen min_value haben
    assert isinstance(rules['sharpness']['min_value'], (int, float)), \
        "sharpness min_value ist nicht numerisch"


def test_config_value_ranges():
    """Test: Konfigurationswerte liegen in sinnvollen Bereichen."""
    manager = ConfigManager(CONFIG_PATH)
    rules = manager.get_rules()
    
    # Helligkeit: min sollte kleiner als max sein
    assert rules['brightness']['min_value'] < rules['brightness']['max_value'], \
        "Helligkeits-min_value ist nicht kleiner als max_value"
    
    # Helligkeit: Werte sollten im Bereich [0, 255] liegen
    assert 0 <= rules['brightness']['min_value'] <= 255, \
        "brightness min_value außerhalb [0, 255]"
    assert 0 <= rules['brightness']['max_value'] <= 255, \
        "brightness max_value außerhalb [0, 255]"


def test_missing_config_file():
    """Test: Fehlerbehandlung bei fehlender Konfigurationsdatei."""
    with pytest.raises(FileNotFoundError):
        ConfigManager("non_existent_config.yaml")


def test_config_reload():
    """Test: Konfiguration kann neu geladen werden."""
    manager = ConfigManager(CONFIG_PATH)
    rules1 = manager.get_rules()
    
    # Lade erneut
    config2 = manager.load_config()
    
    # Sollten identisch sein
    assert rules1 == config2['validation_rules'], \
        "Erneutes Laden liefert unterschiedliche Werte"
