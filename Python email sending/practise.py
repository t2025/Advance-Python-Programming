import smtplib
from smtplib import *
to=input("Enter the email address of receiver")
sender=input("Enter the email address of sender")
password=input("Enter password")
try:
   smtpobj= smtplib.SMTP('smtp.gmail.com',587)
   smtpobj.ehlo()
   smtpobj.starttls()
   smtpobj.login(sender,password)
   
   print("Success")
   smtpobj.close()

except Exception as e:
    print("Failed")




