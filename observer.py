from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, event_data):
        pass

class Email(Observer):
    def update(self, event_data):
        print(f"Email Notifying users for {event_data}")

class SMS(Observer):
    def update(self, event_data):
        print(f"SMS Notifying users for {event_data}")

class AnalyticsService(Observer):
    def update(self, event_data):
        print(f"AnalyticsService Notifying users for {event_data}")

class NotificationService:
    def __init__(self):
        self.observers = []
    
    def attach(self, observer_name:Observer):
        self.observers.append(observer_name)
    
    def detach(self, observer_name:Observer):
        self.observers.remove(observer_name)
    
    def notify(self, event_data):
        for obs in self.observers:
            obs.update(event_data)

notification_service = NotificationService()
notification_service.attach(Email())
notification_service.attach(SMS())
notification_service.attach(AnalyticsService())
notification_service.notify("This is amazing!")

