# Data Collection from NYT

---

## Step 1: Get Links from **NYT API**

This step involves collecting article links from the New York Times (NYT) API. You can find the code for this step in the [Get_Links.py](https://github.com/AdminL3/Jugend-Forscht/blob/main/data-collection/Get_Links.py) file.

1. **Get NYT API Key**:

   - Create a developer account on the [NYT Developer Portal](https://developer.nytimes.com/).
   - Go to the [NYT Apps](https://developer.nytimes.com/my-apps) page.
   - Get your API key.

2. **Use API**:

   - Go to the [NYT APIs](https://developer.nytimes.com/apis) page.
   - Explore the API structure.
   - Choose the data you want to collect (links or titles).
   - Save the data as a file.

---

## Step 2: Extract Source Code from URLs

In this step, you can choose from different methods to extract the source code from URLs. Here are the options:

### 1. Selenium

1. **Install** Selenium:

   ```bash
   pip install selenium
   ```

2. Use **Selenium**:

   - Create Options

   ```bash
   options = webdriver.ChromeOptions()
   options.add_argument("--start-maximized")
   options.add_argument("--disable-search-engine-choice-screen")
   options.add_experimental_option("detach", True)
   options.add_argument("--headless")
   driver = webdriver.Chrome(options=options)
   ```

   - Create Driver

   ```bash
   driver = webdriver.Chrome(options=options)
   ```

   - Access Content

   ```bash
   while True:
      try:
         driver.get(url)
         page_source = driver.execute_script(
               "return document.documentElement.outerHTML;")
         break
      except:
         pass
   ```

### 2. Requests

- This Works for some time until you get blocked. Then you should use Proxys or external APIs --> See **Proxyrotation** and **ExternalAPIs**

1. **Install** Requests:

   ```bash
   pip install requests
   ```

2. Use **Requests**:

   - Access HTML Code

   ```bash
   response = requests.get(url)
   page_source = response.text
   ```

### 3. External API

- I am using [ScraperAPI](https://www.scraperapi.com/)
- This Works, but you are limited tokens and its slower

1. **Install** Requests:

   ```bash
   pip install requests
   ```

2. Access **API**:

   ```bash
   payload = {'api_key': api_key,
               'url': url}
   r = requests.get('https://api.scraperapi.com/', params=payload)
   ```

### 4. Proxyrotation

- You can get free Proxys at [Free Proxy List](https://free-proxy-list.net/)
- Some Proxys do not work!

1. **Install** Requests:

   ```bash
   pip install requests
   ```

2. Check which Proxies work:

   - Download Proxies
   - Loop through them and save as file

3. Use working proxies to access HTML
   - See **2. Requests**

---

## Step 2.5: Use AWS to run in the cloud

- See [Run Python in the Cloud](/AWS)

1. **Create a Virtual Environment**:

   - Navigate to your project directory or create a new directory for your project:

   ```bash
   mkdir my_project
   cd my_project
   python3 -m venv venv
   ```

---

## Step 4: Transfer Files from Local Machine to EC2

1. **Use SCP to Transfer Files**:

   - On your local machine, navigate to the directory where your code is located.
   - Use `scp` (Secure Copy) to copy files to your EC2 instance:

   ```bash
   scp -i key.pem main.py ec2-XX-XX-XXX-XXX.compute-1.amazonaws.com:/home/ubuntu/your_project/
   ```

   - Ensure that you are in the correct directory where your files are (See step 2.2)

---

## Step 5: Run the Script on EC2

1. **SSH Into Your EC2 Instance** (if not already connected):

   ```bash
   ssh -i key.pem ubuntu@ec2-XX-XX-XXX-XXX.compute-1.amazonaws.com
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd /home/ubuntu/your_project
   ```

3. **Run the Python Script**:

   ```bash
   python3 main.py
   ```

---

## Step 6: Troubleshooting

1. **Permission Issues When Installing Packages**:

   - If you encounter permission issues, ensure you're using `sudo` where necessary for installing software packages.

2. **Chromedriver Version Mismatch**:

   - Ensure that the version of `chromedriver` is compatible with the version of Google Chrome/Chromium installed on the instance. You can check your `chromedriver` version by running:

   ```bash
   chromedriver --version
   ```

3. **No `py` Command Available**:

   - Use `python3` instead of `py` to run your Python scripts on Linux-based systems (e.g., EC2).

4. **File Transfer Issues**:

   - Ensure that the paths used in `scp` are correct and that there are no typos or missing files.

---

## Step 7: Stop EC2 Instance

Once you’re done with your EC2 instance, stop it to avoid unnecessary charges.

1. Go to the **EC2 Dashboard** in the AWS Management Console.
2. Select your instance.
3. Click **Actions** → **Instance State** → **Terminate Instance**.
