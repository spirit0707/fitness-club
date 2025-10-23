from __future__ import annotations
from datetime import datetime
import logging
from logging import config
import json

class LoggingMixin:
    """Миксин для логирования
    """
    LOGGING_DIR = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        with open('config/logger.json') as f:
            config.dictConfig(json.load(f))
        self._logger = logging.getLogger()
    
    def log_action(self, action: str, details: str = ""):
        """Логирование действия

        Args:
            action (str): действие
            details (str, optional): дополнительные данные. Defaults to "".
        """
        self._logger.info('%s | %s', action, details)
        
class NotificationMixin:
    """Миксин для отправки уведомлений
    """

    def send_notification(self, title: str, message: str, notification_type: str = "info"):
        """Отправка уведомления

        Args:
            title (str): Заголовок
            message (str): текст уведомления
            notification_type (str, optional): тип уведомления. Defaults to "info".
        """
        icons = {
            "info": "ℹ️",
            "warning": "⚠️", 
            "error": "❌",
            "success": "✅"
        }
        
        icon = icons.get(notification_type, "📢")
        notification = f"{icon} УВЕДОМЛЕНИЕ: {title}\n   {message}"
        
        print(notification)
        self._save_notification(notification)
    
    def _save_notification(self, notification: str):
        """poor man's message queue

        Args:
            notification (str): уведомление
        """
        with open("notifications.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {notification}\n")
    
    def send_class_cancellation(self, class_name: str, reason: str = ""):
        """Отправка уведомления об отмене тренировки

        Args:
            class_name (str): название тренировки
            reason (str, optional): причина отмены. Defaults to "".
        """
        title = f"Тренировка '{class_name}' отменена"
        message = f"Тренировка '{class_name}' была отменена"
        if reason:
            message += f". Причина: {reason}"
        self.send_notification(title, message, "warning")
    
    def send_subscription_expiry(self, days_left: int):
        """Отправка уведомления об истечении срока действия абонемента

        Args:
            days_left (int): кол-во дней до истечения срока действия абонемента
        """
        title = "Срок действия абонемента"
        if days_left == 0:
            message = "Ваш абонемент истекает сегодня!"
            notification_type = "error"
        elif days_left <= 7:
            message = f"Ваш абонемент истекает через {days_left} дней"
            notification_type = "warning"
        else:
            message = f"До истечения абонемента осталось {days_left} дней"
            notification_type = "info"
        
        self.send_notification(title, message, notification_type)