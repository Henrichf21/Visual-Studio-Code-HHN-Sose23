import sqlite3

# def create_database():
#     con = sqlite3.connect("Visual Studio Code Lösung/Aufgabe 3 - Flask/repo/datenbank.db")
#     cur = con.cursor()
#     cur.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='system_user';""")
#     check_table = cur.fetchone()
#     if check_table is None:
#         con = sqlite3.connect("Visual Studio Code Lösung/Aufgabe 3 - Flask/repo/datenbank.db")
#         cur = con.cursor()

#         cur.execute("""CREATE TABLE customer (
#             customer_id integer PRIMARY KEY,
#             vorname varchar(255),
#             nachname varchar(255),
#             geburtstag varchar(255),
#             strasse varchar(255)

#             )""")
#         con.commit()
#         cur.close()

def insert_customer(vorname, nachname, geburtstag,strasse):
    """Adds customer to db"""
    con = sqlite3.connect("Visual Studio Code Lösung/Aufgabe 3 - Flask/repo/datenbank.db")
    cur = con.cursor()
    cur.execute("INSERT INTO customer (vorname, nachname, geburtstag,strasse) "
                "VALUES(?, ?, ?, ?)",
                (vorname, nachname, geburtstag,strasse))
    con.commit()
    cur.close()


def get_all_customer():
    """Get all customer"""
    con = sqlite3.connect("Visual Studio Code Lösung/Aufgabe 3 - Flask/repo/datenbank.db")
    cur = con.cursor()
    cur.execute("SELECT customer_id, vorname, nachname, geburtstag, strasse FROM customer")
    result = cur.fetchall()
    con.commit()
    cur.close()
    return result
