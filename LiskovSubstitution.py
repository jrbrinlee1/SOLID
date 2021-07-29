"""
SOLID Design Principles

Liskov Substitution Principle: Derived class can assume the place of its super class, and everything should work

Motivation:

Implementation:
"""

from abc import ABC, abstractmethod


# BAD
class KitchenAppliance(ABC):
    """
    Bad because not all kitchen appliances have a set temperature feature
    """

    @abstractmethod
    def on(self):
        pass

    @abstractmethod
    def off(self):
        pass

    @abstractmethod
    def set_temperature(self):
        pass


class Oven(KitchenAppliance):
    def off(self):
        pass

    def on(self):
        # code to turn oven on
        pass

    def set_temperature(self):
        # code to set temp
        pass


class Juicer(KitchenAppliance):
    def off(self):
        pass

    def on(self):
        # code to turn oven on
        pass

    """
    ISSUE HERE: no set temperature
    """


# BETTER
class KitchenAppliance(ABC):
    """
    Better because we sub class can always be substituted for super class
    """

    @abstractmethod
    def on(self):
        pass

    @abstractmethod
    def off(self):
        pass


class KitchenApplianceWithTemp(KitchenAppliance):

    @abstractmethod
    def set_temperature(self):
        pass


class Oven(KitchenApplianceWithTemp):
    def off(self):
        # code to turn oven off
        pass

    def on(self):
        # code to turn oven on
        pass

    def set_temperature(self):
        # code to set temp
        pass


class Juicer(KitchenAppliance):
    def off(self):
        # code to turn Juicer off
        pass

    def on(self):
        # code to turn Juicer on
        pass

