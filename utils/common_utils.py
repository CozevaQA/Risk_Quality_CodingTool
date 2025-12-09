# utils/common_utils.py
import base64

def decode_base64(data):
    return base64.b64decode(data).decode("utf-8")

def encode_base64(text):
    return base64.b64encode(text.encode()).decode()