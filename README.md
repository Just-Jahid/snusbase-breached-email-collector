**### Snusbase Breached Email Collector**

This Python script checks a list of email addresses against the Snusbase database to identify any breaches. If a breach is found for an email, it will be saved for further review.

**## Features**
- Checks multiple email addresses against the Snusbase database.
- Saves only those emails that have been compromised.
- Option for a graphical user interface (GUI) for easier interaction.

**## Prerequisites**
- Python 3.x
- Access to a Snusbase account

**## Setup Instructions**

## 1. Install Required Libraries
Open your terminal and run the following command to install the necessary libraries:

```
pip3 install -r requirements.txt
```
2. Install Playwright
Run this command to install Playwright, which is required for web scraping:
```
playwright install

```
3. Configure Your Login Credentials
Open Email_Breach_finer.py in a text editor and replace the username and password placeholders with your Snusbase login credentials.

4. Prepare Email List
Create a text file named gmail.txt in the same directory as the script. Add the email addresses you want to check for breaches, one per line.

5. Run the Script
Execute the following command in your terminal to run the script:
```
python3 Email_Breach_finer.py
```
**For GUI View**
If you prefer a graphical user interface, follow these steps:

Open Email_Breach_finer.py and locate the 9th line in the code.
Modify it to include the following parameters:
```
headless=False, slow_mo=100
```
This will allow you to see the browser actions as the script runs.

**Output**

The found breached emails will be saved in a file named Breach.txt, which will also indicate the number of breaches found for each email in the Snusbase database.

**Conclusion**

You are now ready to check for email breaches using the Snusbase Breached Email Collector. If you encounter any issues or have questions, feel free to raise an issue in this repository!
