class SubscriptionError(Exception):
    """Базовый класс для ошибок подписки

    Args:
        Exception (class)
    """
    pass

class RenewalLimitExceededError(SubscriptionError):
    """Ошибка продления абонемента

    Args:
        SubscriptionError (class)
    """
    def __init__(self, requested_months: int):
        self.requested_months = requested_months
        super().__init__(f"Запрос на продление на {requested_months} месяцев не может быть обработан ни одним звеном в цепочке.")

class ClassFullError(Exception):
    """Нет мест в тренировке

    Args:
        Exception
    """
    def __init__(self, class_name: str):
        self.class_name = class_name
        super().__init__(f"Тренировка '{class_name}' переполнена. Превышена вместимость зала.")

class PermissionDeniedError(Exception):
    """Недостаточно прав для выполения какого-то действия

    Args:
        Exception
    """
    def __init__(self, func_name: str):
        super().__init__(f"Недостаточно прав для выполнения '{func_name}'")