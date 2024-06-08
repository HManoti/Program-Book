import pymysql as sql
c=sql.connect(host="localhost",user="root",password="hitiksha",database="hitiksha_demo")   #password mysql
con=c.cursor()

def AddRecord():
    id=int(input("Enter id:"))
    n=input("Enter NAme:")
    p=input("Enter password:")
    city=input("Enter city:")

    q="insert into login values('%d','%s','%s','%s')"%(id,n,p,city)
    r=con.execute(q)
    if(r>0):
        print("Record insert")
    else:
        print("Record not insert")
    c.commit()

AddRecord()
