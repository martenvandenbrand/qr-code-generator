"""
QR Code Generator Package
"""

from .qr_generator import create_qr_from_url, create_qr_batch

__version__ = "1.0.0"
__author__ = "QR Code Generator"

__all__ = ["create_qr_from_url", "create_qr_batch"]
