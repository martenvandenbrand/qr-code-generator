#!/usr/bin/env python3
"""
Main entry point voor QR Code Generator
Laadt URLs uit config en genereert QR-codes
"""

import sys
from pathlib import Path
from datetime import datetime

# Voeg src folder toe aan Python path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from qr_generator import create_qr_batch

# Importeer URLs uit config
from config import URLS


def main():
    """Main function"""
    print("=" * 50)
    print("QR Code Generator")
    print("=" * 50)
    print(f"Gestart op: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    if not URLS:
        print("⚠ Geen URLs gevonden in config.py")
        print("Voeg URLs toe aan config.py")
        return 1
    
    print(f"URLs om te verwerken: {len(URLS)}\n")
    
    try:
        results = create_qr_batch(URLS)
        
        print(f"\n{'=' * 50}")
        print(f"✓ Succes! {len(results)} QR-codes gemaakt")
        print(f"Location: output/qr_codes/")
        print("=" * 50)
        return 0
        
    except Exception as e:
        print(f"\n✗ Fout opgetreden: {e}")
        print("=" * 50)
        return 1


if __name__ == "__main__":
    sys.exit(main())
