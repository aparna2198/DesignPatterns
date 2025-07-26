import threading
from collections import defaultdict
class MetricsLogger:
    _instances = {}
    _lock = threading.Lock()

    def __init__(self, component):
        self.component = component
        self.metrics = defaultdict(list)

    @classmethod
    def for_component(cls, component):
        with cls._lock:
            if component not in cls._instances:
                cls._instances[component] = MetricsLogger(component)
        return cls._instances[component]

    def log(self, metric_name, value):
        self.metrics[metric_name].append(value)

    def get_metrics(self):
        return dict(self.metrics)

payment_logger = MetricsLogger.for_component("payment")
auth_logger = MetricsLogger.for_component("auth")

payment_logger.log("latency_ms", 123)
auth_logger.log("error_rate", 0.01)

print(payment_logger.get_metrics())  # {'latency_ms': [123]}
print(auth_logger.get_metrics())     # {'error_rate': [0.01]}
