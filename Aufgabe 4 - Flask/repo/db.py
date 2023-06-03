import sqlite3


def insert_customer(vorname, nachname, geburtstag,strasse):
    """Adds customer to db"""
    con = sqlite3.connect("PATH WITH / ")
    cur = con.cursor()
    cur.execute("INSERT INTO customer (vorname, nachname, geburtstag,strasse) "
                "VALUES(?, ?, ?, ?)",
                (vorname, nachname, geburtstag,strasse))
    con.commit()
    cur.close()


def get_all_customer():
    """Get all customer"""
    con = sqlite3.connect("PATH WITH / ")
    cur = con.cursor()
    cur.execute("SELECT customer_id, vorname, nachname, geburtstag, strasse FROM customer")
    result = cur.fetchall()
    con.commit()
    cur.close()
    return result
