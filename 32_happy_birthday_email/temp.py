# import smtplib

# connection = smtplib.SMTP("smtp.gmail.com", port=587)

# email = 'nelsontesting987@gmail.com'
# password = '123456'
# connection.starttls()

# connection.login(user=email,password=password)

# connection.sendmail(from_addr=email,to_addrs='nelsonfse@gmail.com',msg='hello')


import datetime as dt

now = dt.datetime.now()

print(now.weekday())

