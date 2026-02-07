# Google Maps Review Scraper 📍

A powerful, automated web scraper built with Playwright and Python to extract business reviews, ratings, and timestamps directly from Google Maps.

This tool is designed with stealth in mind, utilizing custom browser contexts and anti-bot scripts to mimic human behavior and bypass basic scraping detection.

---

## 🚀 Features

- **Automated Search**: Automatically searches for specific keywords (e.g., "hotels near Kathmandu")
- **Deep Scrape**: Navigates through business listings and enters the "Reviews" tab for each result
- **Infinite Scroll Support**: Simulates mouse scrolling to trigger Google's lazy-loading review system
- **Stealth Mode**:
  - Injects custom JavaScript to hide `navigator.webdriver` flags
  - Uses persistent browser contexts for cookie and session management
  - Mimics real browser headers and locales
- **Data Export**: Saves extracted data (Review text, Rating, Date) into a structured `.csv` file

---

## 🛠 Tech Stack

- **Language**: Python 3.8+
- **Automation**: Playwright (Chromium)
- **Data Handling**: Pandas
- **Regex**: For parsing complex rating and date strings

---

## 📋 Prerequisites

Before running the script, ensure you have the following installed:

1. **Python 3.x**
2. **Playwright Browsers**:

```bash
pip install playwright pandas
playwright install chromium
```

---

## ⚙️ Configuration

Before running, update the `user_data_dir` path in the script to match your local system. This is where your browser profile and session data will be stored:

```python
user_data_dir = r"/your/local/path/to/project/User"
```

---

## 📂 Project Structure

```
.
├── main.py                      # Main scraper script
├── requirements.txt             # Python dependencies
├── *.csv                        # Output data files (generated after run)
├── User/                        # Browser profile data (persistent context)
└── venv/                        # Virtual environment (not tracked in Git)
```

---

## 🚦 Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/prashant7738/GoogleMap-Review-Scrapper.git
   cd GoogleMap-Review-Scrapper
   ```

2. **Create and activate virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers:**

   ```bash
   playwright install chromium
   ```

5. **Run the scraper:**

   ```bash
   python main.py
   ```

6. **Output**: The script will print the processing status to the console and save the results to CSV files.

---

## 🛡 Anti-Detection Measures

This script includes several advanced configurations to prevent being blocked:

- **Window Object Modification**: Overwrites `navigator.webdriver` to `undefined`
- **Fingerprint Masking**: Sets custom plugins and language arrays to match a standard Chrome installation
- **Randomized Delays**: Uses `wait_for_timeout` to simulate human reading time

---

## ⚠️ Disclaimer

This project is for **educational purposes only**. Scraping Google Maps may violate Google's Terms of Service. Use responsibly and ensure you are compliant with local data privacy laws (like GDPR).