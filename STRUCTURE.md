# Project Structuur

```
qr-code-generator/
│
├── .github/
│   └── workflows/
│       ├── generate_qr.yml          # Basis GitHub Actions workflow
│       └── advanced_qr.yml          # Geavanceerde workflow
│
├── src/
│   ├── __init__.py                  # Python package
│   └── qr_generator.py              # Core generator functions
│
├── output/                          # Output folder (gegenereerd)
│   └── qr_codes/                    # QR-code bestanden
│       ├── github.png
│       ├── python.png
│       └── ...
│
├── .gitignore                       # Git configuratie
├── config.py                        # EDIT DEZE: URLs en instellingen
├── main.py                          # Entry point / runner
├── requirements.txt                 # Python dependencies
└── README.md                        # Documentatie
```

## Folder Beschrijving

| Folder | Doel |
|--------|------|
| `.github/workflows/` | GitHub Actions automation scripts |
| `src/` | Python source code (core logic) |
| `output/qr_codes/` | Gegenereerde QR-code bestanden |
| Root | Config, entry point, requirements |

## Workflow

```
1. Edit config.py met je URLs
2. Run: python main.py
3. QR-codes verschijnen in output/qr_codes/
4. Push naar GitHub → Actions draait automatisch
```

## Quick Reference

- **URLs wijzigen:** Edit `config.py`
- **Script draaien:** `python main.py`
- **Output locatie:** `output/qr_codes/`
- **GitHub automation:** `.github/workflows/generate_qr.yml`

## Voordelen van deze structuur

✅ **Schoon & professioneel**  
✅ **Makkelijk uit te breiden**  
✅ **Duidelijke scheiding van concerns**  
✅ **GitHub Actions-friendly**  
✅ **Configuratie gescheiden van code**
