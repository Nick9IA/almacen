import sqlite3

def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, barcode integer, number integer, brand text, color text, location text, price integer,entry integer, expire integer)")
    conn.commit()
    conn.close()
    
def insert(barcode,number,brand,color,location,price,entry,expire):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?,?,?,?,?)",(barcode,number,brand,color,location,price,entry,expire))
    conn.commit()
    conn.close()

def  view():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows
        
def search(barcode="",number="",brand="",color="",location="",price="",entry="",expire=""):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE barcode=? OR number=? OR brand=? OR color=? OR location=? OR price=? OR entry=? OR expire=?",(barcode,number,brand,color,location,price,entry,expire))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,barcode,number,brand,color,location,price,entry,expire):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET barcode=?,number=?,brand=?,color=?,location=?,price=?,entry=?,expire=? WHERE id=?",(barcode,number,brand,color,location,price,entry,expire,id))
    conn.commit()
    conn.close()
            
connect()    
#insert(123132,12,"coco","blue","A1",12,2020,2222)
#print(view())