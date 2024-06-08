import mysql.connector as sql
import datetime

# Functions


# customer( ) for making bill

def customer( ):
    it=0
    bill=0
    while True:
        print("=============================================================================================")
        a=("select product_name,cost_per_product from stock where product_no =%s")
        b=input('product number: ')
        c1.execute(a,b)
        data=c1.fetchall()
        data1=list(data[0])
        print('product name :', data1[0])
        print('cost of the product :', data1[1] )
        appr=input('do you want to buy it (Y/N) :')
        if appr == 'y' or appr =='Y':
            a1=("update stock set stock = stock-1 where product_no=%s")
            c1.execute(a1,b)
            a2=("update stock set purchased = purchased+1 where product_no=%s")
            c1.execute(a2,b)
            bill+=int(data1[1])
            it+=1
            print("bought successfully!!!!")
            opn = input(" Do you want buy any other thing (Y/N):")
            if opn == 'n' or opn =='N':
                break
        elif appr=='N' or appr=='n':
            opn = input(" Do you want buy any other thing (Y/N) :")
            if opn=='n' or opn=='N':
                break
    just=input('MODE OF PAYMENT (Cash/Card):')
    print(' BILL')
    print(''' GAME POINT NUMBER OF ITEMS PURCHASED:''',it)
    print('''GRAND TOTAL AMOUNT:''',bill)
    print('''MODE OF PAYMENT:''',just)
    print('''**THANK YOU****PLEASE VISIT AGAIN**''')
    conn.commit()

    
#view_stock( ) for seeing all products of table stock

def view_stock( ):
    val3=input('Enter the product number :')
    a3=("select * from stock where product_no=%s")
    c1.execute(a3,val3)
    dt=c1.fetchall()
    dt1=list(dt[0])
    print("product name :",dt1[1])
    print("cost per product:",dt1[2])
    print("stock available:",dt1[3])
    print(" Number items purchased :",dt1[4])
    
# add_stock( ) for increasing the stock in table stock

def add_stock( ):
    prdno=int(input("Enter the product number of the productfor which the stock is going to be updated:"))
    upd_value=int(input("enter the number of new stocks came:"))
    a4=("update stock set stock=stock+%s where product_no=%s")
    val4=(upd_value,prdno)
    c1.execute(a4,val4)
    conn.commit()

# anp( ) for adding new product in table stock

def anp( ):
    pno1=input('Enter the product number of new product:')
    pna=input('Enter the product name of the new product:')
    cst=input('Enter the cost of the product:')
    stock12=input('Enter the number of stocks of the new product arrived:')
    pch='0'
    a2=("insert into stock values(%s,%s,%s,%s,%s)")
    val2=(pno1,pna,cst,stock12,pch)
    c1.execute(a2,val2)
    print("Added sucessfully!!!!!!!")
    conn.commit()
    
# admin( ) for maintaining the stock 

def admin( ):
    print("1. veiw stock")
    print("2. add stock")
    print("3. Adding a new product")
    ch=int(input("Enter your choice :"))
    if ch==1:
        view_stock( )
    elif ch==2:
        add_stock( )
    elif ch==3:
        anp( )
    else:
         print('#### INVALID OPTION ####')



#Driver Code

conn= sql.connect(host="localhost",user="root",passwd="ishan",db="sms")
c1=conn.cursor()
c1.execute('use sms')

# table stock will have data of all products
c1.execute("create table stock (product_no int(10) primary key,product_name varchar(30),cost_per_productint(10),stock int(10),purchased int(10) );")

#table user will have data of all users
c1.execute("create table user(username varchar(255),passwd int(255));")

d_day=datetime.date.today()
d_time=datetime.datetime.now()
print(d_day.day,"/",d_day.month,"/",d_day.year,"",d_time.hour,":",d_time.minute,)
print("SALES MANAGEMENT SYSTEM")
while True:
    print("1.LOGIN")
    print("2. ADMIN")
    print("3.REGISTER")
    print("4.EXIT")
    choice=int(input('ENTER THE CHOICE:'))
    print("============================================================================")
    if choice==1:
        # there will be verification of user by cross checking the data from user table
        us=input('USERNAME:')
        ps=input('PASSWORD:')
        result=c1.execute("select * from user;")
        for d in result:
            rec=list(d)
            if rec[0]==us and rec[1]==ps:
                print('''+--------------------------+////////////////////////////////////////////////// welcome to SUPERMARKET ///////////////////////////////////////////////+--------------------------+''')
                while True:
                    print("===========================================================================================")
                    print("1. CUSTOMER")
                    print("2.EXIT")
                    loggin=int(input('enter the choice:'))
                    if loggin==1:
                        customer( )
                    elif loggin==2:
                        print("...QUITING...")
                        break
                    else:
                        print("###INVALID OPTION####")
        else:
            print('''..SORRY.. WRONG.......USERNAME OR PASSWORD''')
    elif choice==2:
        admin( )
    elif choice==3:
        # for adding new data of the user
        us1=input('USERNAME:')
        ps1=input('PASSWORD:')
        s="Insert Into user values(%s,%s)"
        val=(us1,ps1)
        c1.execute(s,val)
        print("Registeration is completed")
        conn.commit( )
    elif choice ==4:
        print(".......................LOGGING...........OUT................")
        break
    else: print('please enter the right option')