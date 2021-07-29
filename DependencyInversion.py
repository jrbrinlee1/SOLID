"""
SOLID Design Principles

Dependency Inversion Principle: High-level modules should not depend on low-level modules. Both should depend on
abstraction. Abstraction should not depend on details. Details should depend on abstractions.

Motivation:

Implementation:
"""

from enum import Enum


# BAD because we are married to the list data type in club membership
class ClubsBad(Enum):
    SWIM_CLUB = 1
    CYCLE_CLUB = 2
    RUN_CLUB = 3


class StudentBad:
    def __init__(self, name):
        self.name = name


class ClubMembershipsBad:
    def __init__(self):
        self.club_memberships = []

    def add_club_membership(self, student, club):
        self.club_memberships.append((student, club))


class InspectMembershipsBad:
    def __init__(self, student_club_memberships):
        memberships = student_club_memberships.club_memberships

        for member in memberships:
            if member[1] == Clubs.SWIM_CLUB:
                print(f"{member[0].name} is in the SWIM club.")
            elif member[1] == Clubs.CYCLE_CLUB:
                print(f"{member[0].name} is in the CYCLE club.")
            if member[1] == Clubs.RUN_CLUB:
                print(f"{member[0].name} is in the RUN club.")


from abc import ABC, abstractmethod


# Better because high level module doesn't depend on low level
class Clubs(Enum):
    SWIM_CLUB = 1
    CYCLE_CLUB = 2
    RUN_CLUB = 3


class Student:
    def __init__(self, name):
        self.name = name


class ClubMembershipLookup:
    @abstractmethod
    def find_all_students_from_club(self, club):
        pass


class ClubMemberships(ClubMembershipLookup):
    def __init__(self):
        self.club_memberships = []

    def add_club_membership(self, student, club):
        self.club_memberships.append((student, club))

    def find_all_students_from_club(self, club):
        for member in self.club_memberships:
            if member[1] == club:
                yield member[0].name


class InspectMemberships:
    def __init__(self, club_memberships_lookup):
        for student in club_memberships_lookup.find_all_students_from_club(Clubs.SWIM_CLUB):
            print(f"{student} is in the SWIM club")

        for student in club_memberships_lookup.find_all_students_from_club(Clubs.RUN_CLUB):
            print(f"{student} is in the RUN club")

        for student in club_memberships_lookup.find_all_students_from_club(Clubs.CYCLE_CLUB):
            print(f"{student} is in the CYCLE club")