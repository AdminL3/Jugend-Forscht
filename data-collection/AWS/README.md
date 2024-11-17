# AWS Python Instance Setup

---

## Step 1: Launch an EC2 Instance

1. **Login to AWS Console**:

   - Go to the [AWS Management Console](https://aws.amazon.com/console/).
   - Select **EC2**.

2. **Launch a New EC2 Instance**:

   - Click **Launch Instance**.
   - Choose an Amazon Machine Image --> **Ubuntu Server**.
   - Select the instance type, e.g., **t2.micro** (for free tier).
   - Configure all the settings (accept defaults or customize).
   - Under **Key Pair**, either create a new key pair or select an existing one. Download the `.pem` file. (Important for accessing later!)
   - Launch the instance.

3. **Get Public DNS of the Instance**:
   - In the **EC2 Dashboard**, go to **Instances**.
   - Select your instance and find the **Public DNS (IPv4)** address.
   - Should look like this: ec2-XX-XX-XXX-XXX.compute-1.amazonaws.com

---

## Step 2: Connect to EC2 Instance

1. **Open Terminal** on your local machine.

2. Access your **AWS** Folder

   ```sh
   cd C:\Users\Path\to\AWS
   ```

   - Your **key.pem** and other files should be here

3. **SSH into EC2 Instance**:

   - Use the public DNS or IP address from your EC2 instance.

   ```sh
   ssh -i key.pem ubuntu@ec2-XX-XX-XXX-XXX.compute-1.amazonaws.com
   ```

- When asked if you trust the connection, type `yes` to continue.

---

## Step 3: Install Dependencies

Now that you are connected you can do your usual setup:

1. **Update Package Lists**:

   - Run the following to make sure your package lists are up to date:

   ```sh
   sudo apt update
   ```

2. **Install Python and Pip**:

   - Install Python 3 and the necessary packages:

   ```sh
   sudo apt install python3 python3-pip
   ```

3. **Install Venv** (optional):
   ```sh
   python3-venv
   ```
4. **Install Chromium and ChromeDriver** (to use selenium):

   - Install Chromium and ChromeDriver on your EC2 instance (ensure they are compatible):

   ```sh
   sudo apt install chromium-browser
   sudo apt install chromedriver
   ```

   - Create a symlink to make `chromedriver` accessible globally:

   ```sh
   sudo ln -s /usr/lib/chromium-browser/chromedriver /usr/bin/chromedriver
   ```

---

## Step 4: Set Up Virtual Environment

1. **Create a Virtual Environment**:

   - Navigate to your project directory or create a new directory for your project:

   ```sh
   mkdir my_project
   cd my_project
   python3 -m venv venv
   ```

2. **Activate the Virtual Environment**:

   - Activate the virtual environment to isolate your Python dependencies:

   ```sh
   source venv/bin/activate
   ```

3. **Install local Dependencies**:

   - Install all the dependencies you want in your project:
   - I am going to install Selenium

   ```sh
   pip install selenium
   ```

---

## Step 5: Transfer Files from Local Machine to EC2

1. **Use SCP to Transfer Files**:

   - On your local machine, navigate to the directory where your `main.py` / **code** is located. Use `scp` (SecureCopy) to copy files to your EC2 instance:

   ```sh
   scp -i key.pem main.py ec2-XX-XX-XXX-XXX.compute-1.amazonaws.com:/home/ubuntu/your_project/
   ```

   - Ensure that you are in the correct directory where your files are (See step 2.2)

---

## Step 6: Run the Script on EC2

1. **SSH Into Your EC2 Instance** (if not already connected):

   ```sh
   ssh -i key.pem ubuntu@ec2-XX-XX-XXX-XXX.compute-1.amazonaws.com
   ```

2. **Navigate to the Project Directory**:

   ```sh
   cd /home/ubuntu/your_project
   ```

3. **Run the Python Script**:

   ```sh
   python3 main.py
   ```

---

## Step 7: Troubleshooting

1. **Permission Issues When Installing Packages**:

   - If you encounter permission issues, ensure you're using `sudo` where necessary for installing software packages.

2. **Chromedriver Version Mismatch**:

   - Ensure that the version of `chromedriver` is compatible with the version of Google Chrome/Chromium installed on the instance. You can check your `chromedriver` version by running:

   ```sh
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
