import pytest
import requests
from utilities import parameters as params

def print_request_response(response):
    """Helper function to print request and response details."""
    print("\nRequest URL:", response.request.url)
    print("Request Method:", response.request.method)
    print("Request Headers:", response.request.headers)
    if response.request.body:
        print("Request Body:", response.request.body)
    print("Response Status Code:", response.status_code)
    print("Response Body:", response.text)

def test_create_pet():
    """Test to create a new pet."""
    response = requests.post(params.BASE_URL, json=params.new_pet)
    print_request_response(response)
    assert response.status_code == params.status_codes["success"]
    assert response.json()["name"] == params.new_pet["name"]
    assert response.json()["status"] == params.new_pet["status"]

def test_create_pet_invalid_data():
    """Test to create a pet with invalid data (e.g., missing 'name')."""
    response = requests.post(params.BASE_URL, json=params.invalid_pet_data)
    print_request_response(response)
    assert response.status_code == params.status_codes["bad_request"]

def test_create_pet_invalid_status():
    """Test to create a pet with an invalid status value."""
    response = requests.post(params.BASE_URL, json=params.invalid_status_pet)
    print_request_response(response)
    assert response.status_code == params.status_codes["bad_request"]
