from os import listdir

import pytest

from BL.api_requests_builder import OcrSpaceApi
from BL.sql_queries import ParkingDecisionDb

FAIL_FOLDER_PATH = r'resources\fail'
SUCCESS_FOLDER_PATH = r'resources\success'


def get_file_names():
    fail_names = []
    pass_names = []

    for filename in listdir(FAIL_FOLDER_PATH):
        fail_names.append(filename)

    for filename in listdir(SUCCESS_FOLDER_PATH):
        pass_names.append(filename)

    return fail_names, pass_names


fail_filenames, success_filenames = get_file_names()


def pytest_generate_tests(metafunc):
    if "fail" in metafunc.fixturenames:
        metafunc.parametrize("fail", fail_filenames, ids=fail_filenames)
    elif "success" in metafunc.fixturenames:
        metafunc.parametrize("success", success_filenames, ids=success_filenames)


@pytest.fixture(scope="module")
def ocr_space_api():
    return OcrSpaceApi()


@pytest.fixture(scope="module")
def parking_decision_db():
    return ParkingDecisionDb()
