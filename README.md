
# 🐍 Twitter Automation Bot with Selenium

This Python script automates the login process on Twitter (now X) and performs a custom search on the platform using Selenium. It provides a template for web scraping and automated UI interactions.

## ⚙️ Prerequisites

1. **Python**
2. **Selenium**
3. **ChromeDriver** – Download the correct version [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) based on your Chrome browser version.

## 🔧 Setup

1. **Create a Virtual Environment** (optional):
   ```bash
   python -m venv venv
   .venv\Scripts\activate  # or source venv/bin/activate
   ```

2. **Install Selenium**:
   ```bash
   pip install selenium
   ```

3. **ChromeDriver Setup**: Ensure `chromedriver` is accessible in your PATH or in the same directory as the script.

## 📜 Script Functionality

1. **Browser Setup**: Opens a maximized Chrome window and disables search engine choice popups.
2. **Automated Login**: Logs in to Twitter using username, email, and password inputs.
3. **Search Execution**: After login, the user can enter a search term to look up content on Twitter.
4. **Output Functionality**: The Core Feature (yet to be implemented) analyses the data of the search query

## 🚀 Usage

Activate VENV (optional) (auto in VSCode)
```bash
.venv\Scripts\activate
```
Run Python file
```bash
py main.py
```



## 🛠️ Known Issues

- **Two-Factor Authentication (2FA)**: This script does not support accounts with 2FA enabled.
- **Popup Variability**: Occasional additional prompts may interrupt the flow.

## 📬 Contact

Feel free to open an issue for questions or suggestions!



