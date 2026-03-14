# # import smtplib
# #
# # my_email = "salembirhanu3@gmail.com"
# # password = "19"
# #
# # with smtplib.SMTP('smtp.gmail.com') as connection:
# #     connection.starttls()
# #     connection.login(user=my_email, password=password)
# #     connection.sendmail(from_addr=my_email,
# #                         to_addrs="surebahiru22@gmail.com",
# #                         msg="Subject:hello\n\n this is the body")
# #     connection.close()
# 
# 
# import datetime as dt
# 
# now = dt.datetime.now()
# print(now.year)
# 
# date_of_birth = dt.datetime(year=2005 ,month=9, day=29 ,hour=17)
# print(date_of_birth)
import pandas
import pandas as pd
import datetime as dt
import smtplib
from random import *

MY_EMAIL = "HHH@gmail.com"
PASSWORD = "SL;J"

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    with open("quotes.txt", "r") as f:
        all_quotes = f.readlines()
        qoute = choice(all_quotes)
    print(qoute)
    connection =smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,to_addrs=MY_EMAIL,msg=f"Subject:Monday Motivation\n\n {qoute}")
    connection.close()
