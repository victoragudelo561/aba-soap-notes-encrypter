import requests
import os
from dotenv import load_dotenv


load_dotenv()

class AITokenizer:
    def __init__(self, ai_json):
        self.ai_json = ai_json
        self.ai_lambda_url = os.environ['AI_LAMBDA_URL']
        self.header = os.environ['API_KEY']

    def get_tokens(self):
        response =  requests.get(
            url=self.ai_lambda_url,
            headers={'API_KEY': self.header},
            json=self.ai_json
        )

        return response.json()