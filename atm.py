## ATM using MYSQL database.

import mysql.connector as my
from datetime import *


mydb=my.connect(host="localhost",
                user="root",
                password="",
                database="atm")
cur=mydb.cursor()


while True:
    user=input("Enter your UserName:")
    user= user.lower()
    cur.execute("select UserName from user_info where UserName='"+user+"' ")
    a= cur.fetchone()
    if cur.rowcount >0:
        print("valide")
        break
    else:
        print("invalide")


count=0
while count<3:
    if count == 2:
        print("One more wrong credantial will be block your id")
    pin= int(input("Enter Pin:"))
    z= str(pin)
    cur.execute("select UserName from user_info where UserName='"+user+"' and Pin='"+z+"'")
    b= cur.fetchone()
    if cur.rowcount>0:
        print('****************')
        print("Login successful")
       
        break
    else:
        count += 1
        print('****************')
        print("Invalide cridential")
        print()
        
        
if count == 3:
	print('-----------------------------------')
	print('3 UNSUCCESFUL PIN ATTEMPTS, EXITING')
	print('!!!YOUR CARD HAS BEEN LOCKED!!!')
	print('-----------------------------------')
	exit()
	
print(str.capitalize(user), 'welcome to ATM')
print('**************************')
print('----------ATM SYSTEM-----------')


while(True):
    
    print("1)Statement")
    print("2)Deposit Money")
    print("3)Withdraw Money")
    print("4)Change Pin")
    print("5)Exit")
    ch=int(input("Enter your choice:"))

    if(ch == 1):
        print("+--------+------+-----------------------------------")
        print("| AMOUNT |  TR  |    DATE          ")
        print("+--------+------+-----------------------------------")
        cur.execute("select amount,ttype,dot from trans where UserName='"+user+"' ")
        for i in cur:
            print (i)
        print("-----------------------------------------------------")
        cur.execute("select amount from user_info where UserName='"+user+"' ")
        a= cur.fetchone()
        print("Current Balance: ",a )
        print("-----------------------------------------------------")

        
    elif(ch == 2):
         dp=int(input("Enter amount to be deposited:"))
         dot= str(datetime.now())
         ttype="Deposit"
         cur.execute("insert into trans values('"+user+"','"+str(dp)+"','"+dot+"','"+ttype+"')")
         cur.execute("update user_info set amount=amount+'"+str(dp)+"' where UserName='"+user+"'")
         mydb.commit()
         print("money has been deposited successully!!!")

    elif(ch == 3):
          wd=int(input("Enter amount to be withdrawn:"))
          dot= str(datetime.now())
          ttype="withdraw"
          cur.execute("insert into trans values('"+user+"','"+str(wd)+"','"+dot+"','"+ttype+"')")
          cur.execute("update user_info set amount=amount-'"+str(wd)+"' where UserName='"+user+"'")
          mydb.commit()
          print("money has been Withdrawn successully!!!")
          
    elif(ch == 4):
        
            new_pin = str(input('ENTER A NEW PIN: '))
            if new_pin != b :
                print('******************')
                new_ppin = str(input('CONFIRM NEW PIN: '))
                if new_ppin != new_pin:
                    print('PIN MISMATCH')
                else:
                    c= str(new_pin)
                    cur.execute("update user_info set pin='"+c+"' where UserName='"+user+"' ")
                    mydb.commit()
                    print('NEW PIN SAVED')
        
            else:
                  print('NEW PIN MUST BE DIFFERENT TO PREVIOUS PIN')
        

    elif (ch == 5):
        exit()

    else:
            print('------------------')
            print('CHOICE NOT VALID')
            print('------------------')
            
        
			



          



















