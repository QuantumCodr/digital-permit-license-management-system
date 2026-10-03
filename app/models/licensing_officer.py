"""
------------------------------------------------------------
Program Name : Digital Permit & License Management System
Author       : QuantumCodr
Date         : 2026-10-02
Language     : Python
Module       : Licensing Officer Model
Description  : Represents a government officer responsible
               for processing permits and licenses.
------------------------------------------------------------
"""


class LicensingOfficer:
    """Represents an officer who processes permits and licenses."""

    def __init__(self, officer_id, name, department):
        self.__officer_id = officer_id
        self.name = name
        self.department = department

    @property
    def officer_id(self):
        """Return the officer's unique identifier."""
        return self.__officer_id

    def display_info(self):
        """Return basic officer information."""
        return (
            f"Officer ID: {self.officer_id}\n"
            f"Name: {self.name}\n"
            f"Department: {self.department}"
        )