from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional
from core.exceptions import RenewalLimitExceededError

class SubscriptionHandler(ABC):
    """Обработчик продлений абонементов

    Args:
        ABC

    Raises:
        RenewalLimitExceededError

    Returns:
        str
    """

    _next_handler: Optional[SubscriptionHandler] = None

    def set_next(self, handler: SubscriptionHandler) -> SubscriptionHandler:
        """Добавить следующий обработчик в цепочке

        Args:
            handler (SubscriptionHandler)

        Returns:
            SubscriptionHandler
        """
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle_request(self, months: int) -> str:
        """Обработать запрос

        Args:
            months (int): количество месяцев, на которое продляется абонемент

        Returns:
            str
        """
        pass

    def _pass_to_next(self, months: int) -> str:
        """Передать обработку следующему обработчику в цепочке

        Args:
            months (int): количество месяцев, на которое продляется абонемент

        Raises:
            RenewalLimitExceededError

        Returns:
            str
        """
        if self._next_handler:
            return self._next_handler.handle_request(months)
        raise RenewalLimitExceededError(months)


class Administrator(SubscriptionHandler):
    """Администратор

    Args:
        SubscriptionHandler

    Returns:
        str
    """
    MAX_MONTHS = 1

    def handle_request(self, months: int) -> str:
        """Обработать запрос

        Args:
            months (int): количество месяцев, на которое продляется абонемент

        Returns:
            str
        """
        if months <= self.MAX_MONTHS:
            return f"Администратор одобрил продление на {months} месяц(а)."
        else:
            print(f"Администратор: Не могу одобрить продление на {months} мес. (Лимит: {self.MAX_MONTHS}). Передаю дальше.")
            return self._pass_to_next(months)


class Manager(SubscriptionHandler):
    """Менеджер

    Args:
        SubscriptionHandler

    Returns:
        str
    """
    MAX_MONTHS = 3

    def handle_request(self, months: int) -> str:
        """Обработать запрос

        Args:
            months (int): количество месяцев, на которое продляется абонемент

        Returns:
            str
        """
        if months <= self.MAX_MONTHS:
            return f"Менеджер одобрил продление на {months} месяца(ев)."
        else:
            print(f"Менеджер: Не могу одобрить продление на {months} мес. (Лимит: {self.MAX_MONTHS}). Передаю Директору.")
            return self._pass_to_next(months)


class Director(SubscriptionHandler):
    """Директор

    Args:
        SubscriptionHandler
    """
    
    def handle_request(self, months: int) -> str:
        """Обработать запрос

        Args:
            months (int): количество месяцев, на которое продляется абонемент

        Returns:
            str
        """
        return f"Директор одобрил продление на {months} месяца(ев)."