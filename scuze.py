import sqlite3
import random

def adauga_scuze ():
    conn = sqlite3.connect('scuze.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS scuze(
        id INTEGER PRIMARY KEY AUTOINCREMENT ,
        scuze_text TEXT NOT NULL
    )''')
    scuza_noua = input("Introdu scuza ta: ")
    cursor.execute('INSERT INTO scuze (scuze_text) VALUES (?)' , (scuza_noua,))
    conn.commit()
    print("Scuza ta a fost adaougata cu succes in DB.")
    conn.close

def generaza_scuza():
    conn = sqlite3.connect('scuze.db')
    cursor = conn.cursor()
    cursor.execute('SELECT scuze_text FROM scuze')
    scuze = cursor.fetchall()
    if scuze:
        scuza_aleasa = random.choice(scuze) [0]
        print(f"Scuza ta este {scuza_aleasa}")
    else:
        print("Nu exista scuza in DB.")
    conn.close

def stergere_scuza():
    conn = sqlite3.connect('scuze.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM scuze')
    scuze = cursor.fetchall()
    print("Scuzele existente in DB sunt: ")
    for i in scuze:
        print(f"ID: {i[0]}; TEXT: {i[1]}")
    id_scuza_de_sters = input("Introdu id-ul scuzei pe care vrei sa o stergi: ")
    cursor.execute('DELETE FROM scuze WHERE id=?', (id_scuza_de_sters,))
    conn.commit()
    print("Scuza ta a fost streasa cu succes din DB.")
    conn.close

def afisare_scuze():
    conn = sqlite3.connect('scuze.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM scuze')
    scuze = cursor.fetchall()
    print("Scuzele existente in DB sunt: ")
    for i in scuze:
        print(f"{i[0]}:{i[1]}")
    conn.close()

def update_scuza():
    conn = sqlite3.connect('scuze.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM scuze')
    scuze = cursor.fetchall()

    if not scuze:
        print("Nu există scuze în baza de date.")
        conn.close()
        return

    print("Scuzele existente în DB sunt:")
    for i in scuze:
        print(f"ID: {i[0]} | TEXT: {i[1]}")

    try:
        id_scuza = int(input("Introdu ID-ul scuzei pe care vrei să o actualizezi: "))
        cursor.execute('SELECT * FROM scuze WHERE id = ?', (id_scuza,))
        scuza_existenta = cursor.fetchone()

        if not scuza_existenta:
            print(f"Scuza cu ID-ul {id_scuza} nu există.")
        else:
            scuza_noua = input("Introdu textul actualizat pentru această scuză: ")
            cursor.execute('UPDATE scuze SET scuze_text = ? WHERE id = ?', (scuza_noua, id_scuza))
            conn.commit()
            print("Scuza a fost actualizată cu succes.")
    except ValueError:
        print("Te rog introdu un ID valid.")
    finally:
        conn.close()


#adauga_scuze()
#generaza_scuza()
#stergere_scuza()
#afisare_scuze()
update_scuza()
