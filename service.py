from typing import List

import Repository
from utilities import VehicleNumber
import uuid


def create_tables():
    drop_tables()
    Repository.create_tickets_table()
    Repository.create_parking_slots_table()
    Repository.create_car_user_details_table()


def drop_tables():
    Repository.drop_tickets_table()
    Repository.drop_parking_slots_table()
    Repository.drop_car_user_details_table()


def check_if_tables_exists() -> bool:
    if not Repository.check_if_tickets_exists():
        return False
    if not Repository.check_if_parking_slots_exists():
        return False
    if not Repository.check_if_car_user_details_exists():
        return False
    return True


def create_parking_slot(number_of_slots: int):
    Repository.insert_parking_slots(n=number_of_slots)


def park_a_car(vrn: VehicleNumber, age: int) -> int:
    if not Repository.check_if_vehicle_has_ticket_active(vrn=vrn):
        return -1
    slot = Repository.get_nearest_empty_parking_slot()
    n = slot[0][0]
    Repository.update_parking_slots(n, False)
    car_user_detail_id = uuid.uuid4()
    Repository.insert_car_user_detail(_id=car_user_detail_id, age=age, vrn=vrn)
    Repository.insert_tickets(car_user_detail_id=car_user_detail_id, slot_number=n, is_active=True)
    return n


def get_slot_numbers_for_driver_of_age(age: int) -> List[str]:
    slots = Repository.get_slot_from_age(age=age)
    return [str(slot[0]) for slot in slots]


def get_slot_number_for_car_number(vrn: VehicleNumber) -> int:
    slots = Repository.get_slot_from_vn(vrn=vrn)
    if len(slots) == 0:
        return 0
    return slots[0][0]


def get_vehicle_number_from_age(age: int) -> List[str]:
    vehicle_numbers = Repository.get_vn_from_age(age=age)
    return [vehicle_number[0] for vehicle_number in vehicle_numbers]


def slot_exit(slot_number: int) -> (str, int):
    details = Repository.get_vn_and_age_details(slot_number=slot_number)
    if len(details) == 0:
        return "", 0
    vn, age = details[0][0], details[0][1]
    Repository.update_tickets_to_inactive(slot_number=slot_number)
    Repository.update_parking_slots(slot_number=slot_number, is_vacant=True)
    return vn, age
