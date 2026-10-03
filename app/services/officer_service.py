"""
------------------------------------------------------------
Program Name : Digital Permit & License Management System
Author       : QuantumCodr
Date         : 2026-10-02
Language     : Python
Module       : Officer Service
Description  : Handles application operations involving
               licensing officers.
------------------------------------------------------------
"""

from app.models.licensing_officer import LicensingOfficer


class OfficerService:
    """Provides application operations for licensing officers."""

    def __init__(self, officer_repository):
        self.officer_repository = officer_repository

    def register_officer(self, name, department):
        """Create and save a new licensing officer."""

        officer_id = self.officer_repository.generate_id()

        officer = LicensingOfficer(
            officer_id,
            name,
            department,
        )

        self.officer_repository.save(officer)

        return officer

    def get_officer(self, officer_id):
        """Return an officer by ID."""
        officer = self.officer_repository.find_by_id(officer_id)

        if officer is None:
            raise ValueError("Officer not found.")

        return officer

    def get_all_officers(self):
        """Return all registered licensing officers."""
        return self.officer_repository.find_all()