from abc import ABC
from core.members import Trainer, Client
from typing import List

class Location:
    def __init__(self, room_name: str, capacity: int):
        self._room_name = room_name
        self._capacity = capacity

    @property
    def room_name(self) -> str:
        return self._room_name

    @room_name.setter
    def room_name(self, value: str):
        if not value.strip():
            raise ValueError("Название зала не может быть пустым.")
        self._room_name = value

    @property
    def capacity(self) -> int:
        return self._capacity

    @capacity.setter
    def capacity(self, value: int):
        if value <= 0:
            raise ValueError("Вместимость должна быть положительной.")
        self._capacity = value

    def __str__(self) -> str:
        return f"Зал: {self._room_name} (вместимость: {self._capacity})"

class GymClass(ABC):
    def __init__(self, class_name: str, trainer: Trainer, schedule: str, location: Location):
        self._class_name = class_name
        self._trainer = trainer
        self._schedule = schedule
        self._location = location
        self._participants: List[Client] = []

    @property
    def class_name(self) -> str:
        return self._class_name
    
    @property
    def trainer(self) -> Trainer:
        return self._trainer
    
    @property
    def schedule(self) -> str:
        return self._schedule
    
    @schedule.setter
    def schedule(self, value: str):
        self._schedule = value

    @property
    def location(self) -> Location:
        return self._location
    
    def add_participant(self, client: Client):
        if len(self._participants) >= self._location.capacity:
            raise ValueError("Зал переполнен")
        if client in self._participants:
            raise ValueError(f"{client.name} уже записан")
        self._participants.append(client)

    def remove_participant(self, client: Client):
        if client not in self._participants:
            raise ValueError(f"{client.name} не найден")
        self._participants.remove(client)

    def get_participants(self) -> list[str]:
        return [p.name for p in self._participants]
    
    def __str__(self) -> str:
        return (
            f"Занятие: {self._class_name}\n"
            f"Тренер: {self._trainer.name}\n"
            f"Расписание: {self._schedule}\n"
            f"{self._location}\n"
            f"Участники: {', '.join(self.get_participants()) or 'нет'}"
        )
    