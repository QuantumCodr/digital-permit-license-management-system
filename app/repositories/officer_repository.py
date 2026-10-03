"""
------------------------------------------------------------
Program Name : Digital Permit & License Management System
Author       : QuantumCodr
Date         : 2026-10-02
Language     : Python
Module       : Officer Repository
Description  : Handles persistence and retrieval of
               LicensingOfficer objects using JSON storage.
------------------------------------------------------------
"""

import json

from app.models.licensing_officer import LicensingOfficer


class OfficerRepository:
    """Provides persistence operations for LicensingOfficer objects."""

    def __init__(self, file_path):
        self.file_path = file_path

    def generate_id(self):
        """Generate the next sequential officer ID."""
        officers = self._load()

        highest_number = 0

        for officer_id in officers:
            number = int(officer_id)

            if number > highest_number:
                highest_number = number

        return highest_number + 1

    def save(self, officer):
        """Save an officer to persistent storage."""
        officers = self._load()

        officers[str(officer.officer_id)] = {
            "officer_id": officer.officer_id,
            "name": officer.name,
            "department": officer.department,
        }

        self._write(officers)

    def find_by_id(self, officer_id):
        """Return an officer by ID, or None if not found."""
        officers = self._load()
        officer_data = officers.get(str(officer_id))

        if officer_data is None:
            return None

        return LicensingOfficer(
            officer_data["officer_id"],
            officer_data["name"],
            officer_data["department"],
        )

    def find_all(self):
        """Return all stored licensing officers."""
        officers = self._load()
        result = {}

        for officer_id, officer_data in officers.items():
            result[officer_id] = LicensingOfficer(
                officer_data["officer_id"],
                officer_data["name"],
                officer_data["department"],
            )

        return result

    def _load(self):
        """Load officers from JSON storage."""
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def _write(self, officers):
        """Write officers to JSON storage."""
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(officers, file, indent=4)