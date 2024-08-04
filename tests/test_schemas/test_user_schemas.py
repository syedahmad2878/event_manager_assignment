import pytest
from pydantic import ValidationError
from datetime import datetime
import uuid
from app.schemas.user_schemas import UserBase, UserCreate, UserUpdate, UserResponse, UserListResponse, LoginRequest

# Fixtures for test data
@pytest.fixture
def user_base_data():
    return {
        "email": "john.doe@example.com",
        "nickname": "john_doe",
        "first_name": "John",
        "last_name": "Doe",
        "bio": "Experienced software developer specializing in web applications.",
        "profile_picture_url": "https://example.com/profiles/john.jpg",
        "linkedin_profile_url": "https://linkedin.com/in/johndoe",
        "github_profile_url": "https://github.com/johndoe"
    }

@pytest.fixture
def user_create_data(user_base_data):
    return {**user_base_data, "password": "Secure*1234"}

@pytest.fixture
def user_update_data():
    return {
        "email": "john.doe.updated@example.com",
        "nickname": "john_doe_updated",
        "first_name": "Johnny",
        "last_name": "Doe",
        "bio": "Updated bio.",
        "profile_picture_url": "https://example.com/profiles/john_updated.jpg",
        "linkedin_profile_url": "https://linkedin.com/in/johndoeupdated",
        "github_profile_url": "https://github.com/johndoeupdated"
    }

@pytest.fixture
def user_response_data(user_base_data):
    return {**user_base_data, "id": uuid.uuid4(), "role": "AUTHENTICATED", "is_professional": True}

@pytest.fixture
def login_request_data():
    return {
        "email": "john.doe@example.com",
        "password": "Secure*1234"
    }

# Tests for UserBase
def test_user_base_valid(user_base_data):
    user = UserBase(**user_base_data)
    assert user.nickname == user_base_data["nickname"]
    assert user.email == user_base_data["email"]

# Tests for UserCreate
def test_user_create_valid(user_create_data):
    user = UserCreate(**user_create_data)
    assert user.nickname == user_create_data["nickname"]
    assert user.password == user_create_data["password"]

# Tests for UserUpdate
def test_user_update_valid(user_update_data):
    user_update = UserUpdate(**user_update_data)
    assert user_update.email == user_update_data["email"]
    assert user_update.first_name == user_update_data["first_name"]

# Tests for UserResponse
def test_user_response_valid(user_response_data):
    user = UserResponse(**user_response_data)
    assert user.id == user_response_data["id"]

# Tests for LoginRequest
def test_login_request_valid(login_request_data):
    login = LoginRequest(**login_request_data)
    assert login.email == login_request_data["email"]
    assert login.password == login_request_data["password"]

# Parametrized tests for nickname and email validation
@pytest.mark.parametrize("nickname", ["test_user", "test-user", "testuser123", "123test"])
def test_user_base_nickname_valid(nickname, user_base_data):
    user_base_data["nickname"] = nickname
    user = UserBase(**user_base_data)
    assert user.nickname == nickname

@pytest.mark.parametrize("nickname", ["test user", "test?user", "", "us"])
def test_user_base_nickname_invalid(nickname, user_base_data):
    user_base_data["nickname"] = nickname
    with pytest.raises(ValidationError):
        UserBase(**user_base_data)

# Parametrized tests for URL validation
@pytest.mark.parametrize("url", ["http://valid.com/profile.jpg", "https://valid.com/profile.png", None])
def test_user_base_url_valid(url, user_base_data):
    user_base_data["profile_picture_url"] = url
    user = UserBase(**user_base_data)
    assert user.profile_picture_url == url

@pytest.mark.parametrize("url", ["ftp://invalid.com/profile.jpg", "http//invalid", "https//invalid"])
def test_user_base_url_invalid(url, user_base_data):
    user_base_data["profile_picture_url"] = url
    with pytest.raises(ValidationError):
        UserBase(**user_base_data)

# Tests for UserBase with invalid email
def test_user_base_invalid_email():
    invalid_email_data = {
        "email": "john.doe.example.com",
        "nickname": "john_doe",
        "first_name": "John",
        "last_name": "Doe",
        "bio": "Experienced software developer specializing in web applications.",
        "profile_picture_url": "https://example.com/profiles/john.jpg",
        "linkedin_profile_url": "https://linkedin.com/in/johndoe",
        "github_profile_url": "https://github.com/johndoe"
    }
    with pytest.raises(ValidationError) as exc_info:
        UserBase(**invalid_email_data)
    assert "value is not a valid email address" in str(exc_info.value)