from models.chama import Chama
from models.member import Member
from storage import save_chama, load_chama
import datetime

chama = Chama(
    name="Test Chama",
    target_amount=2000000,
    deadline=datetime.date(2026, 12, 31),
    frequency="monthly",
)
member = Member(name="Wanjiru", role="member", password="pass1234")
member.contribute(5000)
chama.add_member(member)

save_chama(chama)
print("Saved. Check data/chama.json now.")

reloaded = load_chama()
print("Reloaded chama name:", reloaded.name)
print("Reloaded member savings:", reloaded.members[0].savings_balance)
