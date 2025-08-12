from abc import ABC, abstractmethod
from loguru import logger
class Payment(ABC):
    @abstractmethod
    def pay():
        pass

class CreditCardPayment(Payment):
    def pay(self):
        print("Paying using credit card")

class DebitCardPayment(Payment):
    def pay(self):
        print("Paying using debit card")

class PaymentFactory:
    @staticmethod
    def get_payment_method(payment_method:str):
        if payment_method=="credit":
            return CreditCardPayment()
        elif payment_method=="debit":
            return DebitCardPayment()
        else:
            logger.error("payment method is not know")
            raise ValueError("payment method is not know")

payment_method = PaymentFactory.get_payment_method('debit')
payment_method.pay()
    
