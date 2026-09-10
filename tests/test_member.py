import pytest
from models.member import Member

interest_rate = 0.05  # 5% interest rate


@pytest.fixture
def member():
    return Member(name="Wanjiru", role="member", password="pass1234")


# test member initialization
def test_member_initialization(member):
    assert member.name == "Wanjiru"
    assert member.role == "member"
    assert member.password == "pass1234"


# test contribute method
def test_contribute_method(member):
    member.contribute(5000)
    assert member.savings_balance == 5000


# test contribution of a negative amount
def test_contribute_negative_raises_error(member):
    with pytest.raises(ValueError):
        member.contribute(-100)


# test request_loan method
def test_request_loan_method(member):
    member.request_loan(10000)
    assert member.loan_balance == (10000 * (1 + interest_rate))


# test request_loan method with amount exceeding limit
def test_request_loan_exceeding_limit(member):
    member.contribute(5000)

    with pytest.raises(ValueError):
        member.request_loan(100000)

    assert member.loan_balance == 0  # loan should not be granted


def test_repay_loan_method(member):
    member.request_loan(10000)
    member.repay_loan(5000)
    assert member.loan_balance == (10000 * (1 + interest_rate)) - 5000
