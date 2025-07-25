# Problem Statement: Build a MetricsLogger for Stripe's Payment System
# Stripe runs millions of transactions per second and needs a way to log performance metrics (e.g., response time, failure rates, request volume) for different services.

# You are asked to implement a MetricsLogger class that:

# Is a Singleton — only one instance must exist in the system.
# Exposes a method log(metric_name: str, value: float) to log any metric.
# Stores all metrics internally (you can use a dictionary).
# Has a method get_metrics() to return the entire logged data.
# Must be thread-safe — multiple services may call it simultaneously.

from collections import defaultdict
import threading
from concurrent.futures import ThreadPoolExecutor
import time

class MetricsLogger:
    _instance = None
    _lock = threading.Lock()
    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance.metrics = defaultdict(list)
                cls._instance._metrics_lock = threading.Lock()
        return cls._instance
    
    def log(self, metrics_name, value):
        with self._metrics_lock:
            self.metrics[metrics_name].append(value)
    
    def get_metrics(self):
        with self._metrics_lock:
            return dict(self.metrics)

instances = []
# Thread target function
def simulate_thread_work(i):
    logger = MetricsLogger()
    instances.append(id(logger))
    logger.log("payment_latency_ms", 90 + i * 2.5)
    logger.log("db_connect", 0.5 + i * 0.01)
    return logger.get_metrics()

# Use ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(simulate_thread_work, i) for i in range(5)]

# Wait for threads to complete and gather results
for f in futures:
    result = f.result()

print("\nFinal Metrics:")
print(MetricsLogger().get_metrics())












































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


#BAD
# logger1 = Logger()
# logger2 = Logger() #this will create a new file 


#GOOD single logger everyone uses
# Logger()
# logger1 = Logger.instance
# logger1.test_method()
#good points of singleton
    #guaranteed single instance ( fancy global variable )
    # global access point
    # controlled resource usage

#bad points of singleton
    #hard to test (global state)
    #need to be thread-safe (if used in multithreading)


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


#good implementation

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
        self.variable+=1
        print(f"testing a method -> {self.variable}")

# logger1 = Logger()
# logger2 = Logger()
# logger1.test_method()
# logger2.test_method()
# print(logger2._Logger__pri)







