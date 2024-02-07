import smtplib

my_email = "usuario@email.com"
my_password = "senha_secreta"
PROVIDER = "smtp.gmail.com"

with smtplib.SMTP(PROVIDER) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="fulano@destino.com",
        msg="Subject: New message\n\nThis is the body of message."
                     )