"""
------------------------------------------------------------
Program Name : Digital Permit & License Management System
Author       : QuantumCodr
Date         : 2026-10-02
Language     : Python
Module       : Applicant Repository
Description  : Handles persistence and retrieval of Applicant
               objects using JSON storage.
------------------------------------------------------------
"""

import json

from app.models.applicant import Applicant


class ApplicantRepository:
    """Provides persistence operations for Applicant objects."""

    def __init__(self, file_path):
        self.file_path = file_path

    def generate_id(self):
        """Generate the next sequential applicant ID."""
        applicants = self._load()

        highest_number = 0

        for applicant_id in applicants:
            number = int(applicant_id)

            if number > highest_number:
                highest_number = number

        return highest_number + 1

    def save(self, applicant):
        """Save an applicant to persistent storage."""
        applicants = self._load()

        applicants[str(applicant.applicant_id)] = {
            "applicant_id": applicant.applicant_id,
            "name": applicant.name,
            "address": applicant.address,
        }

        self._write(applicants)

    def find_by_id(self, applicant_id):
        """Return an applicant by ID, or None if not found."""
        applicants = self._load()
        applicant_data = applicants.get(str(applicant_id))

        if applicant_data is None:
            return None

        return Applicant(
            applicant_data["applicant_id"],
            applicant_data["name"],
            applicant_data["address"],
        )

    def find_all(self):
        """Return all stored applicants."""
        applicants = self._load()
        result = {}

        for applicant_id, applicant_data in applicants.items():
            result[applicant_id] = Applicant(
                applicant_data["applicant_id"],
                applicant_data["name"],
                applicant_data["address"],
            )

        return result

    def _load(self):
        """Load applicants from JSON storage."""
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def _write(self, applicants):
        """Write applicants to JSON storage."""
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(applicants, file, indent=4)