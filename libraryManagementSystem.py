import mysql.connector as a
con = a.connect(host='localhost',port='3306',user='root',password='root',database='library',auth_plugin = 'caching_sha2_password')

def addbook():
    bname = input('Enter Book Name:')
    bcode = input('Enter Book Code:')
    total = int(input('Total books:'))
    subject = input('Enter subject:')
    query = "insert into books values('{}','{}',{},'{}')".format(bname,bcode,total,subject)
    c = con.cursor()
    c.execute(query)
    con.commit()
    print('------------------------------------------------------------------------------------')
    print('Book added successfully!!!!')
    main()

def issueb():
    name = input("Enter the student name:")
    regno = input("Enter the student register number:")
    bcode = input("Enter the book code:")
    issue = input("Enter the issue date:")
    query = "insert into issue values('{}','{}',{},'{}')".format(name,regno,bcode,issue)
    c = con.cursor()
    c.execute(query)
    con.commit()
    print("-----------------------------------------------------------------------------------")
    print('Book issued to '+name)
    bookup(bcode,-1)

def submitb():
    name = input("Enter the student name:")
    regno = input("Enter the student register number:")
    bcode = input("Enter the book code:")
    query = "insert into submit values('{}','{}','{}')".format(name,regno,bcode)
    c = con.cursor()
    c.execute(query)
    con.commit()
    print("-----------------------------------------------------------------------------------")
    print('Book submitted from '+name)
    bookup(bcode,1)

def bookup(bcode,no):
    query1 = "select total from books where bcode = '{}'".format(bcode)
    c = con.cursor()
    c.execute(query1)
    result = c.fetchone()
    temp = result[0]+no
    query2 = "update books set total = {} where bcode = '{}'".format(temp,bcode)
    c.execute(query2)
    con.commit()
    main()


def dbook():
    bcode = input('Enter the book code:')
    query = "delete from books where bcode = '{}'".format(bcode)
    c = con.cursor()
    c.execute(query)
    con.commit()
    main()


def dispbook():
    records = 'select * from books'
    c = con.cursor()
    c.execute(records)
    result = c.fetchall()
    for item in result:
        print("Book Name:" ,item[0])
        print('Book Code:',item[1])
        print('Total:',item[2])
        print('-----------------------------------')
    main()


def main():
    print(
        '''                     Library Manager
        1.Add Book
        2.Issue Book
        3.Submit Book
        4.Delete Book
        5.Display Books
        6.exit
        '''
    )
    choice = input('Enter the task number:')
    print('-----------------------------------------------------------------------------------')
    if choice == '1':
        addbook()
    elif choice == '2':
        issueb()
    elif choice == '3':
        submitb()
    elif choice == '4':
        dbook()
    elif choice == '5':
        dispbook()
    elif choice == '6':
        exit()
    else:
        print('Wrong choice........')
        main()

def pswd():
    ps = input("Enter Password:")
    if ps == 'python':
        main()
    else:
        print('wrong password')
        pswd()

pswd()


