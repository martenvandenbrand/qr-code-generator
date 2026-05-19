#!/usr/bin/env python3
"""
QR Code Generator from URLs
Genereert QR-codes van URLs en slaat ze op als afbeeldingen.
"""

import qrcode
from pathlib import Path
from typing import List, Optional


def create_qr_from_url(url: str, filename: Optional[str] = None, size: int = 10) -> str:
    """
    Maakt een QR-code van een URL
    
    Args:
        url: De URL om in QR-code om te zetten
        filename: Naam van het outputbestand (zonder .png). Default: gebaseerd op URL
        size: Grootte van de QR-code (standaard: 10)
    
    Returns:
        Pad naar de gegenereerde QR-code
    """
    
    # Output directory aanmaken
    output_dir = Path(__file__).parent.parent / "output" / "qr_codes"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Filename bepalen
    if filename is None:
        filename = url.replace("https://", "").replace("http://", "").replace("/", "_").replace(".", "_")[:30]
    
    output_path = output_dir / f"{filename}.png"
    
    # QR-code genereren
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=size,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    # Afbeelding maken
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_path)
    
    print(f"✓ QR-code gemaakt: {output_path}")
    return str(output_path)


def create_qr_batch(urls: List[str], filenames: Optional[List[str]] = None) -> List[str]:
    """
    Maakt meerdere QR-codes van een lijst met URLs
    
    Args:
        urls: Lijst met URLs
        filenames: Optionele lijst met bestandsnamen
    
    Returns:
        Lijst met paden naar gegenereerde QR-codes
    """
    
    results = []
    
    for i, url in enumerate(urls):
        filename = filenames[i] if filenames and i < len(filenames) else None
        try:
            path = create_qr_from_url(url, filename)
            results.append(path)
        except Exception as e:
            print(f"✗ Fout bij {url}: {e}")
    
    return results
