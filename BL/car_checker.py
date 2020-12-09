import base64
import re
from datetime import datetime

from BL.api_requests_builder import OcrSpaceApi
from BL.sql_queries import ParkingDecisionDb
from exceptions import LicenseIdentifyingError

public_transportation = ['6', 'G']
military_and_law_enforcement = ['L', 'M']


class ParkingCarChecker:
    def __init__(self):
        self.clean_plate_number = None
        self.decision = None

    def check_car(self, image_path: str):
        ocr_space_api = OcrSpaceApi()
        parking_log_db = ParkingDecisionDb()

        image_text = ocr_space_api.get_text_from_image_file(image_path=image_path)
        self.clean_plate_number = self.find_plate_line(lines=image_text)
        self.decision = self.car_verification(plate_number=self.clean_plate_number)
        parking_log_db.insert_parking_decision(plate_number=self.clean_plate_number, decision=self.decision,
                                               log_time=datetime.now().timestamp())

    @staticmethod
    def find_plate_line(lines: list):
        lines.sort(key=lambda x: x['Words'][0]['Height'], reverse=True)
        plate_number_with_special_chars = lines[0]['LineText']
        clean_plate_number = re.sub('[^A-Za-z0-9]+', '', plate_number_with_special_chars)

        if clean_plate_number.isupper() or clean_plate_number.isnumeric():
            return clean_plate_number

        raise LicenseIdentifyingError('License plate was not found.')

    @staticmethod
    def car_verification(plate_number: str):
        for let in public_transportation:
            if plate_number.endswith(let):
                return False

        for let in military_and_law_enforcement:
            if let in plate_number:
                return False

        if plate_number.isnumeric():
            return False

        return True
