class SubscriptionError(Exception):
    pass

class RenewalLimitExceededError(SubscriptionError):
    def __init__(self, requested_months: int):
        self.requested_months = requested_months
        super().__init__(f"Запрос на продление на {requested_months} месяцев не может быть обработан ни одним звеном в цепочке.")

class ClassFullError(Exception):
    def __init__(self, class_name: str):
        self.class_name = class_name
        super().__init__(f"Тренировка '{class_name}' переполнена. Превышена вместимость зала.")