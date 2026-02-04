from utils.base_test import send_post_request

def test_valid_medicine_name():
    payload = {
        "medicine_name": "Paracetamol"
    }

    response, response_time = send_post_request("/get_medicine_info", payload)

    assert response.status_code == 200
    assert response_time < 2

    data = response.json()

    assert isinstance(data, list)
    assert "medicine_name" in data[0]
    assert "composition" in data[0]
    assert "uses" in data[0]
    assert "side_effects" in data[0]

def test_missing_medicine_name():
    payload = {}

    response, _ = send_post_request("/get_medicine_info", payload)

    assert response.status_code == 400
    assert "error" in response.json()

def test_invalid_medicine_name():
    payload = {
        "medicine_name": "SomeRandomDrugXYZ"
    }

    response, _ = send_post_request("/get_medicine_info", payload)

    assert response.status_code == 404
    assert "error" in response.json()



def test_empty_string_medicine():
    payload = {
        "medicine_name": ""
    }

    response, _ = send_post_request("/get_medicine_info", payload)

    assert response.status_code == 400
