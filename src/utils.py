import datetime, uuid, os
import base64
from PIL import Image
from io import BytesIO

def get_output_name(file_name: str='video', path: str='output'):
    suffix = '{}-{}'.format(
        datetime.datetime.now().strftime('%H%M%S'),
        str(uuid.uuid4())[:8]
    )

    # Create folders
    sub_path = datetime.datetime.now().strftime('%Y%m%d')
    full_path = os.path.join(path, sub_path)
    if not os.path.exists(full_path):
        os.makedirs(full_path)
    
    full_file_name = os.path.join(full_path, file_name)

    return '{}-{}.mp4'.format(full_file_name, suffix)



def image_to_base64(image_uri, format="JPEG"):
    with Image.open(image_uri, mode='r') as img:
        buffered = BytesIO()
        img.save(buffered, format=format)
        img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
        if img_str == '':
            return ''
        img_data = f'data:image/{format.lower()};base64,{img_str}'
    return img_data