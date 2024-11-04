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
    # Ensure the pet exists for delete tests
    requests.post(params.BASE_URL, json=params.new_pet)

def test_delete_pet():
    """Test to delete an existing pet."""
    response = requests.delete(f"{params.BASE_URL}/{params.new_pet['id']}")
    print_request_response(response)
    assert response.status_code == params.status_codes["success"]

    # Verify deletion
    response = requests.get(f"{params.BASE_URL}/{params.new_pet['id']}")
    print_request_response(response)
    assert response.status_code == params.status_codes["not_found"]

def test_delete_nonexistent_pet():
    """Test to delete a pet that does not exist."""
    response = requests.delete(f"{params.BASE_URL}/{params.nonexistent_pet_id}")
    print_request_response(response)
    assert response.status_code in (params.status_codes["bad_request"], params.status_codes["not_found"])
