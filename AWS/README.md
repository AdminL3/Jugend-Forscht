You're right! I apologize for the formatting mistake. Here's the corrected `README.md` with proper formatting:

````markdown
# EC2 Selenium Setup Guide

## Overview

This guide explains how to set up an EC2 instance, install necessary software, and run Python Selenium scripts remotely. You will also learn how to transfer your Python files from your local machine to the EC2 instance and run them.

---

## Step 1: Launch an EC2 Instance

1. **Login to AWS Console**:

   - Go to the [AWS Management Console](https://aws.amazon.com/console/).
   - Select **EC2** under "Compute".

2. **Launch a New EC2 Instance**:

   - Click **Launch Instance**.
   - Choose an Amazon Machine Image (AMI), e.g., **Ubuntu Server**.
   - Select the instance type, e.g., **t2.micro** (free tier eligible).
   - Configure the instance settings (accept default settings or adjust as needed).
   - Under **Key Pair**, either create a new key pair or select an existing one. Download the `.pem` file.
   - Open **Security Groups** and ensure that **SSH (port 22)** is allowed from your IP address.
   - Launch the instance.

3. **Get Public DNS of the Instance**:
   - In the **EC2 Dashboard**, go to **Instances**.
   - Select your instance and find the **Public DNS (IPv4)** address.

---

## Step 2: Connect to EC2 Instance

1. **Open Terminal** on your local machine.

2. **SSH into EC2 Instance**:

   - Use the public DNS or IP address from your EC2 instance.

   ```bash
   ssh -i /path/to/your-key.pem ubuntu@ec2-your-public-dns.compute-1.amazonaws.com
   ```
````

- Replace `/path/to/your-key.pem` with the actual path to your `.pem` key.
- When asked if you trust the connection, type `yes` to continue.

---

## Step 3: Install Dependencies

1. **Update Package Lists**:

   - Run the following to make sure your package lists are up to date:

   ```bash
   sudo apt update
   ```

2. **Install Python 3 and Pip**:

   - Install Python 3 and the necessary packages:

   ```bash
   sudo apt install python3 python3-pip python3-venv
   ```

3. **Install Chromium and ChromeDriver**:

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
   python3 -m venv myenv
   ```

2. **Activate the Virtual Environment**:

   - Activate the virtual environment to isolate your Python dependencies:

   ```bash
   source myenv/bin/activate
   ```

3. **Install Selenium**:

   - Install Selenium in your virtual environment:

   ```bash
   pip install selenium
   ```

---

## Step 5: Transfer Files from Local Machine to EC2

1. **Use SCP to Transfer Files**:

   - On your local machine, navigate to the directory where your `main.py` is located. Use `scp` to copy files to your EC2 instance:

   ```bash
   scp -i /path/to/your-key.pem main.py ubuntu@ec2-your-public-dns.compute-1.amazonaws.com:/home/ubuntu/
   ```

   - Ensure that paths are correct and replace `/path/to/your-key.pem` with the correct path.

---

## Step 6: Run the Script on EC2

1. **SSH Into Your EC2 Instance** (if not already connected):

   ```bash
   ssh -i /path/to/your-key.pem ubuntu@ec2-your-public-dns.compute-1.amazonaws.com
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd /home/ubuntu/my_project
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

## Step 8: Terminate EC2 Instance

Once you’re done with your EC2 instance, you can terminate it to avoid ongoing charges:

1. Go to **EC2 Dashboard** in AWS.
2. Select your instance.
3. Click **Actions** → **Instance State** → **Terminate Instance**.

---

## Conclusion

You’ve successfully set up an EC2 instance to run Selenium scripts remotely, transferred files using SCP, and executed your Python script. This setup allows you to offload tasks to a cloud environment, reducing the computational load on your local machine.

---

### Additional Notes:

- Make sure to secure your `.pem` key file, as it grants access to your EC2 instance.
- If you plan to run long-running scripts, consider using screen or tmux sessions to keep processes running after disconnecting.

```

This version has the correct formatting for headings, lists, and code blocks. You can now paste this into your `README.md` file. Let me know if there’s anything else you’d like to adjust!
```
