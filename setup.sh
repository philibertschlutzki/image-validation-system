#!/bin/bash

# Setup-Script für Image Validation System
# Dieses Script installiert automatisch alle benötigten Abhängigkeiten

echo "=========================================="
echo "  Image Validation System - Setup"
echo "=========================================="
echo ""

# Farben für Ausgabe
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Prüfe ob Python installiert ist
echo "[1/4] Prüfe Python-Installation..."
if command -v python3 &> /dev/null; then
    PYTHON_CMD=python3
    echo -e "${GREEN}✓ Python 3 gefunden: $(python3 --version)${NC}"
elif command -v python &> /dev/null; then
    PYTHON_CMD=python
    echo -e "${GREEN}✓ Python gefunden: $(python --version)${NC}"
else
    echo -e "${RED}✗ Python ist nicht installiert!${NC}"
    echo "Bitte installiere Python von https://www.python.org/downloads/"
    exit 1
fi

echo ""

# Prüfe ob pip installiert ist
echo "[2/4] Prüfe pip (Paketmanager)..."
if command -v pip3 &> /dev/null; then
    PIP_CMD=pip3
    echo -e "${GREEN}✓ pip3 gefunden${NC}"
elif command -v pip &> /dev/null; then
    PIP_CMD=pip
    echo -e "${GREEN}✓ pip gefunden${NC}"
else
    echo -e "${RED}✗ pip ist nicht installiert!${NC}"
    echo "Installiere pip: $PYTHON_CMD -m ensurepip --upgrade"
    exit 1
fi

echo ""

# Installiere Dependencies
echo "[3/4] Installiere benötigte Pakete..."
echo -e "${YELLOW}Dies kann 1-2 Minuten dauern...${NC}"

if [ -f "requirements.txt" ]; then
    $PIP_CMD install -r requirements.txt
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✓ Alle Pakete erfolgreich installiert${NC}"
    else
        echo -e "${RED}✗ Fehler bei der Installation${NC}"
        exit 1
    fi
else
    echo -e "${RED}✗ requirements.txt nicht gefunden!${NC}"
    exit 1
fi

echo ""

# Erstelle benötigte Ordner
echo "[4/4] Erstelle Verzeichnisstruktur..."
mkdir -p tests/fixtures/test_images
mkdir -p configs
echo -e "${GREEN}✓ Verzeichnisse erstellt${NC}"

echo ""
echo "=========================================="
echo -e "${GREEN}✓ Setup erfolgreich abgeschlossen!${NC}"
echo "=========================================="
echo ""
echo "Nächste Schritte:"
echo "1. Lege ein Testbild ab: tests/fixtures/test_images/test1.jpg"
echo "2. Starte die Analyse: $PYTHON_CMD src/main.py"
echo "3. Führe Tests aus: pytest tests/ -v"
echo ""
echo "Weitere Hilfe: Siehe README.md"
echo ""
