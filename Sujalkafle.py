import sqlite3

DB = "jobs.db"

def connect():
    return sqlite3.connect(DB)

def create_table():
    con = connect()
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT NOT NULL,
            role TEXT NOT NULL,
            status TEXT NOT NULL,
            date TEXT
        )
    """)

    con.commit()
    con.close()

def add_application(company, role, status, date):
    con = connect()
    cur = con.cursor()

    cur.execute("""
        INSERT INTO applications
        (company, role, status, date)
        VALUES (?, ?, ?, ?)
    """, (company, role, status, date))

    con.commit()
    con.close()

def get_applications():
    con = connect()
    cur = con.cursor()

    cur.execute("SELECT * FROM applications")
    data = cur.fetchall()

    con.close()
    return data

def search_company(company):
    con = connect()
    cur = con.cursor()

    cur.execute(
        "SELECT * FROM applications WHERE company LIKE ?",
        ("%" + company + "%",)
    )

    data = cur.fetchall()
    con.close()

    return data

def delete_application(app_id):
    con = connect()
    cur = con.cursor()

    cur.execute(
        "DELETE FROM applications WHERE id = ?",
        (app_id,)
    )

    con.commit()
    con.close()
