from DAL.api_handler import ApiConnectionClient
from BL.utils import find_plate_line
from exceptions import *

request_body = {
    'detectOrientation': True,
    'scale': True,
    'isOverlayRequired': True,
    'OCREngine': 2
}


class OcrSpaceApi:
    def __init__(self):
        self.base_url = 'https://api.ocr.space'
        self.api_connection = ApiConnectionClient(base_url=self.base_url)

    def post_request_get_text_from_image_file(self, image_path):
        files = {'upload_file': open(image_path, 'rb')}
        response = self.api_connection.post(url='/parse/image', body=request_body, file=files)

        if response['IsErroredOnProcessing']:
            raise OnProccessingError(response['ErrorMessage'][0])

        return find_plate_line(response['ParsedResults'][0]['TextOverlay']['Lines'])

    def post_request_get_text_from_image_url(self, image_url):
        request_body['url'] = image_url
        response = self.api_connection.post(url='/parse/image', body=request_body)

        return find_plate_line(response['ParsedResults'][0]['TextOverlay']['Lines'])
