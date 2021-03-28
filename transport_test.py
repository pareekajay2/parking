import unittest
from Repository.DataBase import DataBase
import transport
from SQException import SquadException
import service
from utilities import Response


class MyTestCase(unittest.TestCase):
    temp_db = "file_utilities/temp-db.db"
    DataBase.DB = temp_db

    def test_create_parking_lot_1(self):
        with self.assertRaises(SquadException):
            transport.create_parking_lot(" ", True)
        service.drop_tables()

    def test_create_parking_lot_2(self):
        text1 = "Create_parking_lot a"
        with self.assertRaises(SquadException):
            transport.create_parking_lot(text1.split(" "), False)
        service.drop_tables()

    def test_create_parking_lot_3(self):
        text1 = "Create_parking_lot 6"
        t, response = transport.create_parking_lot(text1.split(" "), False)
        self.assertTrue(t)
        self.assertEqual(Response.CreateParkingLot.format(text1.split(" ")[1]), response)
        service.drop_tables()

    def test_parking_a_car(self):
        text1 = "Create_parking_lot 6"
        text2 = "Park K-1 driver_age 20"
        text3 = "Park A1-11-BB-2222 driver_age 20"
        text4 = "Park AA-1a-BB-2222 driver_age 20"
        text5 = "Park AA-11-B1-2222 driver_age 20"
        text6 = "Park AA-11-BB-222a driver_age 20"
        text7 = "Park AA-11-BB-2222 driver_aga 20"
        text8 = "Park AA-11-BB-2222 driver_age 2a"
        text9 = "Park AA-11-BB-2222 driver_age 0"
        text10 = "Park AA-11-BB-2222 driver_age 20"
        text11 = "Park AA-11-BB-2223 driver_age 20"
        text12 = "Park AA-11-BB-2224 driver_age 20"
        text13 = "Park AA-11-BB-2225 driver_age 20"
        text14 = "Park AA-11-BB-2226 driver_age 20"
        text15 = "Park AA-11-BB-2227 driver_age 20"
        text16 = "Park AA-11-BB-2228 driver_age 20"
        t, res1 = transport.create_parking_lot(text1.split(" "), False)
        with self.assertRaises(SquadException):
            transport.parking_a_car(text2.split(" "))
        with self.assertRaises(SquadException):
            transport.parking_a_car(text3.split(" "))
        with self.assertRaises(SquadException):
            transport.parking_a_car(text4.split(" "))
        with self.assertRaises(SquadException):
            transport.parking_a_car(text5.split(" "))
        with self.assertRaises(SquadException):
            transport.parking_a_car(text6.split(" "))
        with self.assertRaises(SquadException):
            transport.parking_a_car(text7.split(" "))
        with self.assertRaises(SquadException):
            transport.parking_a_car(text8.split(" "))
        with self.assertRaises(SquadException):
            transport.parking_a_car(text9.split(" "))
        res2 = transport.parking_a_car(text10.split(" "))
        self.assertEqual(Response.CarParkingResponse.format(text10.split(" ")[1], 1), res2)
        res3 = transport.parking_a_car(text10.split(" "))
        self.assertEqual(Response.TicketActiveResponse.format(text10.split(" ")[1]), res3)
        res4 = transport.parking_a_car(text11.split(" "))
        res5 = transport.parking_a_car(text12.split(" "))
        res6 = transport.parking_a_car(text13.split(" "))
        res7 = transport.parking_a_car(text14.split(" "))
        res8 = transport.parking_a_car(text15.split(" "))
        res9 = transport.parking_a_car(text16.split(" "))
        self.assertEqual(Response.ParkingLotFull, res9)
        service.drop_tables()

    def test_get_slot_numbers_with_driver_age(self):
        text1 = "Create_parking_lot 6"
        text2 = "Park AA-11-BB-2222 driver_age 20"
        text3 = "Park AA-11-BB-2223 driver_age 20"
        text4 = "Slot_numbers_for_driver_of_age 2a"
        text5 = "Slot_numbers_for_driver_of_age 22"
        text6 = "Slot_numbers_for_driver_of_age 20"
        t, res1 = transport.create_parking_lot(text1.split(" "), False)
        res2 = transport.parking_a_car(text2.split(" "))
        res3 = transport.parking_a_car(text3.split(" "))
        with self.assertRaises(SquadException):
            transport.get_slot_numbers_with_driver_age(text4.split(" "))
        res5 = transport.get_slot_numbers_with_driver_age(text5.split(" "))
        self.assertEqual([], res5)
        res6 = transport.get_slot_numbers_with_driver_age(text6.split(" "))
        self.assertEqual(['1', '2'], res6)
        service.drop_tables()

    def test_get_slot_number_with_vehicle_number(self):
        text1 = "Create_parking_lot 6"
        text2 = "Park AA-11-BB-2222 driver_age 20"
        text3 = "Slot_number_for_car_with_number AA-11-BB-2223"
        text4 = "Slot_number_for_car_with_number AA-11-BB-2222"
        text5 = "Slot_number_for_car_with_number A-111-BB-2222"
        text6 = "Slot_number_for_car_with_number AA-1-BBB-2222"
        text7 = "Slot_number_for_car_with_number AA-11-B-22222"
        text8 = "Slot_number_for_car_with_number AA-11-BB-222"
        t, res1 = transport.create_parking_lot(text1.split(" "), False)
        res2 = transport.parking_a_car(text2.split(" "))
        res3 = transport.get_slot_number_with_vehicle_number(text3.split(" "))
        self.assertEqual(Response.VehicleNotInParkingLot.format(text3.split(" ")[1]), res3)
        res4 = transport.get_slot_number_with_vehicle_number(text4.split(" "))
        self.assertEqual(1, res4)
        with self.assertRaises(SquadException):
            transport.get_slot_number_with_vehicle_number(text5.split(" "))
        with self.assertRaises(SquadException):
            transport.get_slot_number_with_vehicle_number(text6.split(" "))
        with self.assertRaises(SquadException):
            transport.get_slot_number_with_vehicle_number(text7.split(" "))
        with self.assertRaises(SquadException):
            transport.get_slot_number_with_vehicle_number(text8.split(" "))
        service.drop_tables()

    def test_get_vehicle_number_for_driver_age(self):
        text1 = "Create_parking_lot 6"
        text2 = "Park AA-11-BB-2222 driver_age 20"
        text3 = "Vehicle_registration_number_for_driver_of_age 18"
        text4 = "Vehicle_registration_number_for_driver_of_age 20"
        text5 = "Vehicle_registration_number_for_driver_of_age 20a"
        t, res1 = transport.create_parking_lot(text1.split(" "), False)
        res2 = transport.parking_a_car(text2.split(" "))
        res3 = transport.get_vehicle_number_for_driver_age(text3.split(" "))
        self.assertEqual([], res3)
        res4 = transport.get_vehicle_number_for_driver_age(text4.split(" "))
        self.assertEqual(['AA-11-BB-2222'], res4)
        with self.assertRaises(SquadException):
            transport.get_slot_numbers_with_driver_age(text5.split(" "))
        service.drop_tables()

    def test_leave(self):
        text1 = "Create_parking_lot 6"
        text2 = "Park AA-11-BB-2222 driver_age 20"
        text3 = "Leave a"
        text4 = "Leave 0"
        text5 = "Leave 2"
        text6 = "Leave 1"
        t, res1 = transport.create_parking_lot(text1.split(" "), False)
        res2 = transport.parking_a_car(text2.split(" "))
        with self.assertRaises(SquadException):
            transport.leave_slot(text3.split(" "))
        with self.assertRaises(SquadException):
            transport.leave_slot(text4.split(" "))
        self.assertEqual(Response.SlotAlreadyVacant, transport.leave_slot(text5.split(" ")))
        res6 = transport.leave_slot(text6.split(" "))
        self.assertEqual(Response.LeaveResponse.format(1, "AA-11-BB-2222", 20), res6)



if __name__ == '__main__':
    unittest.main()
