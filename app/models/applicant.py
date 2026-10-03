"""
------------------------------------------------------------
Program Name : Digital Permit & License Management System
Author       : QuantumCodr
Date         : 2026-10-02
Language     : Python
Module       : Applicant Model
Description  : Represents an applicant who applies for a
               government permit or license.
------------------------------------------------------------
"""


class Applicant:
    """Represents an applicant in the permit and license system."""

    def __init__(self, applicant_id, name, address):
        self.__applicant_id = applicant_id
        self.name = name
        self.address = address

    @property
    def applicant_id(self):
        """Return the applicant's unique identifier."""
        return self.__applicant_id

    def display_info(self):
        """Return basic applicant information."""
        return (
            f"Applicant ID: {self.applicant_id}\n"
            f"Name: {self.name}\n"
            f"Address: {self.address}"
        )