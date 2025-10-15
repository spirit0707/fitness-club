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
