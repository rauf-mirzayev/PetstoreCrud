# tests/test_delete_pet.py

import pytest
import requests
from utilities import parameters as params

@pytest.fixture(scope="module", autouse=True)
def setup_create_pet():
    # Ensure the pet exists for delete tests
    requests.post(params.BASE_URL, json=params.new_pet)

def test_delete_pet():
    """Test to delete an existing pet."""
    response = requests.delete(f"{params.BASE_URL}/{params.new_pet['id']}")
    assert response.status_code == params.status_codes["success"]

    # Verify deletion
    response = requests.get(f"{params.BASE_URL}/{params.new_pet['id']}")
    assert response.status_code == params.status_codes["not_found"]

def test_delete_nonexistent_pet():
    """Test to delete a pet that does not exist."""
    response = requests.delete(f"{params.BASE_URL}/{params.nonexistent_pet_id}")
    assert response.status_code in (params.status_codes["bad_request"], params.status_codes["not_found"])
