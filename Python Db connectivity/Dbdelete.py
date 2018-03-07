import pymysql
db=pymysql.connect("localhost","root","root","Python_App")
sname=raw_input("Enter the name")
cursor=db.cursor()
try:
    sql="DELETE from student WHERE sname='%s' "%(sname)
    res=cursor.execute(sql)
    if res>0:
        print "Done"
except Exception as e:
    print e 
    print "Failed"
db.close()                

