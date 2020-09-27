import psycopg2
def create():
    conn=psycopg2.connect(dbname="postgres", user="postgres",password="", host="localhost", port="5432" )
    cur=conn.cursor()
    cur.execute('''create table student(id serial,name text,age text,address text );s''')
    print("table created")
    conn.commit()
    conn.close()

def insert_data():
    conn=psycopg2.connect(dbname="postgres", user="postgres",password="", host="localhost", port="5432" )
    cur=conn.cursor()
    name=input("Enter Name")
    age=input("Enter Age")
    address=input("Enter Address")
    query='''insert into student(name,age,address) values(%s,%s,%s);'''

    cur.execute(query,(name,age,address))
    print("table created")
    conn.commit()
    conn.close()

insert_data()