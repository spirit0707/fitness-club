from __future__ import annotations
from abc import ABC, ABCMeta, abstractmethod
from datetime import date

class MemberMeta(ABCMeta):
    registry = {}

    def __new__(mcs, name, bases, attrs):
        cls = super().__new__(mcs, name, bases, attrs)
        if name != "Member" and issubclass(cls, Member):
            MemberMeta.registry[name] = cls
        return cls

class Member(ABC, metaclass=MemberMeta):

    def __init__(self, member_id: int, name: str, age: int, membership_type: str, join_date: date):
        self.__member_id = member_id
        self.__name = name
        self.__age = age
        self.__membership_type = membership_type
        self.__join_date = join_date

    @property
    def member_id(self) -> int:
        return self.__member_id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Имя не может быть пустым.")
        self.__name = value

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, value: int):
        if value <= 0:
            raise ValueError("Возраст должен быть положительным.")
        self.__age = value

    @property
    def membership_type(self) -> str:
        return self.__membership_type

    @membership_type.setter
    def membership_type(self, value: str):
        self.__membership_type = value

    @property
    def join_date(self) -> date:
        return self.__join_date

    @classmethod
    def create(cls, member_type: str, *args, **kwargs) -> Member:
        member_class = MemberMeta.registry.get(member_type)
        if member_class is None:
            raise ValueError(f"Неизвестный тип участника: {member_type}")
        return member_class(*args, **kwargs)

    @abstractmethod
    def get_membership_info(self) -> str:
        pass

    def __str__(self) -> str:
        return f"Участник: {self.name}, Тип членства: {self.membership_type}"

    def __lt__(self, other: Member) -> bool:
        return self.age < other.age

    def __gt__(self, other: Member) -> bool:
        return self.age > other.age

class Client(Member):

    def __init__(self, member_id: int, name: str, age: int, membership_type: str,
                 join_date: date, subscription: str):
        super().__init__(member_id, name, age, membership_type, join_date)
        self.__subscription = subscription

    @property
    def subscription(self) -> str:
        return self.__subscription

    @subscription.setter
    def subscription(self, value: str):
        self.__subscription = value

    def get_membership_info(self) -> str:
     return f"Клиент: {self.name}, Абонемент: {self.subscription}, " \
         f"Тип членства: {self.membership_type}, Дата вступления: {self.join_date}"

    def __str__(self) -> str:
        return f"Клиент: {self.name}, Абонемент: {self.subscription}"

class Trainer(Member):

    def __init__(self, member_id: int, name: str, age: int, membership_type: str,
                 join_date: date, specialization: str):
        super().__init__(member_id, name, age, membership_type, join_date)
        self.__specialization = specialization

    @property
    def specialization(self) -> str:
        return self.__specialization

    @specialization.setter
    def specialization(self, value: str):
        self.__specialization = value

    def get_membership_info(self) -> str:
     return f"Тренер: {self.name}, Специализация: {self.specialization}, " \
         f"Тип членства: {self.membership_type}, Дата вступления: {self.join_date}"

    def __str__(self) -> str:
        return f"Тренер: {self.name}, Специализация: {self.specialization}"