from SQException.squadException import SquadException, Codes
from utilities.CommandValidator import CommandValidator


class VehicleNumber(CommandValidator):
    def __init__(self, number: str):
        self.number = number

    def is_valid(self):
        vn = self.number.split("-")
        if len(vn) != 4:
            raise SquadException(Codes.SQ_001)
        state, region, alphabet_series, num = vn[0], vn[1], vn[2], vn[3]
        if not state.isalpha() or len(state) != 2:
            raise SquadException(Codes.SQ_002)
        if not region.isnumeric() or len(region) != 2:
            raise SquadException(Codes.SQ_003)
        if not alphabet_series.isalpha() or len(alphabet_series) != 2:
            raise SquadException(Codes.SQ_004)
        if not num.isnumeric() or len(num) != 4:
            raise SquadException(Codes.SQ_005)
