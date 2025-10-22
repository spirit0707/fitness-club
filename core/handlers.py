from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional

class SubscriptionHandler(ABC):

    _next_handler: Optional[SubscriptionHandler] = None

    def set_next(self, handler: SubscriptionHandler) -> SubscriptionHandler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle_request(self, months: int) -> str:
        pass

    def _pass_to_next(self, months: int) -> str:
        if self._next_handler:
            return self._next_handler.handle_request(months)
        from core.exceptions import RenewalLimitExceededError
        raise RenewalLimitExceededError(months)


class Administrator(SubscriptionHandler):
    MAX_MONTHS = 1

    def handle_request(self, months: int) -> str:
        if months <= self.MAX_MONTHS:
            return f"Администратор одобрил продление на {months} месяц(а)."
        else:
            print(f"Администратор: Не могу одобрить продление на {months} мес. (Лимит: {self.MAX_MONTHS}). Передаю дальше.")
            return self._pass_to_next(months)


class Manager(SubscriptionHandler):
    MAX_MONTHS = 3

    def handle_request(self, months: int) -> str:
        if months <= self.MAX_MONTHS:
            return f"Менеджер одобрил продление на {months} месяца(ев)."
        else:
            print(f"Менеджер: Не могу одобрить продление на {months} мес. (Лимит: {self.MAX_MONTHS}). Передаю Директору.")
            return self._pass_to_next(months)


class Director(SubscriptionHandler):
    def handle_request(self, months: int) -> str:
        return f"Директор одобрил продление на {months} месяца(ев)."