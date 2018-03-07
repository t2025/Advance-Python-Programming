import smtplib
from smtplib import *
to=input("Enter the email address of receiver")
sender=input("enter the email address of sender")
password=input("Enter the password")
header="To:"+to+"\n"+"From:"+sender
print(header)
msg="Hi ! This is a test mail"
try:
    smtpObj=smtplib.SMTP("smtp.gmail.com",587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(sender,password)
    smtpObj.sendmail(sender,to,msg)
    print("Success")
    smtpObj.close()
except Exception as e:
    print("Failed")
    print(e)    








