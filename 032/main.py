##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

#load birthdays.cdv to a dictionary
import pandas
import datetime as dt
import random
import smtplib

my_email = "usuario@email.com"
my_password = "senha_secreta"
PROVIDER = "smtp.gmail.com"



def send_message(name_in, email_in):
    
    # letters = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
    # random_letter = random.choice(letters)
    random_letter = f"letter_templates/letter_{random.randint(1,3)}.txt"
    
    with open(random_letter, "r") as fp:
        template_letter = fp.read()
        
    new_message = template_letter.replace("[NAME]", name_in)
    
    with smtplib.SMTP(PROVIDER) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email_in,
            msg=f"Subject: Happy Birthday!\n\n{new_message}"
                        )



#main()
data = pandas.read_csv("birthdays.csv").to_dict("records")

now = dt.datetime.now()

for record in data:
    if record["month"] == now.month and record["day"] == now.day:
        send_message(record["name"], record["email"])
        



