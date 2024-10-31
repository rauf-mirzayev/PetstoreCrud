# utilities/parameters.py

# Base URL for the Petstore API
BASE_URL = "https://petstore.swagger.io/v2/pet"

# Sample pet data for tests
new_pet = {
    "id": "000111",
    "name": "Lucky",
    "status": "available"
}

# Pet data with missing required fields (negative scenario)
invalid_pet_data = {
    "id": "8172"
}

# Pet data with invalid status value (negative scenario)
invalid_status_pet = {
    "id": "123457",
    "name": "InvalidStatusPet",
    "status": "unknown_status"
}

# Non-existent pet ID for negative scenarios
nonexistent_pet_id = 9999997878787899

# Expected HTTP status codes for various responses
status_codes = {
    "success": 200,
    "not_found": 404,
    "bad_request": 400
}
