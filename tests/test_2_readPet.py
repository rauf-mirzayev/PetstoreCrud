# tests/test_read_pet.py

import pytest
import requests
from utilities import parameters as params

@pytest.fixture(scope="module", autouse=True)
def setup_create_pet():
    # Ensure the pet exists for read tests
    requests.post(params.BASE_URL, json=params.new_pet)

def test_get_pet():
    """Test to retrieve an existing pet."""
    response = requests.get(f"{params.BASE_URL}/{params.new_pet['id']}")
    assert response.status_code == params.status_codes["success"]
    assert response.json()["id"] == params.new_pet["id"]
    assert response.json()["name"] == params.new_pet["name"]

def test_get_nonexistent_pet():
    """Test to retrieve a pet that does not exist."""
    response = requests.get(f"{params.BASE_URL}/{params.nonexistent_pet_id}")
    assert response.status_code == params.status_codes["not_found"]
