import base64
import re

from exceptions import LicenseIdentifyingError

public_transportation = ['6', 'G']
military_and_law_enforcement = ['L', 'M']


def find_plate_line(lines: list):
    lines.sort(key=lambda x: x['Words'][0]['Height'], reverse=True)
    plate_number = re.sub('[^A-Za-z0-9]+', '', lines[0]['LineText'])

    if plate_number.isupper() or plate_number.isnumeric():
        return plate_number

    raise LicenseIdentifyingError('License plate number was not found.')


def car_verification(plate_number: str):
    plate_number = re.sub('[^A-Za-z0-9]+', '', plate_number).upper()

    for let in public_transportation:
        if plate_number.endswith(let):
            return False

    for let in military_and_law_enforcement:
        if let in plate_number:
            return False

    if plate_number.isnumeric():
        return False

    return True
