import uuid
from datetime import datetime
from enum import Enum
from iso4217 import Currency
from decimal import Decimal


class ProviderI:
    """
    Interface for provider object

    Args:
        payment: Instance of class Payment
    """
    name = ""

    def pay(self, payment):
        raise NotImplementedError


class Money:
    """
    Read-only class used as representation of money in Payment class

    Args:
        value: Decimal
        currency: string
    """
    def __init__(self, value, currency):
        self.__value = Decimal(value)
        self.__currency = currency

    @staticmethod
    def __verify_currency(currency):
        currency = str(currency).upper()
        Currency(currency)
        return currency

    @property
    def get_value(self):
        return self.__value

    @property
    def get_currency(self):
        return self.__currency


class Status(Enum):
    """
    Enumerator class for Status of Payment
    """
    FAILED = -1
    CREATED = 1
    COMPLETED = 2


class Payment:
    """
    Class to represent one instance of payment

    Args:
        value: string
        currency: string
        created_at: datetime
    """
    def __init__(self, value, currency="EUR", created_at=datetime.now()):
        self.money = Money(value, currency)
        self.id = uuid.uuid1()
        self.transaction_id = None
        self.created_at = created_at
        self.status = Status.CREATED

    @classmethod
    def from_payment(cls, payment):
        return Payment(payment.value, payment.currency, payment.created_at)


def pay(payment, provider, repository):
    payment = provider.pay(payment)
    repository.save(payment)
