# Data Collection from NYT

---

## Step 1: Get Links from **NYT API**

##### See [Get_Links.py](https://github.com/AdminL3/Jugend-Forscht/blob/main/data-collection/Get_Links.py)

1. **Get NYT API Key**:

   - Create Developer Account
   - Go to the [NYT Apps](https://developer.nytimes.com/my-apps).
   - Get **API Key**.

2. **Use API**:

   - Go to [NYT APIs](https://developer.nytimes.com/apis).
   - Check out the API Structure.
   - Get links or titles (depending on needs)
   - Save as File

---

## Step 2: Extract Source code from URLs

#### I tried different ways to do this choose yourself (sorted by working level)

### 1. Selenium

1. **Install** Selenium.

   ```bash
   pip install selemij
   ```

   - Your **key.pem** and other files should be here

2. **SSH into EC2 Instance**:

   - Use the public DNS or IP address from your EC2 instance.

   ```bash
   ssh -i key.pem ubuntu@ec2-XX-XX-XXX-XXX.compute-1.amazonaws.com
   ```

- When asked if you trust the connection, type `yes` to continue.

---

## Step 3: Install Dependencies

Now that you are connected you can do your usual setup:

1. **Update Package Lists**:

   - Run the following to make sure your package lists are up to date:

   ```bash
   sudo apt update
   ```

2. **Install Python and Pip**:

   - Install Python 3 and the necessary packages:

   ```bash
   sudo apt install python3 python3-pip
   ```

3. **Install Venv** (optional):
   ```bash
   python3-venv
   ```
4. **Install Chromium and ChromeDriver** (to use selenium):

   - Install Chromium and ChromeDriver on your EC2 instance (ensure they are compatible):

   ```bash
   sudo apt install chromium-browser
   sudo apt install chromedriver
   ```

   - Create a symlink to make `chromedriver` accessible globally:

   ```bash
   sudo ln -s /usr/lib/chromium-browser/chromedriver /usr/bin/chromedriver
   ```

---

## Step 4: Set Up Virtual Environment

1. **Create a Virtual Environment**:

   - Navigate to your project directory or create a new directory for your project:

   ```bash
   mkdir my_project
   cd my_project
   python3 -m venv venv
   ```

2. **Activate the Virtual Environment**:

   - Activate the virtual environment to isolate your Python dependencies:

   ```bash
   source venv/bin/activate
   ```

3. **Install local Dependencies**:

   - Install all the dependencies you want in your project:
   - I am going to install Selenium

   ```bash
   pip install selenium
   ```

---

## Step 5: Transfer Files from Local Machine to EC2

1. **Use SCP to Transfer Files**:

   - On your local machine, navigate to the directory where your `main.py` / **code** is located. Use `scp` (SecureCopy) to copy files to your EC2 instance:

   ```bash
   scp -i key.pem main.py ec2-XX-XX-XXX-XXX.compute-1.amazonaws.com:/home/ubuntu/your_project/
   ```

   - Ensure that you are in the correct directory where your files are (See step 2.2)

---

## Step 6: Run the Script on EC2

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

## Step 7: Troubleshooting

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

## Step 8: Stop EC2 Instance

Once you’re done with your EC2 instance, stop it to avoid payment

1. Go to **EC2 Dashboard** in AWS.
2. Select your instance.
3. Click **Actions** → **Instance State** → **Terminate Instance**.

---
