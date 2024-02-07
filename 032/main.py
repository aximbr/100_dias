import smtplib
import datetime as dt
import random

#Load the quotes.txt to a list 
#Check the day of week
#If the day match, pick a random quote and e-mail to destination

my_email = "usuario@email.com"
my_password = "senha_secreta"
PROVIDER = "smtp.gmail.com"
DESTINATION = "somebody@email.com"

def send_message(destination, message):
    with smtplib.SMTP(PROVIDER) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=destination,
            msg=f"Subject: New message\n\n{message}"
                        )

#main()
with open("quotes.txt", "r") as fp:
    data = fp.readlines()
    
now = dt.datetime.now()

if now.weekday() == 2: #Wednesday
    message = random.choice(data)
    send_message(DESTINATION, message)
else:
    print("Nothing to send")