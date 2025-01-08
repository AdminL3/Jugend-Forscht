# Running a Python Script on AWS EC2

See my post on [Running a Python Script in the Cloud](https://dev.to/adminl3/how-to-run-python-in-the-cloud-mkh)

To do this, I’m going to use Amazon Web Services (AWS) to create a virtual machine and run the Python script on it!

---

## Step 1: Launch an EC2 Instance

### 1. Login to AWS Console:

- Go to the AWS Management Console.
- Select **EC2**.

### 2. Launch a New EC2 Instance:

- Click **Launch Instance**.
- Choose an Amazon Machine Image → **Ubuntu Server**.
- Select the instance type, e.g., **t2.micro** (for free tier).
- Configure all the settings (accept defaults or customize).
- Under **Key Pair**, either create a new key pair or select an existing one. Download the `.pem` file (important for accessing later!).
- Launch the instance.

### 3. Get Public DNS of the Instance:

- In the EC2 Dashboard, go to **Instances**.
- Select your instance and find the **Public DNS (IPv4)** address.
  - Should look like this: `ec2-XX-XX-XXX-XXX.compute-1.amazonaws.com`.

---

## Step 2: Connect to EC2 Instance

### 1. Open Terminal on Your Local Machine:

- Navigate to your AWS folder:
  ```bash
  cd C:\Users\Path\to\AWS
  ```

Your `key.pem` file and other related files should be here.

### 2. SSH into EC2 Instance:

- Use the public DNS or IP address from your EC2 instance:
  ```bash
  ssh -i key.pem ubuntu@ec2-XX-XX-XXX-XXX.compute-1.amazonaws.com
  ```
- When asked if you trust the connection, type `yes` to continue.

---

## Step 3: Install Dependencies

### 1. Update Package Lists:

- Run the following to ensure your package lists are up to date:
  ```bash
  sudo apt update
  ```

### 2. Install Python and Pip on EC2 Instance:

- Install Python 3 and the necessary packages:
  ```bash
  sudo apt install python3 python3-pip
  ```

### 3. Install Other Packages (Optional):

- If you want to install other packages or use a virtual environment, you can do that now.

#### Installing Selenium:

```bash
pip install selenium
```

#### Installing Chromium and ChromeDriver (for Selenium):

```bash
sudo apt install chromium-browser
sudo apt install chromedriver
```

- Create a symlink to make ChromeDriver accessible globally:
  ```bash
  sudo ln -s /usr/lib/chromium-browser/chromedriver /usr/bin/chromedriver
  ```

---

## Step 4: Transfer Files from Local Machine to EC2

### Use SCP to Transfer Files:

- On your local machine, navigate to the directory where your `main.py` or code is located.
- Use `scp` (SecureCopy) to copy files to your EC2 instance:
  ```bash
  scp -i key.pem main.py ec2-XX-XX-XXX-XXX.compute-1.amazonaws.com:/home/ubuntu/your_project/
  ```
- Ensure that you are in the correct directory where your files are located (see step 2.1).

---

## Step 5: Run the Script on EC2

### 1. SSH Into Your EC2 Instance (if not already connected):

```bash
ssh -i key.pem ubuntu@ec2-XX-XX-XXX-XXX.compute-1.amazonaws.com
```

### 2. Navigate to the Project Directory:

```bash
cd /home/ubuntu/your_project
```

### 3. Run the Python Script:

```bash
python3 main.py
```

---

## Step 6: Stop EC2 Instance

Once you’re done with your EC2 instance, stop it to avoid unnecessary charges:

1. Go to **EC2 Dashboard** in AWS.
2. Select your instance.
3. Click **Actions** → **Instance State** → **Terminate Instance**.

---
