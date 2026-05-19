# QR Code Generator 🔲

Een professioneel Python-project om QR-codes van URLs te genereren met GitHub Actions automatisering.

## 📁 Structuur

```
qr-code-generator/
├── .github/workflows/          # GitHub Actions
├── src/                        # Python code
├── output/qr_codes/            # Generated QR-codes
├── config.py                   # ⭐ EDIT DEZE
├── main.py                     # Runner
└── requirements.txt            # Dependencies
```

[Zie `STRUCTURE.md` voor details →](./STRUCTURE.md)

## 🚀 Quick Start

### 1. Clone & Setup

```bash
git clone https://github.com/jouw-username/qr-code-generator.git
cd qr-code-generator
pip install -r requirements.txt
```

### 2. Voeg je URLs toe

Edit `config.py`:

```python
URLS = [
    "https://jouw-website.com",
    "https://github.com/jouw-username",
    "https://linkedin.com/in/jij",
]
```

### 3. Voer uit

```bash
python main.py
```

✓ QR-codes verschijnen in `output/qr_codes/`

---

## 📖 Gedetailleerde Handleiding

### Lokaal draaien

```bash
# Setup
pip install -r requirements.txt

# Draaien
python main.py

# QR-codes
ls output/qr_codes/
```

### Config opties

In `config.py`:

```python
# Basis
URLS = ["https://example.com"]

# Custom bestandsnamen
FILENAMES = ["myqr"]

# QR-code grootte
QR_SIZE = 10

# Output folder
OUTPUT_DIR = "output/qr_codes"
```

### GitHub Actions 🤖

GitHub voert het script automatisch uit:

#### Trigger momenten:

- **Bij push naar main** - Wanneer je wijzigingen pusht
- **Dagelijks 09:00 UTC** - Automatisch elke dag
- **Handmatig** - Actions tab → Run workflow

#### Wat doet het:

✓ Installeert dependencies  
✓ Voert script uit  
✓ Genereert QR-codes  
✓ Committed wijzigingen  
✓ Maakt artifacts beschikbaar  

#### Bekijk resultaten:

1. Ga naar **Actions** tab
2. Klik op een workflow run
3. Zie output in logs
4. Download artifacts

### GitHub Actions aanpassen

**Schedule wijzigen** (`.github/workflows/generate_qr.yml`):

```yaml
schedule:
  - cron: '0 12 * * *'  # 12:00 UTC
```

[Cron syntax →](https://crontab.guru/)

**Auto-commit uitschakelen:**

```yaml
- name: Commit and push
  if: false
```

---

## 💻 API Gebruik

```python
from src.qr_generator import create_qr_from_url, create_qr_batch

# Eén QR-code
create_qr_from_url("https://example.com", filename="myqr", size=10)

# Meerdere
urls = ["https://site1.com", "https://site2.com"]
filenames = ["site1", "site2"]
create_qr_batch(urls, filenames)
```

---

## 🛠️ Requirements

- Python 3.7+
- qrcode
- pillow
- GitHub Actions (optioneel, automatisch)

## 📦 Installation

```bash
pip install -r requirements.txt
```

---

## 📋 Workflow bestanden

| File | Doel |
|------|------|
| `generate_qr.yml` | Basis automatisering |
| `advanced_qr.yml` | Met extra features |

---

## ⚙️ Troubleshooting

### ❓ Workflow draait niet?
- Check `.github/workflows/` map bestaat
- Kijk in **Actions** tab voor errors
- Zorg `requirements.txt` correct is

### ❓ Git push mislukt?
- Settings → Actions → Zorg GitHub Actions actief is
- Check `GITHUB_TOKEN` permissions

### ❓ QR-codes niet zichtbaar?
- Check `output/qr_codes/` folder
- Zorg `config.py` URLs bevat

### ❓ Import errors?
```bash
pip install -r requirements.txt
python main.py
```

---

## 📝 LICENSE

MIT

## 🤝 Bijdragen

Issues en PRs welkom!

---

## 📚 Meer info

- [Project Structuur](./STRUCTURE.md)
- [Python qrcode docs](https://github.com/lincolnloop/python-qrcode)
- [GitHub Actions docs](https://docs.github.com/en/actions)
