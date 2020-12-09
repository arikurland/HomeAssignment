import pytest


def test_car_denied_access(car_checker, fail_file_paths: str):
    car_checker.check_car(image_path=fail_file_paths)

    assert not car_checker.decision, "Car managed to get in although it didn't fit the criteria"


def test_car_allowed_access(car_checker, success_file_paths: str):
    car_checker.check_car(image_path=success_file_paths)

    assert car_checker.decision, "Car failed to get in although it fit the criteria"
