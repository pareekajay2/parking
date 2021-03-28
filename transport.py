import sqlite3
from typing import List
from utilities import *
from SQException.squadException import SquadException, Codes
import service


def process_command(commands: List[str]):
    service.drop_tables()
    parking_lot = False
    for command in commands:
        request = command.split(" ")
        length_of_request = len(request)
        try:
            if request[0] == Method.CreateParkingLot and length_of_request == 2:
                parking_lot, response = create_parking_lot(request, parking_lot)
                print(response)

            elif request[0] == Method.Parking and length_of_request == 4:
                print(parking_a_car(request))

            elif request[0] == Method.SlotNumbersForDriverOfAge and length_of_request == 2:
                print(", ".join(get_slot_numbers_with_driver_age(request)))

            elif request[0] == Method.SlotNumberForCarWithNumber and length_of_request == 2:
                print(get_slot_number_with_vehicle_number(request))

            elif request[0] == Method.VehicleRegistrationNumberForDriverAge and length_of_request == 2:
                print(", ".join(get_vehicle_number_for_driver_age(request)))

            elif request[0] == Method.Leave and length_of_request == 2:
                print(leave_slot(request))
            else:
                print(SquadException(Codes.SQ_999).exception_statement())

        except SquadException as e:
            print(e.exception_statement())


def leave_slot(request):
    try:
        slot_number = int(request[1])
        if slot_number < 1:
            raise SquadException(Codes.SQ_009)

        vn, age = service.slot_exit(slot_number=slot_number)
        if vn == "" or age == 0:
            return Response.SlotAlreadyVacant

        return Response.LeaveResponse.format(slot_number, vn, age)
    except ValueError:
        raise SquadException(Codes.SQ_009)
    except sqlite3.OperationalError:
        raise SquadException(Codes.SQ_007)


def get_vehicle_number_for_driver_age(request):
    try:
        age = int(request[1])
        return service.get_vehicle_number_from_age(age=age)
    except ValueError:
        raise SquadException(Codes.SQ_008)
    except sqlite3.OperationalError:
        raise SquadException(Codes.SQ_007)


def get_slot_number_with_vehicle_number(request):
    try:
        vrn = VehicleNumber(request[1])
        vrn.is_valid()
        slot = service.get_slot_number_for_car_number(vrn=vrn)
        if slot == 0:
            return Response.VehicleNotInParkingLot.format(vrn.number)
        return slot
    except sqlite3.OperationalError:
        raise SquadException(Codes.SQ_007)


def get_slot_numbers_with_driver_age(request) -> List[str]:
    try:
        age = int(request[1])
        return service.get_slot_numbers_for_driver_of_age(age=age)
    except ValueError:
        raise SquadException(Codes.SQ_008)
    except sqlite3.OperationalError:
        raise SquadException(Codes.SQ_007)


def parking_a_car(request) -> str:
    try:
        vrn = VehicleNumber(request[1])
        vrn.is_valid()
        if request[2] != Variables.DriverAge:
            raise SquadException(Codes.SQ_999)
        age = int(request[3])
        if age < 1:
            raise ValueError
        n = service.park_a_car(vrn=vrn, age=age)
        if n is None:
            return Response.ParkingLotFull
        elif n == -1:
            return Response.TicketActiveResponse.format(vrn.number)
        else:
            return Response.CarParkingResponse.format(vrn.number, n)

    except ValueError:
        raise SquadException(Codes.SQ_008)
    except sqlite3.OperationalError:
        raise SquadException(Codes.SQ_007)


def create_parking_lot(request, parking_lot) -> (bool, str):
    try:
        if not parking_lot:
            parking_lot = True
        else:
            raise SquadException(Codes.SQ_012)
        service.create_tables()
        number_of_slots = int(request[1])
        if number_of_slots <= 0:
            raise SquadException(Codes.SQ_006)

        service.create_parking_slot(number_of_slots=number_of_slots)
        return parking_lot, Response.CreateParkingLot.format(number_of_slots)

    except ValueError:
        raise SquadException(Codes.SQ_006)
    except sqlite3.OperationalError:
        raise SquadException(Codes.SQ_007)
