"""
SOLID Design Principles

Open Closed Principle: Open for extension and closed for modification

Motivation: Maintainability, flexibility & extensibility

Implementation:
"""


class BadStorageLocker:
    """
    Bad because we're going to need to modify code elsewhere when extending
    """

    def authenticate(self, client):
        if client == "aws":
            # code to auth aws
            pass
        elif client == 'azure':
            # code to auth azure
            pass

        return client

    def upload(self, client):
        if client == "aws":
            # code to upload to aws
            pass
        elif client == 'azure':
            # code to upload azure
            pass


from abc import ABC, abstractmethod


class Authenticater(ABC):
    @abstractmethod
    def authenticate(self):
        pass


class Uploader(ABC):
    @abstractmethod
    def upload_file(self):
        pass


class Aws(Authenticater, Uploader):

    def authenticate(self):
        # code to auth aws
        pass

    def upload_file(self):
        # code to upload to aws
        pass


class Azure(Authenticater, Uploader):

    def authenticate(self):
        # code to auth azure
        pass

    def upload_file(self):
        # code to upload to azure
        pass
