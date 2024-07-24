"""
#if user wants to return a book,
	a) check whether return temp[9:11] is due or not
	b) ask fine if due date passed
	c) if not then return the book and update the database."""

import mysql.connector as sqltor

cobj=sqltor.connect(host="localhost" , user="root" , passwd="fiitjee@40625" , database="navacomp")


def RETURN():
    cursor1=cobj.cursor()
    mobileno=input("Enter your mobile no. ")  #Use the mobile no given during log in
    q="SELECT book_name , due_date FROM books , users WHERE users.book_borrowed=books.book_id AND users.mobile_no={}".format(mobileno,)
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

    if todate<duetemp[9:11]:
        print("The book you have borrowed",bname, "is due on",duedate)
        ch=input("Do you wish to return the book today? (y/n)")
        
        if ch=="y":
            cursor3=cobj.cursor()
            q3="UPDATE books SET availability = 'Available' WHERE book_name ='{}'".format(bname,)
            cursor3.execute(q3)
            cobj.commit()
            q4="UPDATE users SET book_borrowed = 'None' , due_date= NULL WHERE Mobile_no= '{}' ".format(mobileno,)
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
        #Go back to user menu
    
RETURN()
    
