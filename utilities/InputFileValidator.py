from utilities.Requests import Method
from SQException.squadException import SquadException, Codes


class FileValidator:
    def __init__(self, content: str):
        self.lines = content.split("\n")

    def is_valid(self):
        if self.lines[0].split(" ")[0] != Method.CreateParkingLot:
            raise SquadException(Codes.SQ_011)
