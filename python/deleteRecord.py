import pymysql as sql
c=sql.connect(host="localhost",user="root",password="hitiksha",database="hitiksha_demo")   #password mysql
con=c.cursor()

def DeleteRecord():
    id=int(input("Enter Id:"))

    q="delete from login where id='%d'"%(id)
    r=con.execute(q)
    if(r>0):
        print("Record Delete")
    else:
        print("Record Not Delete")
    c.commit()

DeleteRecord()