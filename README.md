# Ultimate Outlook Checker

This script is designed to check the validity of Microsoft Outlook accounts using threading for maximum efficiency. It processes multiple accounts and proxies simultaneously, checking whether the accounts are valid, and logging the results to text files. The script includes colorful console output and status updates throughout the checking process.

## Features

- **Multi-Threaded Account Checking**: Allows you to check multiple accounts simultaneously with configurable thread numbers for faster processing.
- **Proxy Support**: Supports the use of HTTP proxies to avoid rate-limiting.
- **Real-Time Status Updates**: Displays account checking progress, valid accounts, and bad accounts in real-time using a custom console title.
- **Color-Coded Output**: Uses `colorama` and `pystyle` for colorful and styled terminal output, making it easier to track account statuses.
- **Results Logging**: Logs valid accounts to `worked.txt` and invalid accounts to `invaild.txt`.
- **Custom Console Title**: Updates the terminal title with progress, showing checked accounts and invalid results.

## Requirements

- Python 3.x
- Required Libraries:
  - `requests`
  - `colorama`
  - `pystyle`
  - `requests_toolbelt`

## How to Use

1. **Install Dependencies**:
   - Run the following command to install the necessary libraries:
     ```bash
     pip install requests colorama pystyle requests_toolbelt
     ```

2. **Prepare Account and Proxy Files**:
   - Create an `accounts.txt` file with the format:
     ```text
     email1@example.com:password1
     email2@example.com:password2
     ```
   - Create a `proxies.txt` file (optional) with one proxy per line in the following format:
     ```text
     ip:port
     ```

3. **Run the Script**:
   - To execute the script, run:
     ```bash
     python main.py
     ```

4. **Input Threads**:
   - You will be prompted to enter the number of threads you want to use. For example:
     ```bash
     Pls put threads: 10
     ```

5. **Monitor Progress**:
   - The script will output status updates in the terminal, showing the progress of the account checking process with colorful messages.

6. **Results**:
   - **Valid Accounts**: Logged in `worked.txt`.
   - **Invalid Accounts**: Logged in `invaild.txt`.

## How It Works

- **Account Checking**: The script uses the Microsoft login system to verify the provided email and password. If the account is valid, it logs the account to `worked.txt`.
- **Proxy Support**: Proxies are loaded from `proxies.txt`, and a random proxy is selected for each request to help avoid IP bans.
- **Multi-threading**: The script uses multiple threads to check several accounts at once, improving performance and reducing checking time.

## Customization

- **User-Agent**: You can modify the `ua` variable to change the user-agent string for the requests.
- **Thread Count**: You can increase or decrease the thread count when prompted to suit your system's performance capabilities.

## Console Output

The script uses color-coded output for easy monitoring:
- **Cyan**: Information and progress updates.
- **Red**: Errors or invalid account status.
- **Green**: Valid account detected.

## Notes

- Make sure your `accounts.txt` and `proxies.txt` files are correctly formatted before running the script.
- The script checks for valid Microsoft accounts and logs the results. It also handles privacy notice pages and other Microsoft account prompts automatically.

