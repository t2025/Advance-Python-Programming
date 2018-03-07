import pymysql

db = pymysql.connect('localhost', 'root', 'root', 'student')

cursor = db.cursor()

sid = int(input('Enter student id: '))
daytomarkattendance = int(input('Enter day to mark attendance: '))

try:
    r = cursor.execute('Update attendance set d' + str(daytomarkattendance) + ' = 1 where id = ' + str(sid))
    if r:
        print('Success')
    else:
        print('Failure')
    db.commit()
except Exception as e:
    print(e)









