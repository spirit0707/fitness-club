from datetime import date
from core.members import Trainer, Client, Member
from core.gym_class import GymClass, Location

# тест пункта 1
class TempMember(Member):
    def get_membership_info(self) -> str:
        return f"Временный участник {self.name}"

m1 = TempMember(1, "Иван", 25, "Gold", date(2024, 10, 1))
m2 = TempMember(2, "Анна", 30, "Silver", date(2024, 10, 1))

print(m1)
print(m2)
print("Моложе ли Иван, чем Анна?", m1 < m2)
print("Дата вступления:", m1.join_date)
print(m1.get_membership_info())

# тест пункта 2
client = Client(1, "Иван Петров", 25, "Премиум", date(2023, 1, 15), "Годовой")
trainer = Trainer(2, "Анна Сидорова", 30, "Персонал", date(2022, 5, 10), "Фитнес")
    
print(client.get_membership_info())
print(client)
print(trainer.get_membership_info())
print(trainer)
print(f"Клиент младше тренера: {client < trainer}")
print(f"Тренер старше клиента: {trainer > client}")

# тест пункта 3
trainer = Trainer(1, "Анна", 30, "Staff", date(2020, 5, 1), "Йога")
client1 = Client(2, "Иван", 25, "Premium", date(2024, 7, 1), "Йога")
client2 = Client(3, "Мария", 28, "Basic", date(2024, 8, 1), "Йога")

location = Location("Зал №3", capacity=10)

yoga_class = GymClass("Йога", trainer, "Пн/Ср/Пт 10:00", location)

yoga_class.add_participant(client1)
yoga_class.add_participant(client2)

print("Информация о занятии")
print(yoga_class)