import pymysql
db=pymysql.connect("localhost","root","root","attendance")
cursor=db.cursor()
sid=int(raw_input("Enter id"))
sname=raw_input("Enter student name")
email=raw_input("Enter email_id")
mobile=int(raw_input("Enter contact number"))
address =raw_input("Enter address")

sql="insert into students values(%d,'%s','%s','%d','%s')" % (sid,sname,email,mobile,address)
res=cursor.execute(sql)
try:
    if res>0:
        print "Details added successfully"
except Exception as e:
    print e
    print "Failed"
db.close()

    