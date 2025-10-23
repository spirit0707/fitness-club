from abc import ABC
from core.members import Trainer, Client

class Location:
    """Место проведения тренировки
    """
    def __init__(self, room_name: str, capacity: int):
        self.__room_name = room_name
        self.__capacity = capacity

    @property
    def room_name(self) -> str:
        return self.__room_name

    @room_name.setter
    def room_name(self, value: str):
        if not value.strip():
            raise ValueError("Название зала не может быть пустым.")
        self.__room_name = value

    @property
    def capacity(self) -> int:
        return self.__capacity

    @capacity.setter
    def capacity(self, value: int):
        if value <= 0:
            raise ValueError("Вместимость должна быть положительной.")
        self.__capacity = value

    def __str__(self) -> str:
        return f"Зал: {self.__room_name} (вместимость: {self.__capacity})"

class GymClass(ABC):
    """Тренировка

    Args:
        ABC
    """
    def __init__(self, class_name: str, trainer: Trainer, schedule: str, location: Location):
        self.__class_name = class_name
        self.__trainer = trainer
        self.__schedule = schedule
        self.__location = location
        self.__participants: list[Client] = []

    @property
    def class_name(self) -> str:
        return self.__class_name

    @property
    def trainer(self) -> Trainer:
        return self.__trainer

    @property
    def schedule(self) -> str:
        return self.__schedule

    @schedule.setter
    def schedule(self, value: str):
        self.__schedule = value

    @property
    def location(self) -> Location:
        return self.__location

    def add_participant(self, client: Client):
        """Добавить клиента в список участников

        Args:
            client (Client): кого добавить

        Raises:
            ValueError: зал переполнен или клиент уже записан
        """
        if len(self.__participants) >= self.location.capacity:
            raise ValueError("Зал переполнен")
        if client in self.__participants:
            raise ValueError(f"{client.name} уже записан")
        self.__participants.append(client)

        if hasattr(client, 'send_notification'):
            client.send_notification(
                "Успешная запись на тренировку",
                f"Вы записаны на тренировку '{self.class_name}'. "
                f"Тренер: {self.trainer.name}. Время: {self.schedule}",
                "success"
            )

        if hasattr(self.trainer, 'send_notification'):
            self.trainer.send_notification(
                "Новый участник на тренировке",
                f"Клиент {client.name} записался на вашу тренировку '{self.class_name}'",
                "info"
            )

    def remove_participant(self, client: Client):
        """Убрать клиента из списка участников

        Args:
            client (Client): кого убрать

        Raises:
            ValueError: клиент не найден
        """
        if client not in self.__participants:
            raise ValueError(f"{client.name} не найден")
        self.__participants.remove(client)

        if hasattr(client, 'send_notification'):
            client.send_notification(
                "Отмена записи на тренировку",
                f"Ваша запись на тренировку '{self.class_name}' отменена",
                "warning"
            )

    def get_participants(self) -> list[str]:
        """Получить список участников

        Returns:
            list[str]: имена клиентов на тренировке
        """
        return [p.name for p in self.__participants]

    def __str__(self) -> str:
        return (
            f"Занятие: {self.class_name}\n"
            f"Тренер: {self.trainer.name}\n"
            f"Расписание: {self.schedule}\n"
            f"{self.location}\n"
            f"Участники: {', '.join(self.get_participants()) or 'нет'}"
        )
