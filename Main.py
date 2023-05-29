import mysql.connector as m

def connection():
    database = m.connect(host = "localhost",user='root',password = 'Yashu2dec10#')
    cur = database.cursor()
    cur.execute('create database  if not exists vita2023')
    cur.execute('use vita2023')
    cur.execute('create table if not exists students (std_id int unique key not null,name varchar(20) not null,course varchar(20) not null,passout_year year,internal_marks int not null,CCEE int not null,overall_marks Float )')
    database.commit()
    database.close()

def enter_rec():
    database = m.connect(host='localhost',user = 'root',password = 'Yashu2dec10#',database ='vita2023' )
    cur = database.cursor()
    n = int(input("how many students records you want to insert ::"))
 
    for i in range(n):
        a = int(input("enter Indivisual id of student::"))
        b = input("enter a name::")
        c = input("enter a course name (dac/dbda)::")
        d = int(input("enter a passout Year::"))
        e = int(input("enter Internal marks::"))
        f = int(input("enter CCEE  marks::"))
        g = (e+f)/2
        print(f"overall_avg ::{g}%")
        cur.execute("insert into students values (%s, %s, %s, %s, %s, %s,%s )",(a,b,c,d,e,f,g))
        
        database.commit()
    database.close()    
    #print("your data is saved successfully")

def search_rec():
    database = m.connect(host='localhost',user = 'root',password = 'Yashu2dec10#',database ='vita2023' )
    cur = database.cursor()
    c = input("if you want to search by id press 'i' or by passout_year press 'b' ::-> ")
    while c =='i':
        n = int(input("enter a id to search::->"))
        cur.execute("select * from students where std_id = %s",(n,))
        row = cur.fetchall()
        for i in row:
            for j in i:
                print(j,end="|")
            print()
        c = (input("want to continue press i else press n::->"))
        if c=='n':
            break 
        database.commit()       
    while c =='b':
        n = int(input("enter a year to search (YYYY)::->"))
        cur.execute("select * from students where passout_year = %s",(n,))
        row = cur.fetchall()
        for i in row:
            for j in i:
                print(j,end="|")
            print()
        c = (input("want to continue press 'b' else 'n'::->"))
        if c=='n':
            break 
        database.commit()
    database.close()        
def update_rec():
    database = m.connect(host='localhost',user = 'root',password='Yashu2dec10#',database = 'vita2023')
    cur = database.cursor()
    c = input("if you want to add internal_marks press 'a' or minus press 'm' ::-> ")
    while c=='a':
        m1 =int(input("enter marks to add::->"))
        id1 = int(input("enter std_id for updation of marks::->")) 
        
        cur.execute("update students set internal_marks=internal_marks+%s where std_id=%s",(m1,id1))
        database.commit()    
        cur.execute("select internal_marks from students where std_id=%s",(id1,))
        i = cur.fetchone()
        internal = i[0]
        cur.execute("select CCEE from students where std_id=%s",(id1,))
        w = cur.fetchone()
        ccee = w[0]
        avg =internal+ccee
        avg1= avg/2
        cur.execute("update students set overall_marks=%s where std_id=%s",(avg1,id1))
        database.commit()
        cur.execute("select * from students")
        rows = cur.fetchall()
        for i in rows:
            for j in i:
                print(j,end="|")
            print()

        c = input("want to continue update press 'a' else press 'n'::->")
        if c=='n':
            break 
        database.commit()   
    while c=='m':
        m1 =int(input("enter marks to minus::->"))
        id1 = int(input("enter std_id for minus  marks::->")) 
        
        cur.execute("update students set internal_marks=internal_marks-%s where std_id=%s",(m1,id1))
        database.commit()    
        cur.execute("select internal_marks from students where std_id=%s",(id1,))
        i = cur.fetchone()
        internal = i[0]
        #print(internal)
        cur.execute("select CCEE from students where std_id=%s",(id1,))
        w = cur.fetchone()
        ccee = w[0]
        #print(ccee)
        avg =internal+ccee
        avg1= avg/2
        cur.execute("update students set overall_marks=%s where std_id=%s",(avg1,id1))
        database.commit()
        cur.execute("select * from students")
        rows = cur.fetchall()
        for i in rows:
            for j in i:
                print(j,end="|")
            print()

        c = input("want to continue update press 'm' else press 'n'::->")
        if c=='n':
            break  
        database.commit()
    database.close()    
def delete():    
    database = m.connect(host='localhost',user = 'root',password='Yashu2dec10#',database = 'vita2023')
    cur = database.cursor()
    c= 'd'
    while c =='d':
        n = int(input("enter a std_id to delete record::->"))
        cur.execute("delete from students where std_id = %s",(n,))
        database.commit()
        cur.execute("select * from students")
        rows = cur.fetchall()
        for i in rows:
            for j in i:
                print(j,end="|")
            print()
        database.commit()    
        c = input("want to continue delete press d else press n::->")
        if c=='n':
          break 
    database.close()
def display():
    database = m.connect(host='localhost',user='root',password='Yashu2dec10#',database='vita2023')
    cur = database.cursor()
    cur.execute("select * from students")
    rows = cur.fetchall()
    for i in rows:
        for j in i:
            print(j,end="|")
        print()
        
    
        
    database.commit()
    database.close()
connection()
c = 'y'

while c=='y':
    print("1. Insert Record Of Students::->")
    print("2. Search Record Of Students::->")
    print("3. Update Marks  Of Students::->")
    print("4. Delete Record Of Students::->")
    print("5. display Record Of Students::->")
    choice = int(input('enter a choice::->'))
    if choice==1:
        enter_rec()
    elif choice==2:
        search_rec()
    elif choice==3:
        update_rec()
    elif choice==4:
        delete()
    elif choice==5:
        display()
    c = input("want to continue to main menu press y else press n::->")
    if c=='n':
        break    
        







                       