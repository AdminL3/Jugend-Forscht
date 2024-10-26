# 🐍 Twitter (X) Automation Bot with Selenium

A Python script that automates interactions with Twitter/X platform, including login, search, and data extraction capabilities. Perfect for social media research and content analysis.


## ⚙️ Prerequisites

1. **Python 3.x**
2. **Required Packages**:
   - Selenium
   - Pyperclip
3. **ChromeDriver** or **Google Chrome Browser**

## 🔧 Installation

1. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   .venv\Scripts\activate  # Windows
   source venv/bin/activate  # Linux/Mac
   ```

2. **Install Dependencies**:
   ```bash
   pip install selenium pyperclip
   ```

3. **ChromeDriver Setup** (optional if Chrome): 
   - Download matching version from [ChromeDriver Downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads)
   - Add to system PATH or place in script directory

## 🚀 Usage

### Standard Operation
```bash
python main.py
```

### Session Types

1. **Automatic Login**:
   - Select 'n' when prompted
   - Bot will:
     - Launch fresh Chrome instance
     - Handle cookie acceptance
     - Perform automated login

2. **Existing Session**:
   - Open Chrome with debugging port:
     ```bash
     "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222
     ```
   - Manually login to X
   - Select 'y' when running script
   - Continue with existing logged-in session

### Search & Extraction
1. Enter search query when prompted
2. Specify number of results to extract
3. URLs will be collected from search results

## 🔐 Authentication

Default credentials are provided (but using your own is recommended):
- Username: LeviBlu412024
- Email: l-blu@outlook.de
- Password: X+aDGi@S484+qcL

## ⚠️ Limitations & Known Issues

- **Two-Factor Authentication**: Not supported
- **Dynamic Content**: May need adjustments for Twitter's UI changes
- **Rate Limiting**: No built-in handling for Twitter's rate limits
- **Session Handling**: Debug port must be manually configured for existing sessions

## 🛠️ Technical Details

- Uses Selenium WebDriver for browser automation
- Implements explicit waits for better reliability
- Handles cookie consent popups automatically
- Supports both fresh and existing Chrome sessions
- Extracts article URLs using XPath and tag selection

## 📝 Future Improvements

- [ ] Add support for 2FA
- [ ] Add data export functionality
- [ ] Data Analytics

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests.

## 📬 Support

For issues and questions:
1. Open an issue in the repository
2. Provide detailed description of the problem
3. Include steps to reproduce if applicable

## 📜 License

This project is open source - feel free to use and modify with attribution.