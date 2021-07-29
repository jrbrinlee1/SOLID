"""
SOLID Design Principles

Interface Segregation Principle: No client should be forced to depend on methods it does not use - role interfaces

Motivation:

Implementation:
"""

from abc import ABC, abstractmethod


# BAD
class MobilePhone(ABC):
    """
    Bad because not all kitchen appliances have a set temperature feature
    """

    @abstractmethod
    def voice(self):
        pass

    @abstractmethod
    def text(self):
        pass

    @abstractmethod
    def camera(self):
        pass


class BestMobilePhoneEverBad(MobilePhone):
    def voice(self):
        pass

    def text(self):
        pass

    def camera(self):
        pass


class OldSchoolPhoneBad(MobilePhone):
    def voice(self):
        pass

    def text(self):
        pass

    # ISSUE HERE: no camera on this phone
    def camera(self):
        raise NotImplementedError


# BETTER because we don't inherit things we don't need. Interfaces are as simple as possible
class Phone(ABC):
    @abstractmethod
    def voice(self):
        pass


class Text(ABC):
    @abstractmethod
    def text(self):
        pass


class Camera(ABC):
    @abstractmethod
    def photo(self):
        pass


class BestMobilePhoneEver(Phone, Text, Camera):
    def voice(self):
        pass

    def text(self):
        pass

    def photo(self):
        pass


class OldSchoolPhone(Phone, Text):
    def voice(self):
        pass

    def text(self):
        pass


