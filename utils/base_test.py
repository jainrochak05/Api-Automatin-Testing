import requests
import time

BASE_URL = "https://medicine-data-lstd.onrender.com"

def send_post_request(endpoint, payload):
    start_time = time.time()
    response = requests.post(
        BASE_URL + endpoint,
        json=payload,
        headers={"Content-Type": "application/json"}
    )
    response_time = time.time() - start_time
    return response, response_time
