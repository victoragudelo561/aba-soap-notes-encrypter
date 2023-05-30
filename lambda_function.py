import json
import os

from dotenv import load_dotenv

from encrypter import AESCipher
from ai_lambda import AITokenizer

load_dotenv()


def lambda_handler(event, context):
    raw_text_to_decrypt = json.loads(event['body']).get("text")

    if not raw_text_to_decrypt:  # TODO change to key from FE:
        return {'statusCode': 400, 'body': 'There is no data available'}

    raw_text_decrypted = AESCipher().decrypt(raw_text_to_decrypt)
    json_text_decrypted = json.loads(raw_text_decrypted)
    ai_token = AITokenizer(json_text_decrypted).get_tokens()
    ai_token_as_string = json.dumps(ai_token)
    ai_token_encrypted = AESCipher().encrypt(ai_token_as_string)

    return json.dumps({'statusCode': 200, 'body': ai_token_encrypted})
