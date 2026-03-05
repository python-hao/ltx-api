import os

from src.options import *
from src.globals import BASE_URL

class ApiParameters:
    def __init__(
        self,
        prompt: str,
        model: Model=Model.LTX_2_FAST,
        duration: Duration=Duration.SEC_8,
        resolution: Resolution=Resolution.TEN_EIGHTY_P,
        is_portrait: bool=False,
        image_uri: str='',
    ):
        self.prompt = prompt
        self.model = model
        self.duration = duration
        self.resolution = resolution
        self.is_portrait = is_portrait
        self.image_uri = image_uri

        self.base_url = BASE_URL
        if len(self.image_uri) > 0:
            self.endpoint = Endpoint.IMAGE_TO_VIDEO
        else:
            self.endpoint = Endpoint.TEXT_TO_VIDEO
    
    def __get_payload_with_only_prompt(self):
        return {
            'prompt': self.prompt,
            'model': self.model.value,
            'duration': self.duration.value,
            'resolution': self.resolution.value.__str__(self.is_portrait),
        }
    def __get_payload_with_image(self):
        return {
            'image_uri': self.image_uri,
            'prompt': self.prompt,
            'model': self.model.value,
            'duration': self.duration.value,
            'resolution': self.resolution.value.__str__(self.is_portrait),
        }
    def get_payload(self):
        if self.endpoint == Endpoint.IMAGE_TO_VIDEO:
            return self.__get_payload_with_image()
        else:
            return self.__get_payload_with_only_prompt()
    def get_url(self):
        return os.path.join(self.base_url, self.endpoint.value)