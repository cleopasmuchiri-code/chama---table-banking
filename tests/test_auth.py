# auth tests
import pytest
from models.member import Member


@pytest.fixture
def member():
    return Member(name="Wanjiru", role="member", password="pass1234")


# test login method - both successful and unsuccessful login attempts
def test_login(member):
    assert member.login("pass1234") is True
    with pytest.raises(ValueError):
        member.login("wrongpassword")
