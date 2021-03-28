import sqlite3
import uuid

from Repository.DataBase import DataBase
from utilities import VehicleNumber


def create_car_user_details_table():
    conn = sqlite3.connect(DataBase.DB)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE car_user_details(
    id TEXT PRIMARY KEY,
    age INTEGER NOT NULL,
    vehicle_registration_number TEXT NOT NULL
    )""")
    conn.commit()
    conn.close()


def drop_car_user_details_table():
    conn = sqlite3.connect(DataBase.DB)
    cur = conn.cursor()
    cur.execute("""
        DROP TABLE IF EXISTS car_user_details
    """)
    conn.commit()
    conn.close()


def check_if_car_user_details_exists():
    conn = sqlite3.connect(DataBase.DB)
    cur = conn.cursor()
    cur.execute("""
        SELECT 1 FROM car_user_details
    """)
    return True


def insert_car_user_detail(_id: uuid, age: int, vrn: VehicleNumber):
    conn = sqlite3.connect(DataBase.DB)
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO car_user_details
    VALUES ('{}', '{}', '{}')
    """.format(_id, age, vrn.number))
    conn.commit()
    conn.close()
