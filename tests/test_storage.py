from models.chama import Chama
from models.member import Member
from storage import save_chama, load_chama
import datetime


def test_save_and_load(tmp_path):
    filepath = tmp_path / "chama.json"

    chama = Chama(
        name="Test",
        target_amount=100000,
        deadline=datetime.date(2026, 12, 31),
        frequency="monthly",
    )
    member = Member(name="Wanjiru", role="member", password="pass1234")
    member.contribute(5000)
    chama.add_member(member)

    save_chama(chama, filepath=str(filepath))
    reloaded = load_chama(filepath=str(filepath))

    assert reloaded.name == "Test"
    assert reloaded.members[0].savings_balance == 5000
