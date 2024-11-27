# Automated Data Collection with AWS

### Setup:

- See my [Setup Guide](./Setup.md) for a **VERY** detailed explanation on how to set up your AWS EC2 Instance.

---

### Upload Files:

- Use `scp` to **transfer files** from your local machine to your EC2 Instance.
- See [Step 5 of the Setup Guide](./Setup.md#step-5-transfer-files-from-local-machine-to-ec2) for more information.

---

### Run Python Scripts:

- **Run** your Python Scripts on the EC2 Instance.
- See [Step 6 of the Setup Guide](./Setup.md#step-6-run-the-script-on-ec2) for more information.

---

### Download created files:

- Use `scp` to transfer files from your EC2 Instance to your local machine.

```sh
scp -i /path/to/your-key.pem ec2-user@your-ec2-public-ip:/path/to/remote/file /path/to/local/destination
```

---

### Merge created data with existing data:

- My file [`merge_data.py`](./merging_sources.py) is a Python script that merges the data you collected with existing data.

---

### Most used commands

- In [commands.txt](./commands.txt) you can find my most used commands for this process.
