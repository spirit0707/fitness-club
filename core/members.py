from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import date

class Member(ABC):

    def __init__(self, member_id: int, name: str, age: int, membership_type: str, join_date: date):
        self._member_id = member_id
        self._name = name
        self._age = age
        self._membership_type = membership_type
        self._join_date = join_date

    @property
    def member_id(self) -> int:
        return self._member_id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Имя не может быть пустым.")
        self._name = value

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int):
        if value <= 0:
            raise ValueError("Возраст должен быть положительным.")
        self._age = value

    @property
    def membership_type(self) -> str:
        return self._membership_type

    @membership_type.setter
    def membership_type(self, value: str):
        self._membership_type = value

    @property
    def join_date(self) -> date:
        return self._join_date

    @abstractmethod
    def get_membership_info(self) -> str:
        pass

    def __str__(self) -> str:
        return f"Участник: {self._name}, Тип членства: {self._membership_type}"
    
    def __lt__(self, other: Member) -> bool:
        return self._age < other.age

    def __gt__(self, other: Member) -> bool:
        return self._age > other.age

class Client(Member):
    
    def __init__(self, member_id: int, name: str, age: int, membership_type: str, 
                 join_date: date, subscription: str):
        super().__init__(member_id, name, age, membership_type, join_date)
        self._subscription = subscription

    @property
    def subscription(self) -> str:
        return self._subscription

    @subscription.setter
    def subscription(self, value: str):
        self._subscription = value

    def get_membership_info(self) -> str:
        return f"Клиент: {self._name}, Абонемент: {self._subscription}, " \
               f"Тип членства: {self._membership_type}, Дата вступления: {self._join_date}"

    def __str__(self) -> str:
        return f"Клиент: {self._name}, Абонемент: {self._subscription}"

class Trainer(Member):
    
    def __init__(self, member_id: int, name: str, age: int, membership_type: str, 
                 join_date: date, specialization: str):
        super().__init__(member_id, name, age, membership_type, join_date)
        self._specialization = specialization

    @property
    def specialization(self) -> str:
        return self._specialization

    @specialization.setter
    def specialization(self, value: str):
        self._specialization = value

    def get_membership_info(self) -> str:
        return f"Тренер: {self._name}, Специализация: {self._specialization}, " \
               f"Тип членства: {self._membership_type}, Дата вступления: {self._join_date}"

    def __str__(self) -> str:
        return f"Тренер: {self._name}, Специализация: {self._specialization}"