# 🔍 AutoPriceTracker

**AutoPriceTracker** is a Python CLI application that tracks prices of products from e-commerce websites (like Amazon, Walmart, etc.) and alerts users when prices drop below a target value.

---

## 🚀 Features

- ✅ Track product prices from given URLs
- ✅ Store historical price data (JSON/CSV)
- ✅ Notify user if price falls below a threshold
- ✅ Mockable and testable components
- ✅ Auto CI testing pipeline with GitHub Actions

---

## 🛠️ Stack

- Python 3.11+
- `requests`, `beautifulsoup4` for web scraping
- `pytest`, `pytest-mock` for testing
- GitHub Actions for CI
- `black`, `flake8`, `mypy` for linting and type checking

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/autopricetracker.git
cd autopricetracker
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

---

## 🧪 Running Tests

```bash
pytest
```

---

## 📈 Example Usage

```bash
python main.py --url https://www.amazon.com/dp/B08N5WRWNW --target-price 200
```

---
