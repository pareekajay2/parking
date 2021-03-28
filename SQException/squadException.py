class Codes:
    SQ_001 = "SQ_001"
    SQ_002 = "SQ_002"
    SQ_003 = "SQ_003"
    SQ_004 = "SQ_004"
    SQ_005 = "SQ_005"
    SQ_006 = "SQ_006"
    SQ_007 = "SQ_007"
    SQ_008 = "SQ_008"
    SQ_009 = "SQ_009"
    SQ_010 = "SQ_010"
    SQ_011 = "SQ_011"
    SQ_012 = "SQ_012"
    SQ_999 = "SQ_999"


class ExceptionCodes:
    SQ_001 = "IncorrectVehicleRegistrationNumberError"
    SQ_002 = "IncorrectStateIdError"
    SQ_003 = "IncorrectRegionIdError"
    SQ_004 = "IncorrectAlphabetSeriesError"
    SQ_005 = "IncorrectVehicleNumberError"
    SQ_006 = "IncorrectParkingNumberError"
    SQ_007 = "InternalServiceError"
    SQ_008 = "IncorrectAgeError"
    SQ_009 = "IncorrectSlotNumberError"
    SQ_010 = "Slot already vacant"
    SQ_011 = "IncorrectFirstCommandError"
    SQ_012 = "ParkingLotAlreadyExistsError"


class SquadException(Exception):
    def __init__(self, code: str):
        self.code = code

    def exception_statement(self) -> str:
        return getattr(ExceptionCodes, self.code) if hasattr(ExceptionCodes, self.code) else "Unknown Command"
