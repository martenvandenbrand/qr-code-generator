"""
Configuration file voor QR Code Generator
Voeg hier je URLs toe
"""

# URLs om QR-codes van te maken
URLS = [
    "https://github.com",
    "https://www.python.org",
    "https://www.google.com",
]

# Optioneel: custom bestandsnamen
# Zet deze op None of verwijder voor auto-naming
FILENAMES = None
# FILENAMES = ["github", "python", "google"]

# QR-code grootte (standaard: 10)
QR_SIZE = 10

# Output directory (relatief naar project root)
OUTPUT_DIR = "output/qr_codes"
