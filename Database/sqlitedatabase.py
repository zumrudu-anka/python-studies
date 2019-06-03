import sqlite3
import random
import time
import datetime

"""con = sqlite3.connect("dersler.db") #Veritabani olusturmak ve baglanmak icin

cursor = con.cursor()

def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS ogrenciler (ad TEXT,soyad TEXT, numara INT,ogrenci_not INT)")

def add_value():
    cursor.execute("INSERT INTO ogrenciler VALUES ('Yeni','Ogrenci',1919,100)")

create_table()
add_value()
con.commit()
con.close()"""

"""print(time.time())
print(datetime.datetime.now())

input("asd:")"""


con = sqlite3.connect("dersler.db")

cursor = con.cursor()

def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS tablo2(zaman REAL,tarih TEXT,anahtar_kelime TEXT,deger REAL)")
    
def add_random_value():
    zaman=time.time()
    tarih=str(datetime.datetime.fromtimestamp(zaman).strftime('%Y-%m-%d %H:%M:%S'))
    anahtar_kelime = "Python SQLite3"
    deger = random.randrange(0,10)
    cursor.execute("INSERT INTO tablo2 (zaman,tarih,anahtar_kelime,deger) VALUES(?,?,?,?)",(zaman,tarih,anahtar_kelime,deger))
    con.commit()

"""create_table()

for i in range(0,10):
    add_random_value()
    #time.sleep(1)

"""

def get_value():
    cursor.execute("SELECT * FROM tablo2 WHERE deger = 3.0")
    data = cursor.fetchall()
    for i in data:
        print(i)
    print(type(data))

#get_value()

def delete_and_update():
    cursor.execute("SELECT * FROM tablo2")
    data = cursor.fetchall()
    print("\nilk Degerler:\n")
    for i in data:
        print(i)
    """cursor.execute("UPDATE tablo2 SET deger = 99 WHERE deger = 3.0")
    con.commit()    ## Tabloya bu degerleri ekledi. Aksi halde programda kalir tabloya gitmez
    cursor.execute("SELECT * FROM tablo2")
    data=cursor.fetchall()
    print("\nGuncellendikten Sonra:\n")
    for i in data:
        print(i)"""
    cursor.execute("DELETE FROM tablo2 WHERE deger = 99.0")
    con.commit()
    cursor.execute("SELECT * FROM tablo2")
    data=cursor.fetchall()
    print("\nSilindikten Sonra:\n")
    for i in data:
        print(i)


delete_and_update()

con.close()
