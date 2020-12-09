from BL import sql_queries
from BL.api_requests_builder import OcrSpaceApi
from os import listdir
from datetime import datetime

from BL.sql_queries import ParkingDecisionDb
from BL.utils import car_verification

FAIL_FOLDER_PATH = r'resources\fail'
SUCCESS_FOLDER_PATH = r'resources\success'


def test_fails_from_file(ocr_space_api, parking_decision_db, fail):
    plate_number = ocr_space_api.post_request_get_text_from_image_file(image_path=FAIL_FOLDER_PATH + '\\' + fail)
    decision = car_verification(plate_number=plate_number)

    parking_decision_db.insert_parking_decision(plate_number=plate_number, decision=decision,
                                                log_time=datetime.now().timestamp())

    assert not decision, "Car managed to get in although it didn't fit the criteria"


def test_succeeds_from_files(ocr_space_api, parking_decision_db, success):
    plate_number = ocr_space_api.post_request_get_text_from_image_file(image_path=SUCCESS_FOLDER_PATH + '\\' + success)
    decision = car_verification(plate_number=plate_number)

    parking_decision_db.insert_parking_decision(plate_number=plate_number, decision=decision,
                                                log_time=datetime.now().timestamp())

    assert decision, "Car failed to get in although it fit the criteria"

# def test_enter():
#     plate_number = post_request_get_text_from_image_file(
#         image_path=FAIL_FOLDER_PATH + '\\' + 'unnamed.jpg')
#     car_verification(plate_number='123!@#%#^%$^ asc 435p /g/*-:')
