import sqlite3
from Repository.DataBase import DataBase


def create_parking_slots_table():
    conn = sqlite3.connect(DataBase.DB)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE parking_slots(
    slot_number INTEGER NOT NULL PRIMARY KEY,
    is_vacant BOOLEAN DEFAULT TRUE
    )""")
    conn.commit()
    conn.close()


def drop_parking_slots_table():
    conn = sqlite3.connect(DataBase.DB)
    cur = conn.cursor()
    cur.execute("""
        DROP TABLE IF EXISTS parking_slots
    """)
    conn.commit()
    conn.close()


def check_if_parking_slots_exists():
    conn = sqlite3.connect(DataBase.DB)
    cur = conn.cursor()
    cur.execute("""
        SELECT 1 FROM parking_slots
    """)
    conn.close()
    return True


def update_parking_slots(slot_number: int, is_vacant: bool):
    conn = sqlite3.connect(DataBase.DB)
    cur = conn.cursor()
    cur.execute("""
        UPDATE parking_slots
        SET is_vacant = '{}'
        WHERE slot_number = '{}'
        """.format(is_vacant, slot_number))
    conn.commit()
    conn.close()


def insert_parking_slots(n: int):
    conn = sqlite3.connect(DataBase.DB)
    cur = conn.cursor()
    for i in range(n):
        cur.execute("""
        INSERT INTO parking_slots
        VALUES ('{}', '{}')
        """.format(i + 1, True))
    conn.commit()
    conn.close()


def get_nearest_empty_parking_slot():
    conn = sqlite3.connect(DataBase.DB)
    cur = conn.cursor()
    cur.execute("""
            SELECT min(slot_number) as slot_number
            FROM parking_slots
            WHERE is_vacant = '{}'
            """.format(True))
    return cur.fetchall()
