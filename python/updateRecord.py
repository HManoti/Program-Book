import pymysql as sql
c=sql.connect(host="localhost",user="root",password="hitiksha",database="hitiksha_demo")   #password mysql
con=c.cursor()

def UpdateRecord():
    id=int(input("Enter Id:"))
    p=input("Enter Password:")
    city=input("Enter City:")
    q="update login set password='%s', city='%s' where id='%d'"%(p,city,id)
    r=con.execute(q)
    if(r>0):
        print("Record Update")
    else:
        print("Record Not Update")

    c.commit()
UpdateRecord()