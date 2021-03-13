import requests

def test_main_defaultroute_return_code():
    response = requests.get("http://127.0.0.1:8081")
    assert response.status_code == 200

