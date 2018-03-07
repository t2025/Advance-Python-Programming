import smtplib
from smtplib import *

to=raw_input("Enter the email address of receiver")
gmail_user=raw_input("Enter email address of sender")
gmail_password=raw_input("Enter password of sender")
header='To:'+to+'\n'+'From'+gmail_user+'\n'+'subject: Text message\n'
print(header)
msg=header+'\n'+'Hello!'
try:
    smtpObj=smtplib.SMTP("smtp.gmail.com",587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(gmail_user,gmail_password)
    print "Success!"
    smtpObj.close()   
except Exception as e:
    print e
    print 'failed'
    
