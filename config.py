"""
Configuration file voor QR Code Generator
Voeg hier je URLs toe
"""

# URLs om QR-codes van te maken
URLS = [
    "https://mvdb.wine/pages/feedback-proeverij-jozef-eten-drinken-19-mei",
]

# Optioneel: custom bestandsnamen
# Zet deze op None of verwijder voor auto-naming
FILENAMES = None
# FILENAMES = ["github", "python", "google"]

# QR-code grootte (standaard: 10)
QR_SIZE = 10

# Output directory (relatief naar project root)
OUTPUT_DIR = "output/qr_codes"
