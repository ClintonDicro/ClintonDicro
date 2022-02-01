# # import os
# # import math
# # import random
# # import smtplib

# # digits="0123456789"
# # OTP=""
# # for i in range(6):
# #     OTP+=digits[math.floor(random.random()*10)]
# # otp = OTP + " is your OTP"
# # msg= otp
# # s = smtplib.SMTP('smtp.gmail.com', 587)
# # s.starttls()
# # s.login("dicro12347@gmail.com", "hwumijdjdewurliq")
# # emailid = input("Enter your email: ")
# # s.sendmail('&&&&&&&&&&&',emailid,msg)
# # a = input("Enter Your OTP >>: ")
# # if a == OTP:
# #     print("Verified")
# # else:
# #     print("Please Check your OTP again")
# import datetime
# from datetime import date, timedelta



# # date = '2021-05-21 11:22:03'
# # datem = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
# # print(datem.day)        # 25
# # print(datem.month)      # 5
# # print(datem.year)       # 2021
# # print(datem.hour)       # 11
# # print(datem.minute)     # 22
# # print(datem.second)     # 3


# # start_date = date(2022, 1, 10) 
# # end_date = date(2022, 1, 28)    # perhaps date.now()

# # delta = end_date - start_date   # returns timedelta

# # for i in range(delta.days + 1):
# #     day = start_date + timedelta(days=i)
# #     print(day)


# # end_date = '2022-1-28'
# # datee = datetime.datetime.strptime(end_date, "%Y-%m-%d")
# # day = datee.day - 1
# # dayone = datee.day + 1
# # print(dayone)
# # print(day)
# # print(datee.day)

# # today= date.today()
# # today_date = today.strftime("%Y-%m-%d")

# # current_year = int(today.strftime("%Y"))
# # current_month = today.strftime("%m")
# # this_day = int(today.strftime("%d"))
# # add_day = this_day + 4
# # print(add_day)
# # print(today_date)
# # print(current_month)


# from datetime import date, timedelta

# start_date = date(2022, 1, 25) 
# end_date = date(2022, 1, 31)    # perhaps date.now()

# delta = end_date - start_date   # returns timedelta

# # before = range(delta.days)
# # current = range(delta.days+1)
# # after = range(delta.days+2)
# # print(before)
# # print(current)
# # print(after)

# # a = [before,current,after]
# # print(a[0])

# # for i in a[0]:
# #     if a[0]: 
# #         day = start_date + timedelta(days=i)
# #         print(day)
# #         print('sent mail')
# # for i in a[1]: 
# #     day = start_date + timedelta(days=i)
# #     print(day)
# # for i in a[2]: 
# #     day = start_date + timedelta(days=i)
# #     print(day)

# print(delta)

# for i in range(delta.days):
#     day = start_date + timedelta(days=i)
#     n = delta.days
#     print(day)
# print(n)

# for i in range(delta.days + 1):
#     day = start_date + timedelta(days=i)
#     n = delta.days + 1
#     print(day)
# print(n)

# for i in range(delta.days + 2):
#     day = start_date + timedelta(days=i)
#     n = delta.days + 2
#     print(day)
# print(n)

# import datetime
# from datetime import date,timedelta


# curr_date1 = date.today()
# curr_date2 = curr_date1.strftime("%Y/%m/%d")
# curr_date_temp1 = datetime.datetime.strptime(curr_date2, "%Y/%m/%d")

# end="2022/1/31"
# curr_date_temp = datetime.datetime.strptime(end, "%Y/%m/%d")

# new_date = curr_date_temp + datetime.timedelta(days=0)
# new_date1 = curr_date_temp + datetime.timedelta(days=-1)
# new_date2 = curr_date_temp + datetime.timedelta(days=1)

# if curr_date_temp1  == new_date : 
#     print("current date")
# elif curr_date_temp1  == new_date1: 
#     print("before date")
# elif curr_date_temp1  == new_date2:
#     print("after day")
# else:
#     print("Date not missed")


import datetime as dt
import time
import smtplib
from email.message import EmailMessage

def send_email():
    get_email = smtplib.SMTP(host="smtp.gmail.com", port=587)
    get_email.starttls()
    get_email.login("dicro12347@gmail.com", "hwumijdjdewurliq")
    message = EmailMessage()
    msg = "confirmation"
    message.set_content(msg)
    message['Subject'] = 'Alert message'
    message['From'] = 'dicro12347@gmail.com'
    message['To'] = 'clintondicro12345@gmail.com'
    get_email.send_message(message)
    # app.logger.info('Email send successfully.')
    get_email.quit()
    return 'Email sent'

def send_email_at(send_time,send_time_one,send_time_two,send_time_three):
    
    time.sleep(send_time.timestamp() - time.time())
    print(send_time)
    send_email()
    print('email sent')
    time.sleep(send_time_one.timestamp() - time.time())
    print(send_time_one)
    send_email()
    print('email sent')
    time.sleep(send_time_two.timestamp() - time.time())
    print(send_time_two)
    send_email()
    print('email sent')
    time.sleep(send_time_three.timestamp() - time.time())
    print(send_time_three)
    send_email()
    print('email sent')

first_email_time = dt.datetime(2022,1,30,14,34,0)
second_email_time = dt.datetime(2022,1,30,14,35,0) # set your sending time in UTC
third_email_time = dt.datetime(2022,1,30,14,36,0)
four_email_time = dt.datetime(2022,1,30,14,37,0)
interval = dt.timedelta(seconds=1*60) # set the interval for sending the email

send_time = first_email_time
send_time_one = second_email_time
send_time_two = third_email_time
send_time_three = four_email_time
while True:
    send_email_at(send_time,send_time_one,send_time_two,send_time_three)
    send_time = send_time + interval
    send_time_one = send_time_one + interval
    send_time_two = send_time_two + interval
    send_time_three = send_time_three + interval
