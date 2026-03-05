import dotenv, os

class Secret:
    api_key: str
    def __init__(self, env_name: str='LTXV_API_KEY'):
        dotenv.load_dotenv()
        self.api_key = os.getenv(env_name)
    
    def get_headers(self):
        return {
            'Authorization': 'Bearer {}'.format(self.api_key),
            'Content-Type': 'application/json',
        }

