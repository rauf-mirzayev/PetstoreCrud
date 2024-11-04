import pytest
import requests
from utilities import parameters as params

def print_request_response(response):
    """Helper function to print request and response details."""
    print("\nRequest URL:", response.request.url)
    print("Request Method:", response.request.method)
    print("Request Headers:", response.request.headers)
    print("Response Status Code:", response.status_code)
    print("Response Body:", response.text)

@pytest.fixture(scope="module", autouse=True)
def setup_create_pet():
    # Ensure the pet exists for read tests
    requests.post(params.BASE_URL, json=params.new_pet)

def test_get_pet():
    """Test to retrieve an existing pet."""
    response = requests.get(f"{params.BASE_URL}/{params.new_pet['id']}")
    print_request_response(response)
    assert response.status_code == params.status_codes["success"]
    assert response.json()["id"] == params.new_pet["id"]
    assert response.json()["name"] == params.new_pet["name"]

def test_get_nonexistent_pet():
    """Test to retrieve a pet that does not exist."""
    response = requests.get(f"{params.BASE_URL}/{params.nonexistent_pet_id}")
    print_request_response(response)
    assert response.status_code == params.status_codes["not_found"]
