from abc import ABC, abstractmethod

from core.gym_class import GymClass
from core.members import Member

class Bookable(ABC):
    """Интерфейс записи на тренировку

    Args:
        ABC
    """
    @abstractmethod
    def book_class(self, member: Member, gym_class: GymClass):
        """Запуск процесса записи

        Args:
            member (Member): кто записывается
            gym_class (GymClass): куда записывается
        """
        pass

class Reportable(ABC):
    """Интерфейс генерации отчетов

    Args:
        ABC
    """

    @abstractmethod
    def generate_report(self):
        """Запуск генерации отчета
        """
        pass