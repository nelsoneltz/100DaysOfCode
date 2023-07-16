#Monday Motivation Project
import smtplib
import datetime as dt
import random

email = 'nelsontesting987@gmail.com'
password = '123456'

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 6:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(
            from_addr=email,
            to_addrs=email,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )
