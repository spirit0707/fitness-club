from datetime import date
from core.members import Member

class TempMember(Member):
    def get_membership_info(self) -> str:
        return f"Временный участник {self.name}"

m1 = TempMember(member_id=1, name="Иван", age=25, membership_type="Gold", join_date=date(2024, 10, 1))
m2 = TempMember(member_id=2, name="Анна", age=30, membership_type="Silver", join_date=date(2024, 10, 1))

print(m1)
print(m2)
print("Моложе ли Иван, чем Анна?", m1 < m2)
print("Дата вступления:", m1.join_date)
print(m1.get_membership_info())
