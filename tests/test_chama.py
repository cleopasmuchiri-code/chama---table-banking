from models.chama import Chama
from models.member import Member
import datetime
import math
import pytest


@pytest.fixture
def chama():
    return Chama(
        name="Test Chama",
        target_amount=2000000,
        deadline=datetime.date(2026, 12, 31),
        frequency="monthly",
    )


@pytest.fixture
def members():
    return [
        Member(name="Wanjiru", password="pass1234"),
        Member(name="John", password="pass5678"),
    ]


def test_chama_initialization(chama):
    assert chama.name == "Test Chama"
    assert chama.target_amount == 2000000
    assert chama.frequency == "monthly"


def test_add_member_appends_to_list(chama):
    member = Member(name="Wanjiru", password="pass1234")
    chama.add_member(member)

    assert member in chama.members
    assert len(chama.members) == 1


def test_expected_contribution_per_member_calculation(chama, members):
    chama.members = members
    expected_contribution = chama.expected_contribution_per_member()

    assert expected_contribution == 1000000  # 2000000 / 2 members


def test_total_saved_calculation(chama, members):
    chama.members = members
    total_saved = chama.total_saved()

    assert total_saved == 0  # No contributions made yet


def test_progress_percentage_calculation(chama, members):
    chama.members = members

    progress_percentage = chama.progress_percentage()

    assert progress_percentage == 0  # No contributions made yet


def test_suggested_amount_per_member(chama, members):
    chama.members = members
    members[0].contribute(500000)
    expected_contribution = chama.expected_contribution_per_member()
    days_remaining = (chama.deadline - datetime.date.today()).days

    suggested_amount = chama.suggested_amount_per_member(members[0])

    assert suggested_amount == math.ceil(
        (expected_contribution - members[0].savings_balance) / days_remaining
    )
