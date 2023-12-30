"""
def Register():
    print("Please enter the following details to register;")
    N=input("Enter your name:")
    MN=int(input("Enter your mobile number:"))
    print("Your unique user ID is","uid")
    print("The above ID must be used for login in future" )

def MLogin():
    print("Please enter the following details to login;")
    ID=input("Enter your User ID :")
    MN=int(input("Enter your mobile number:"))
    print("Login Successful")

def ALogin():
    print("Please enter the following details to login;")
    ID=input("Enter your Admin ID:")
    PWD=int(input("Enter the password:"))
    if PWD=="123":
        print("Login Successful")
    else:
        print("The password entered is incorrect. Please try again.")
        ALogin()

def Menu():
    print("Welcome to XYZ Library".center(89 , '*'))
    print('1. Search for books'.center(155))
    print("\n")
    print('2. Return books'.center(155))
    print("\n")
    print('3. Check due date and fine'.center(155))
    print("\n")
    
c = 'y'
while c.lower() == 'y' :
    print("Welcome to XYZ Library".center(89 , '*'))
    print('1. Register'.center(155))
    print("\n")
    print('2. Login as member'.center(155))
    print("\n")
    print('3. Login as Admin'.center(155))
    print("\n")
    choice = int(input("Enter your choice : "))
    if choice==1:
        Register()
        continue
    elif choice==2:
        MLogin()
        Menu()
    elif choice==3:
        ALogin()
        AMenu()
    print()
    c = input("Do you want to return to main menu (y/n) : ")
else:
    print("Thank you for coming to XYZ Library, please come again ! ")
"""
"""
#if user wants to return a book,
	a) check whether return date is due or not
	b) ask fine if due date passed
	c) if not then return the book and update the database."""





"""import mysql.connector as sqltor

cobj=sqltor.connect(host="localhost" , user="root" , passwd="fiitjee@40625" , database="navacomp")


def RETURN():
    cursor1=cobj.cursor()
    mobileno=input("Enter your mobile no. ")  #Use the mobile no given during log in
    q="SELECT book_name , due_date FROM books_copy , users_copy WHERE users_copy.book_borrowed=books_copy.book_id AND users_copy.mobile_no={}".format(mobileno,)
    cursor1.execute(q)
    info=cursor1.fetchone()
    bname=info[0]
    duedate=info[1]

    cursor2=cobj.cursor()
    q2="SELECT CURDATE()"
    cursor2.execute(q2)
    info2=cursor2.fetchone()
    todate=info2[0]

    f1=10               #fine for each extra day

    if todate<duedate:
        print("The book you have borrowed",bname, "is due on",duedate)
        ch=input("Do you wish to return the book today? (y/n)")
        
        if ch=="y":
            cursor3=cobj.cursor()
            q3="UPDATE books_copy SET availability = 'Available' WHERE book_name ='{}'".format(bname,)
            cursor3.execute(q3)
            cobj.commit()
            q4="UPDATE users_copy SET book_borrowed = 'None' , due_date= NULL WHERE Mobile_no= '{}' ".format(mobileno,)
            cursor3.execute(q4)
            cobj.commit()
            print("Thank you for coming to NSSS Library. Have a great day !")
            #Go back to user menu
            
        elif ch=="n":
            print("Thank you for coming to NSSS Library. Have a great day !")
            #Go back to user menu
                       
    else:
        #Calculating the fine
        fine=str(f1*(todate-duedate))
        fine=int(fine[0:-14])
        print()
        print("The book you have borrowed",bname, "has crossed the due date",duedate)
        print()
        print("To return the book today, kindly pay the fine of",fine,"rupees to the librarian.")
    
RETURN()
"""


import mysql.connector as sqltor

cobj=sqltor.connect(host="localhost" , user="root" , passwd="fiitjee@40625" , database="navacomp")


def LEND():
    mobileno=input("Enter your mobileno :")         #Use from login info
    cursor2=cobj.cursor()
    q2="SELECT book_borrowed FROM users_copy WHERE mobile_no ='{}'".format(mobileno,)
    cursor2.execute(q2)
    info=cursor2.fetchone()
    checkpt=info[0]
    if checkpt!="None":
        print("Kindly return the book you have already borrowed in order to borrow a new book.")
         #Go to user menu

    b_id=input("Enter the book id of the book you wish to borrow :") #Get it using a query from user input
    cursor1=cobj.cursor()
    q1="SELECT book_name , availability FROM books_copy WHERE book_id ='{}'".format(b_id,)
    cursor1.execute(q1)
    info=cursor1.fetchone()
    bname=info[0]
    avail=info[1]
    
    if avail=="Available" or avail=="available":
        print("The book you have requested",bname, "is currently available.","Kindly collect your book from the librarian.")
        cursor3=cobj.cursor()
        q3="UPDATE books_copy SET availability = 'Unavailable' WHERE book_name ='{}'".format(bname,)
        cursor3.execute(q3)
        cobj.commit()
        q4="UPDATE users_copy SET book_borrowed = '{}' , due_date= DATE_ADD( CURDATE() , INTERVAL 7 DAY) WHERE Mobile_no= '{}' ".format(b_id,mobileno)
        cursor3.execute(q4)
        cobj.commit()
        print("Thank you for coming to NSSS Library. Have a great day !")
            #Go back to user menu
            
    elif avail=="Unavailable" or avail =="unavailable":
        print("Unfortunately the book ",bname,"which you have requested is unavailable currently.")
        print()
        ch=input("Would you like to find another book ? (y/n)")
            
        if ch.lower()=="y":
            LEND()
        elif ch=="n":
            print("Thank you for coming to NSSS Library. Have a great day !")
                #Go back to user menu
                       
   
LEND()



































    
    

        
