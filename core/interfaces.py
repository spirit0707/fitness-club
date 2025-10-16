from abc import ABC, abstractmethod

from core.gym_class import GymClass
from core.members import Client

class Bookable(ABC):

    @abstractmethod
    def book_class(self, gym_class: GymClass, participant: Client):
        pass

class Reportable(ABC):

    @abstractmethod
    def generate_report(self):
        pass