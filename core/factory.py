from datetime import date
from core.members import Client, Member, Trainer


class MemberFactory:

    @staticmethod
    def create_member(member_type: str, *args) -> Member:
        member_classes = {
            "client": Client,
            "trainer": Trainer
        }

        member_class = member_classes.get(member_type.lower())
        if not member_class:
            raise ValueError(f"Неизвестный тип участника: {member_type}")

        # Просто передаем все аргументы в конструктор
        return member_class(*args)
    
    @staticmethod
    def create_client(member_id: int, name: str, age: int, membership_type: str, 
                     join_date: date, subscription: str, permission: int = 1) -> Client:
        return Client(member_id, name, age, membership_type, join_date, subscription, permission)
    
    @staticmethod
    def create_trainer(member_id: int, name: str, age: int, membership_type: str, 
                      join_date: date, specialization: str, permission: int = 1) -> Trainer:
        return Trainer(member_id, name, age, membership_type, join_date, specialization, permission)