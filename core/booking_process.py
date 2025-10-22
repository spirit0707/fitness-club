from abc import ABC, abstractmethod
from core.members import Client, Trainer
from core.gym_class import GymClass
from core.exceptions import ClassFullError
from core.decorators import check_access
from typing import Union

class BookingProcess(ABC):

    @check_access
    def book_class(self, member: Union[Client, Trainer], gym_class: GymClass) -> str:
        print(f"Запуск процесса записи для {member.name} на {gym_class.class_name}")

        self._specific_availability_check(gym_class, member)
        self._add_participant(member, gym_class)
        self._confirm_booking(member, gym_class)

        return f"Процесс записи для {member.name} завершен успешно."

    @abstractmethod
    def _specific_availability_check(self, gym_class: GymClass, member: Union[Client, Trainer]):
        pass

    @abstractmethod
    def _add_participant(self, member: Union[Client, Trainer], gym_class: GymClass):
        pass

    def _confirm_booking(self, member: Union[Client, Trainer], gym_class: GymClass):
        print(f"3. Подтверждение: Участник {member.name} уведомлен о записи.")


class ClientBookingProcess(BookingProcess):

    def _specific_availability_check(self, gym_class: GymClass, member: Client):
        if len(gym_class.get_participants()) >= gym_class.location.capacity:
            raise ClassFullError(gym_class.class_name)
        print("1. Проверка доступности: OK.")

    def _add_participant(self, client: Client, gym_class: GymClass):
        try:
            gym_class.add_participant(client)
            print(f"2. Добавление: Клиент {client.name} успешно записан в список.")
        except ValueError as e:
            print(f"2. Добавление: {e}")

class TrainerBookingProcess(BookingProcess):

    def _specific_availability_check(self, gym_class: GymClass, member: Trainer):
        print("1. Проверка доступности: Тренер не влияет на вместимость зала. OK.")
        pass

    def _add_participant(self, trainer: Trainer, gym_class: GymClass):
        print(f"2. Добавление: Тренер {trainer.name} назначен на тренировку.")