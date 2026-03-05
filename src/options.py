import enum

class ImageSize:
    width: int
    height: int
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
    
    def __str__(self, is_portrait: bool=False):
        return f'{self.height}x{self.width}' if is_portrait else f'{self.width}x{self.height}'

class Resolution(enum.Enum):
    TEN_EIGHTY_P = ImageSize(width=1920, height=1080)
    TWO_K = ImageSize(width=2560, height=1440)
    FOUR_K = ImageSize(width=3840, height=2160)

class Duration(enum.Enum):
    SEC_6 = 6
    SEC_8 = 8
    SEC_10 = 10
    SEC_12 = 12
    SEC_14 = 14
    SEC_16 = 16
    SEC_18 = 18
    SEC_20 = 20

class Model(enum.Enum):
    LTX_2_FAST = 'ltx-2-fast'
    LTX_2_PRO = 'ltx-2-pro'

class Endpoint(enum.Enum):
    TEXT_TO_VIDEO = 'v1/text-to-video'
    IMAGE_TO_VIDEO = 'v1/image-to-video'
    # AUDIO_TO_VIDEO = 'v1/audio-to-video'
    # RETAKE = 'v1/retake'
    # EXTEND = 'v1/extend'