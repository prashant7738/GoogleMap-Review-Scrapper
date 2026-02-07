# Google Map Review Scraper

A Python web scraper to extract hotel reviews from Google Maps using Playwright.

## Setup

1. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Playwright browsers:**
   ```bash
   playwright install chromium
   ```

## Usage

Run the scraper:
```bash
python main.py
```

The scraped data will be saved to CSV files.

## Project Structure

- `main.py` - Main scraper script
- `requirements.txt` - Python dependencies
- `venv/` - Virtual environment (not tracked in Git)
- `User/` - Chrome user data (not tracked in Git)
- `*.csv` - Output CSV files with scraped reviews

## Notes

- The `venv/` and `User/` directories are excluded from Git to keep the repository clean
- Make sure to create your own virtual environment when setting up the project
