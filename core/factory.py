from datetime import date
from core.members import Client, Member, Trainer


class MemberFactory:
    """Фабрика для создания клиентов и тренеров
    """

    @staticmethod
    def create_member(member_type: str, *args) -> Member:
        """Создать участника по названию класса

        Args:
            member_type (str): тип участника

        Raises:
            ValueError: Неизвестный тип участника

        Returns:
            Member
        """
        member_classes = {
            "client": Client,
            "trainer": Trainer
        }

        member_class = member_classes.get(member_type.lower())
        if not member_class:
            raise ValueError(f"Неизвестный тип участника: {member_type}")

        return member_class(*args)
    
    @staticmethod
    def create_client(member_id: int, name: str, age: int, membership_type: str, 
                     join_date: date, subscription: str, permission: int = 1) -> Client:
        """Создать клиента

        Args:
            member_id (int)
            name (str)
            age (int)
            membership_type (str)
            join_date (date)
            subscription (str)
            permission (int, optional): Defaults to 1.

        Returns:
            Client
        """
        return Client(member_id, name, age, membership_type, join_date, subscription, permission)
    
    @staticmethod
    def create_trainer(member_id: int, name: str, age: int, membership_type: str, 
                      join_date: date, specialization: str, permission: int = 1) -> Trainer:
        """Создать тренера

        Args:
            member_id (int)
            name (str)
            age (int)
            membership_type (str)
            join_date (date)
            specialization (str)
            permission (int, optional): Defaults to 1.

        Returns:
            Trainer
        """
        return Trainer(member_id, name, age, membership_type, join_date, specialization, permission)