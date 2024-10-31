# tests/test_create_pet.py

import pytest
import requests
from utilities import parameters as params

def test_create_pet():
    """Test to create a new pet."""
    response = requests.post(params.BASE_URL, json=params.new_pet)
    assert response.status_code == params.status_codes["success"]
    assert response.json()["name"] == params.new_pet["name"]
    assert response.json()["status"] == params.new_pet["status"]

def test_create_pet_invalid_data():
    """Test to create a pet with invalid data (e.g., missing 'name')."""
    response = requests.post(params.BASE_URL, json=params.invalid_pet_data)
    assert response.status_code == params.status_codes["bad_request"]

def test_create_pet_invalid_status():
    """Test to create a pet with an invalid status value."""
    response = requests.post(params.BASE_URL, json=params.invalid_status_pet)
    assert response.status_code == params.status_codes["bad_request"]
