# test loans
from models.loan import loan
from models.member import Member
import pytest

interest_rate = 0.05  # 5% interest rate


@pytest.fixture
def member():
    return Member(name="Wanjiru", role="member", password="pass1234")


def test_loan_balance(member):
    member.request_loan(10000)
    assert member.loan_balance == (10000 * (1 + interest_rate))


def test_loan_repayment(member):
    member.request_loan(10000)
    assert member.loan_balance == (10000 * (1 + interest_rate))
    member.repay_loan(5000)
    assert member.loan_balance == (10000 * (1 + interest_rate)) - 5000


def test_loan_is_active(member):
    member.request_loan(10000)
    assert member.is_loan_active() is True
    member.repay_loan(5000)
    assert member.is_loan_active() is True
    member.repay_loan(5500)
    assert member.is_loan_active() is False
