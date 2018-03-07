import pymysql
db=pymysql.connect("localhost","root","root","user")
cursor=db.cursor()
username=input("Enter username")
password=input("Enter password")
try:
    sql="select uname,password from user_detail WHERE uname='%s'"%(username)
    rs=cursor.execute(sql)
    r=cursor.fetchone()
    if r:
        print("Success")
    eid=int(input("Enter id "))
    exp=int(input("Enter amount"))
    cat=input("Enter actegory")
    date=input("Enter date")
    sql1="insert into expense values(%d,%d,'%s','%s')"%(eid,exp,cat,date)
    rs=cursor.execute(sql1)
    if rs:
        print("Successfully added!")
      
except Exception as e:
    print("Error")
    print(e)
db.commit()
db.close()            


