import functools
from core.exceptions import PermissionDeniedError

def check_access(func):
    """Проверка прав

    Args:
        func (function): декорируемая функция

    Raises:
        PermissionDeniedError

    Returns:
        any: результат работы декорируемой функции
    """
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        if (args[1].permission == 0):
            raise PermissionDeniedError(func.__name__)

        return func(*args, **kwargs)
    return wrapper_decorator