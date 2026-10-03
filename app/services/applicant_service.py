"""
------------------------------------------------------------
Program Name : Digital Permit & License Management System
Author       : QuantumCodr
Date         : 2026-10-02
Language     : Python
Module       : Applicant Service
Description  : Handles application operations involving
               applicants.
------------------------------------------------------------
"""

from app.models.applicant import Applicant


class ApplicantService:
    """Provides application operations for applicants."""

    def __init__(self, applicant_repository):
        self.applicant_repository = applicant_repository

    def register_applicant(self, name, address):
        """Create and save a new applicant."""

        applicant_id = self.applicant_repository.generate_id()

        applicant = Applicant(
            applicant_id,
            name,
            address,
        )

        self.applicant_repository.save(applicant)

        return applicant

    def get_applicant(self, applicant_id):
        """Return an applicant by ID."""
        applicant = self.applicant_repository.find_by_id(applicant_id)

        if applicant is None:
            raise ValueError("Applicant not found.")

        return applicant

    def get_all_applicants(self):
        """Return all registered applicants."""
        return self.applicant_repository.find_all()