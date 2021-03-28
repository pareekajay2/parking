import sqlite3
import uuid

from Repository.DataBase import DataBase
from utilities import VehicleNumber


def create_tickets_table():
    conn = sqlite3.connect(DataBase.DB)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE tickets(
    id TEXT PRIMARY KEY,
    car_user_detail_id TEXT NOT NULL,
    slot_number INTEGER NOT NULL,
    is_active BOOLEAN
    )""")
    conn.commit()


def drop_tickets_table():
    conn = sqlite3.connect(DataBase.DB)
    cur = conn.cursor()
    cur.execute("""
        DROP TABLE IF EXISTS tickets""")
    conn.commit()
    conn.close()


def check_if_tickets_exists():
    conn = sqlite3.connect(DataBase.DB)
    cur = conn.cursor()
    cur.execute("""
        SELECT 1 FROM tickets
    """)
    return True


def update_tickets_to_inactive(slot_number: int):
    conn = sqlite3.connect(DataBase.DB)
    cur = conn.cursor()
    cur.execute("""
        UPDATE tickets
        SET is_active = '{}'
        WHERE slot_number = '{}'
        """.format(False, slot_number))
    conn.commit()
    conn.close()


def insert_tickets(car_user_detail_id: uuid, slot_number: int, is_active: bool):
    conn = sqlite3.connect(DataBase.DB)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO tickets
        VALUES ('{}', '{}', '{}', '{}')
        """.format(uuid.uuid4(), car_user_detail_id, slot_number, is_active))
    conn.commit()
    conn.close()


def get_slot_from_age(age: int):
    conn = sqlite3.connect(DataBase.DB)
    cur = conn.cursor()
    cur.execute("""
            SELECT t.slot_number
            FROM tickets t
            INNER JOIN car_user_details cud
            ON cud.id = t.car_user_detail_id
            WHERE cud.age = '{}'
            AND t.is_active = '{}'
            """.format(age, True))
    return cur.fetchall()


def get_slot_from_vn(vrn: VehicleNumber):
    conn = sqlite3.connect(DataBase.DB)
    cur = conn.cursor()
    cur.execute("""
            SELECT t.slot_number
            FROM tickets t
            INNER JOIN car_user_details cud
            ON cud.id = t.car_user_detail_id
            WHERE cud.vehicle_registration_number = '{}'
            AND t.is_active = '{}'
            """.format(vrn.number, True))
    return cur.fetchall()


def get_vn_from_age(age: int):
    conn = sqlite3.connect(DataBase.DB)
    cur = conn.cursor()
    cur.execute("""
                SELECT cud.vehicle_registration_number
                FROM tickets t
                INNER JOIN car_user_details cud
                ON cud.id = t.car_user_detail_id
                WHERE cud.age = '{}'
                AND t.is_active = '{}'
                """.format(age, True))
    return cur.fetchall()


def get_vn_and_age_details(slot_number: int):
    conn = sqlite3.connect(DataBase.DB)
    cur = conn.cursor()
    cur.execute("""
        SELECT cud.vehicle_registration_number, cud.age
        FROM tickets t
        INNER JOIN car_user_details cud
        ON cud.id = t.car_user_detail_id
        WHERE t.slot_number = '{}'
        AND t.is_active = '{}'
    """.format(slot_number, True))
    return cur.fetchall()


def check_if_vehicle_has_ticket_active(vrn: VehicleNumber) -> bool:
    conn = sqlite3.connect(DataBase.DB)
    cur = conn.cursor()
    cur.execute("""
            SELECT t.id
            FROM tickets t
            INNER JOIN car_user_details cud
            ON cud.id = t.car_user_detail_id
            WHERE cud.vehicle_registration_number = '{}'
            AND t.is_active = '{}'
        """.format(vrn.number, True))
    if len(cur.fetchall()) > 0:
        return False
    return True
