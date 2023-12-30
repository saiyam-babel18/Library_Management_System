
import mysql.connector as sqltor

cobj=sqltor.connect(host="localhost" , user="root" , passwd="pwd" , database="db")


def LEND():
    mobileno=input("Enter your mobileno :")         #Use from login info
    cursor2=cobj.cursor()
    q2="SELECT book_borrowed FROM users WHERE mobile_no ='{}'".format(mobileno,)
    cursor2.execute(q2)
    info=cursor2.fetchone()
    checkpt=info[0]
    if checkpt!="None":
        print("Kindly return the book you have already borrowed in order to borrow a new book.")
         #Go to user menu

    b_id=input("Enter the book id of the book you wish to borrow :") #Get it using a query from user input
    cursor1=cobj.cursor()
    q1="SELECT book_name , availability FROM books WHERE book_id ='{}'".format(b_id,)
    cursor1.execute(q1)
    info=cursor1.fetchone()
    bname=info[0]
    avail=info[1]
    
    if avail=="Available" or avail=="available":
        print("The book you have requested",bname, "is currently available.","Kindly collect your book from the librarian.")
        cursor3=cobj.cursor()
        q3="UPDATE books SET availability = 'Unavailable' WHERE book_name ='{}'".format(bname,)
        cursor3.execute(q3)
        cobj.commit()
        q4="UPDATE users SET book_borrowed = '{}' , due_date= DATE_ADD( CURDATE() , INTERVAL 7 DAY) WHERE Mobile_no= '{}' ".format(b_id,mobileno)
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
