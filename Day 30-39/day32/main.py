# import datetime as dt
# import smtplib
# from random import *
# 
# MY_EMAIL = "HHH@gmail.com"
# PASSWORD = "SL;J"
# 
# now = dt.datetime.now()
# day_of_week = now.weekday()
# 
# if day_of_week == 0:
#     with open("quotes.txt", "r") as f:
#         all_quotes = f.readlines()
#         qoute = choice(all_quotes)
#     print(qoute)
#     connection =smtplib.SMTP("smtp.gmail.com")
#     connection.starttls()
#     connection.login(user=MY_EMAIL, password=PASSWORD)
#     connection.sendmail(from_addr=MY_EMAIL,to_addrs=MY_EMAIL,msg=f"Subject:Monday Motivation\n\n {qoute}")
#     connection.close()

from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "ASD@gmail.com"
PASSWORD = "asdfg"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row.month,data_row.day):data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_{random.randint(1,3)}"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[Name]", birthday_person["name"] )
    with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(MY_EMAIL,birthday_person["email"],msg=f"Subject:Happy Birthday!\n\n{contents}")



