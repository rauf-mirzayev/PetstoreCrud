# tests/test_update_pet.py

import pytest
import requests
from utilities import parameters as params

@pytest.fixture(scope="module", autouse=True)
def setup_create_pet():
    # Ensure the pet exists for update tests
    requests.post(params.BASE_URL, json=params.new_pet)

def test_update_pet():
    """Test to update an existing pet."""
    updated_pet = params.new_pet.copy()
    updated_pet["status"] = "sold"
    response = requests.put(params.BASE_URL, json=updated_pet)
    assert response.status_code == params.status_codes["success"]
    assert response.json()["status"] == "sold"

def test_update_nonexistent_pet():
    """Test to update a pet that does not exist."""
    non_existing_pet = {
        "id": params.nonexistent_pet_id,
        "name": "Ghost",
        "status": "available"
    }
    response = requests.put(params.BASE_URL, json=non_existing_pet)
    assert response.status_code in (params.status_codes["bad_request"], params.status_codes["not_found"])
