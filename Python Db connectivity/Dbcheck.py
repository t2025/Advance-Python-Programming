import pymysql




db=pymysql.connect("localhost","root","root","Python_App")
cursor=db.cursor()

try:
    '''
    for i in range(0,5):
        ename=raw_input("Enter employee name")
        salary=int(raw_input("Enter salary"))
        address=raw_input("Enter address")
        sql="insert into employee values('%s',%d,'%s')"%(ename,salary,address)
     '''   
    #sql1="select SUM(salary) from employee"
    sql2="select * from employee"
    sql3="select SUM(salary) from employee"
    sql4="select * from employee order by salary desc limit 1"
    
    #r=cursor.execute(sql1)
    #r =cursor.execute(sql2)
    r1=cursor.execute(sql3)
   
    res=cursor.fetchall()
    
    '''
    for row in res:
        ename=row[0]
        salary=row[1]
        address=row[2]
        sum1=row[3]
        print(ename,salary,address)
    '''
    for row in res:
        s=row[0]
        print(s)
    r2=cursor.execute(sql4)
    res1=cursor.fetchall() 

    for row in res1:
        ename=row[0]
        salary=row[1]
        address=row[2]
        print(ename,salary,address)
     
       
    '''   
    if r>0:
        print "Success"
    '''    
    #db.commit()
except Exception as e:
    print(e)
    print "Failed"
db.close()             



 




