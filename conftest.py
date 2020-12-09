from os import listdir

import pytest

import config
from BL.car_checker import ParkingCarChecker


def get_file_paths():
    fail_paths = []
    pass_paths = []

    for filename in listdir(config.FAIL_FOLDER_PATH):
        fail_paths.append(config.FAIL_FOLDER_PATH + '\\' + filename)

    for filename in listdir(config.SUCCESS_FOLDER_PATH):
        pass_paths.append(config.SUCCESS_FOLDER_PATH + '\\' + filename)

    return fail_paths, pass_paths


fail_filenames, success_filenames = get_file_paths()


def pytest_generate_tests(metafunc):
    if "fail_file_paths" in metafunc.fixturenames:
        metafunc.parametrize("fail_file_paths", fail_filenames, ids=fail_filenames)
    elif "success_file_paths" in metafunc.fixturenames:
        metafunc.parametrize("success_file_paths", success_filenames, ids=success_filenames)


@pytest.fixture(scope="module")
def car_checker():
    return ParkingCarChecker()
