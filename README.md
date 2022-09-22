# snusbase-breached-email-collector
With a list of emails, check for several breaches available for each gmail and save it. It will keep the email only if there is a breach found on snusbase database.

<h2>How to setup</h2>
1. run this command in terminal: pip3 install -r requirements.txt

2. run this command in terminal: playwright install
3. open the Email_Breach_finer.py and replace username and password with your snusbase login
4. provide email addresses that you want to check breach for in the gmail.txt file
5. and then just run python3 Email_Breach_finer.py 
<h3>For GUI</h3>
7. for GUI view, open Email_Breach_finer.py and place this line: headless=False, slow_mo=100 between the brackets () of the 9th line in the code.

<h3>Finishing</h3>
Founded breached emails will be saved in the Breach.txt file with the number of breaches found on the database.
<h3 align=center>Thats it! Ready to fly<h3>
