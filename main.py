from datetime import date
from core.members import Trainer, Client, Member, MemberMeta
from core.gym_class import GymClass, Location
from core.handlers import Administrator, Manager, Director
from core.exceptions import RenewalLimitExceededError, ClassFullError, PermissionDeniedError
from core.booking_process import ClientBookingProcess, TrainerBookingProcess

# тест пункта 1
m1 = Client(1, "Иван", 25, "Gold", date(2024, 10, 1), "Годовой")
m2 = Client(2, "Анна", 30, "Silver", date(2024, 10, 1), "Годовой")

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

# тест 6
print("Реестр зарегистрированных подклассов:")
print(MemberMeta.registry)

member = Member.create("Trainer", 2, "Анна", 30, "Premium", date.today(), "Йога")

print(member)
print(member.get_membership_info())

# Тест пункта 8
admin = Administrator()
manager = Manager()
director = Director()

admin.set_next(manager).set_next(director)

requests = [
    (1, "1 месяц (Лимит Администратора)"),
    (3, "3 месяца (Лимит Менеджера)"),
    (6, "6 месяцев (Должен одобрить Директор)"),
    (12, "12 месяцев (Должен одобрить Директор)")
]

for months, description in requests:
    print(f"\nЗапрос на продление: {description}")
    try:
        result = admin.handle_request(months)
        print(f"Результат: {result}")
    except RenewalLimitExceededError as e:
        print(f"Неожиданная Ошибка: {e}")

# Тест пункта 9
trainer_9 = Trainer(10, "Елена", 35, "Персонал", date(2021, 1, 1), "Пилатес")
client_9_1 = Client(11, "Петр", 28, "Basic", date(2024, 9, 1), "Месячный")
client_9_2 = Client(12, "Светлана", 22, "Premium", date(2024, 9, 1), "Годовой")

location_9 = Location("Малый зал", capacity=1)
pilates_class = GymClass("Пилатес", trainer_9, "Вт/Чт 18:00", location_9)

print("\nПроцесс 1: Запись первого клиента (Петр)")
client_booking = ClientBookingProcess()
client_booking.book_class(client_9_1, pilates_class)
print(f"Текущие участники: {pilates_class.get_participants()}")

print("\nПроцесс 2: Запись второго клиента (Светлана) - ОЖИДАЕТСЯ ОШИБКА")
try:
    client_booking.book_class(client_9_2, pilates_class)
except ClassFullError as e:
    print(f"Ошибка (проверено): {e}")

print("\nПроцесс 3: Назначение тренера")
trainer_booking = TrainerBookingProcess()
trainer_booking.book_class(trainer_9, pilates_class)

# Тест пункта 10
print()
client10 = Client(13, "Петр Бесправный", 28, "Basic", date(2024, 9, 1), "Месячный", 0)
try:
    client_booking.book_class(client10, yoga_class)
except PermissionDeniedError as e:
    print(f"Ошибка: {e}")

# Тест пункт 12
print()
client_file = client10.to_file()
print(client_file)
client12 = Member.from_file(client_file)
print(client12)

print()
trainer_file = trainer.to_file()
print(trainer_file)
trainer12 = Member.from_file(trainer_file)
print(trainer12)
# тест 6
print("Реестр зарегистрированных подклассов:")
print(MemberMeta.registry)

member = Member.create("Trainer", 2, "Анна", 30, "Premium", date.today(), "Йога")

print(member)
print(member.get_membership_info())
