import requests
from bs4 import BeautifulSoup
import time
import smtplib
import datetime

go = True
x = str(datetime.datetime.now())
while go == True:
    url = 'WEBSITE'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text,"lxml")

    if str(soup).find('KEYWORD') == -1:
        time.sleep(60)
        continue

    else:
        my_user = 'EMAIL'
        my_pass = 'PASSWORD'

        from_addrs = 'FROM_EMAIL'
        to_addrs = 'TO_EMAIL'
        subject = 'SUBJECT'
        body = 'TEXT' + x
        body = 'Subject: {}\n\n{}'.format(subject,body)

        server = smtplib.SMTP_SSL('smtp.gmail.com',465)
        server.ehlo()
        server.login(my_user,my_pass)
        server.sendmail(from_addrs,to_addrs,body)
        server.close()
        print('Email has sent.')
        
        go = False

        

        