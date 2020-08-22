import uuid
from datetime import datetime
from enum import Enum


class ProviderI:
    name = ""

    def pay(self, payment):
        raise NotImplementedError


class Money:
    def __init__(self, value, currency):
        self.__value = value
        self.__currency = currency

    @property
    def get_value(self):
        return self.__value

    @property
    def get_currency(self):
        return self.__currency


class Status(Enum):
    FAILED = -1
    CREATED = 1
    AUTHORIZED = 2
    COMPLETED = 3


class Payment:
    def __init__(self, value, currency="EUR"):
        self.money = Money(value, currency)
        self.id = uuid.uuid1()
        self.created_at = datetime.now()
        self.status = Status.CREATED


def pay(payment, provider):
    return provider.pay(payment)
