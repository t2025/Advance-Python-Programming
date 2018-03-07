import pymysql
db=pymysql.connect("localhost","root","root","Python_App")


sname=raw_input("enter name")
fname=raw_input("enter father name")
address=raw_input("Enter address")
mobile=int(raw_input("Enter mobile no"))

cursor=db.cursor()
sql="UPDATE student "\
    "SET sname='%s',fname='%s',address='%s',mobile=%d" %(sname,fname,address,mobile)
try:
    res=cursor.execute(sql)
    if res>0:
        print "updated"
except Exception as e:
    print e
    print "Failed"
db.commit()
db.close()
