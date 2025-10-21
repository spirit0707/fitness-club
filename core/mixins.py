from __future__ import annotations
from datetime import datetime

class LoggingMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._log_file = "fitness_log.txt"
    
    def log_action(self, action: str, details: str = ""):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        class_name = self.__class__.__name__

        log_entry = f"[{timestamp}] {class_name}: {action}"
        if details:
            log_entry += f" | {details}"
        
        with open(self._log_file, "a", encoding="utf-8") as f:
            f.write(log_entry + "\n")
        
        print(f"ЛОГ: {log_entry}")
    
    def get_log_history(self) -> list[str]:
        try:
            with open(self._log_file, "r", encoding="utf-8") as f:
                return f.readlines()
        except FileNotFoundError:
            return []
        
class NotificationMixin:

    def send_notification(self, title: str, message: str, notification_type: str = "info"):
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
        with open("notifications.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {notification}\n")
    
    def send_class_cancellation(self, class_name: str, reason: str = ""):
        title = f"Тренировка '{class_name}' отменена"
        message = f"Тренировка '{class_name}' была отменена"
        if reason:
            message += f". Причина: {reason}"
        self.send_notification(title, message, "warning")
    
    def send_subscription_expiry(self, days_left: int):
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