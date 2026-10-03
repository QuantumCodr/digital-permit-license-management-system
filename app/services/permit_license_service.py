"""
------------------------------------------------------------
Program Name : Digital Permit & License Management System
Author       : QuantumCodr
Date         : 2026-10-02
Language     : Python
Module       : Permit License Service
Description  : Handles permit and license application,
               assignment, approval, expiration, and retrieval.
------------------------------------------------------------
"""

from app.models.permit_license import PermitLicense


class PermitLicenseService:
    """Provides application operations for permits and licenses."""

    def __init__(
        self,
        permit_license_repository,
        applicant_repository,
        officer_repository,
    ):
        self.permit_license_repository = permit_license_repository
        self.applicant_repository = applicant_repository
        self.officer_repository = officer_repository

    def submit_application(
        self,
        applicant_id,
        permit_type,
        purpose,
    ):
        """Create and save a new permit or license application."""

        applicant = self.applicant_repository.find_by_id(applicant_id)

        if applicant is None:
            raise ValueError("Applicant not found.")

        if not PermitLicense.is_valid_type(permit_type):
            raise ValueError("Invalid permit or license type.")

        permit_license_id = (
            self.permit_license_repository.generate_id()
        )

        permit_license = PermitLicense.create_basic(
            permit_license_id,
            applicant_id,
            permit_type,
            purpose,
        )

        self.permit_license_repository.save(permit_license)

        return permit_license

    def get_permit_license(self, permit_license_id):
        """Return a permit or license by ID."""
        permit_license = (
            self.permit_license_repository.find_by_id(
                permit_license_id
            )
        )

        if permit_license is None:
            raise ValueError("Permit or license not found.")

        return permit_license

    def get_all_permits_licenses(self):
        """Return all permits and licenses."""
        return self.permit_license_repository.find_all()

    def assign_application(self, permit_license_id, officer_id):
        """Assign a permit or license application to an officer."""

        permit_license = self.get_permit_license(
            permit_license_id
        )

        officer = self.officer_repository.find_by_id(officer_id)

        if officer is None:
            raise ValueError("Officer not found.")

        if permit_license.status == PermitLicense.EXPIRED:
            raise ValueError(
                "An expired permit or license cannot be assigned."
            )

        if permit_license.status == PermitLicense.APPROVED:
            raise ValueError(
                "An approved permit or license cannot be assigned."
            )

        permit_license.assign_officer(officer_id)

        self.permit_license_repository.save(permit_license)

        return permit_license

    def approve_application(self, permit_license_id):
        """Approve a permit or license assigned to an officer."""

        permit_license = self.get_permit_license(
            permit_license_id
        )

        if permit_license.officer_id is None:
            raise ValueError(
                "A permit or license must be assigned to an officer "
                "before it can be approved."
            )

        if permit_license.status == PermitLicense.APPROVED:
            raise ValueError(
                "Permit or license is already approved."
            )

        if permit_license.status == PermitLicense.EXPIRED:
            raise ValueError(
                "An expired permit or license cannot be approved."
            )

        permit_license.approve()

        self.permit_license_repository.save(permit_license)

        return permit_license

    def expire_permit_license(self, permit_license_id):
        """Mark an approved permit or license as expired."""

        permit_license = self.get_permit_license(
            permit_license_id
        )

        if permit_license.status != PermitLicense.APPROVED:
            raise ValueError(
                "Only an approved permit or license can expire."
            )

        permit_license.expire()

        self.permit_license_repository.save(permit_license)

        return permit_license