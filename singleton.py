# Problem Statement: Build a MetricsLogger for Stripe's Payment System
# Stripe runs millions of transactions per second and needs a way to log performance metrics (e.g., response time, failure rates, request volume) for different services.

# You are asked to implement a MetricsLogger class that:

# Is a Singleton — only one instance must exist in the system.
# Exposes a method log(metric_name: str, value: float) to log any metric.
# Stores all metrics internally (you can use a dictionary).
# Has a method get_metrics() to return the entire logged data.
# Must be thread-safe — multiple services may call it simultaneously.

from collections import defaultdict, deque
import threading
from concurrent.futures import ThreadPoolExecutor
import time
import copy
import numpy as np
from abc import ABC
import json

class Exporter(ABC):
    def flush(self, data):
        pass


class FileExporter(Exporter):

    def __init__(self, filepath):
        self.filepath = filepath

    def flush(self, data):
        with open(self.filepath, "w") as file:
            serializable_data = {k:list(v) for k,v in data.items()}
            file.write(json.dumps(serializable_data))


class ConsoleExporter(Exporter):

    def flush(self, data):
        print(data)


class MonitoringExported(Exporter):
    def __init__(self, platform):
        self.platform = platform

    def flush(self, data):
        self.platform.send(data)


class MetricsLogger:
    _instance = None
    _lock = threading.Lock()
    # def __init__(self, exporters:list) -> None:
    #     self.exporters = exporters

    def __new__(cls,exporters=None):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance.metrics = defaultdict(lambda: deque(maxlen=10000))  #
                cls._instance._metrics_lock = threading.Lock()
                cls._instance._exporters = exporters or []
        return cls._instance

    def log(self, metrics_name, value):
        with self._metrics_lock:
            self.metrics[metrics_name].append(value)

    def get_metrics(
        self,
    ):
        with self._metrics_lock:
            return dict(
                self.metrics
            )  # copy.deepcopy(dict(self.metrics)) (do deepcopy if you dont want you user to mutate internal state)

    def get_metrics_avg(self, metrics_name: str) -> float:
        with self._metrics_lock:
            try:
                metrics_values = self.metrics[metrics_name]
                return sum(metrics_values) / len(metrics_values)
            except ZeroDivisionError as err:
                print(f"No values are present for metrics {metrics_name}")

    def get_metrics_p95(self, metrics_name):
        with self._metrics_lock:
            metrics_values = self.metrics[metrics_name]
            return np.percentile(metrics_values, 95)

    def get_metrics_count(self, metrics_name):
        with self._metrics_lock:
            metrics_values = self.metrics[metrics_name]
            return len(metrics_values)
    
    def flush(self, data):
        for exp in self._exporters:
            exp.flush(data)

    

instances = []



# Thread target function
def simulate_thread_work(i):
    file_exp = FileExporter('./DesignPatterns/logs69.txt')
    console_exp = ConsoleExporter()
    logger = MetricsLogger([file_exp, console_exp])
    instances.append(id(logger))
    logger.log("payment_latency_ms", 90 + i * 2.5)
    logger.log("db_connect", 0.5 + i * 0.01)
    data = logger.get_metrics()
    logger.flush(data)
    return data


# Use ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(simulate_thread_work, i) for i in range(5)]

# Wait for threads to complete and gather results
for f in futures:
    result = f.result()

# print("\nFinal Metrics:")
# print(MetricsLogger().get_metrics())
# print("avg", MetricsLogger().get_metrics_avg("payment_latency_ms"))
# print("p95", MetricsLogger().get_metrics_p95("db_connect"))
# MetricsLogger().flush([file_exp, console_exp],MetricsLogger().get_metrics())
# logger = MetricsLogger()
# logger.log("latency", 100)

# snapshot = logger.get_metrics()
# snapshot["latency"].append(99999)
# print(logger.get_metrics())


class Logger:
    class IMPLogger:
        def test_method(self):
            print("I am a test method")

    instance = None

    def __init__(self):
        print("init dunder is called")
        # if Logger.instance is None:
        #     print("New instance creating")
        #     Logger.instance = Logger.IMPLogger()
        # else:
        #     print("Reusing old instance")

    def __new__(cls):
        print("new dunder is called")
        return super().__new__(cls)
        # if Logger.instance is None:
        #     print("New instance creating in new")
        #     Logger.instance = Logger.IMPLogger()
        # else:
        #     print("Reusing old instance in new")


# BAD
# logger1 = Logger()
# logger2 = Logger() #this will create a new file


# GOOD single logger everyone uses
# Logger()
# logger1 = Logger.instance
# logger1.test_method()
# good points of singleton
# guaranteed single instance ( fancy global variable )
# global access point
# controlled resource usage

# bad points of singleton
# hard to test (global state)
# need to be thread-safe (if used in multithreading)


class Animal:
    def speak(self):
        print("Animal speak")


class Dog(Animal):
    def speak(self):
        print("Dog speak")
        super().speak()


class GermanSpheferd(Dog):
    def speak(self):
        print("GermanSpheferd speak")
        super().speak()


# GermanSpheferddog = GermanSpheferd()
# GermanSpheferddog.speak()


# good implementation


class Logger:
    _instance = None
    variable = 10
    __pri = 90

    def __new__(cls):
        if cls._instance is None:
            print("creating new instance")
            cls._instance = super().__new__(cls)
        else:
            print("reusing old instance")
        return cls._instance

    def __init__(self):
        self.variable = 20
        print("In constructor")

    def test_method(self):
        self.variable += 1
        print(f"testing a method -> {self.variable}")


# logger1 = Logger()
# logger2 = Logger()
# logger1.test_method()
# logger2.test_method()
# print(logger2._Logger__pri)
