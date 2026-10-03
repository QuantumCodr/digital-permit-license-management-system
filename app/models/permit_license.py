"""
------------------------------------------------------------
Program Name : Digital Permit & License Management System
Author       : QuantumCodr
Date         : 2026-10-02
Language     : Python
Module       : Permit License Model
Description  : Represents a government permit or license
               and its lifecycle within the system.
------------------------------------------------------------
"""


class PermitLicense:
    """Represents a permit or license application."""

    PENDING = "Pending"
    APPROVED = "Approved"
    EXPIRED = "Expired"

    VALID_TYPES = {
        "Driving License": "Driving License",
        "Business Permit": "Business Permit",
        "Building Permit": "Building Permit",
        "Trading License": "Trading License",
        "Other": "Other",
    }

    def __init__(
        self,
        permit_license_id,
        applicant_id,
        permit_type,
        purpose,
    ):
        self.__permit_license_id = permit_license_id
        self.applicant_id = applicant_id
        self.permit_type = permit_type
        self.purpose = purpose
        self.status = self.PENDING
        self.officer_id = None

    @property
    def permit_license_id(self):
        """Return the permit or license unique identifier."""
        return self.__permit_license_id

    def assign_officer(self, officer_id):
        """Assign an officer and move the application under review."""
        self.officer_id = officer_id

    def approve(self):
        """Approve the permit or license."""
        self.status = self.APPROVED

    def expire(self):
        """Mark the permit or license as expired."""
        self.status = self.EXPIRED

    @classmethod
    def create_basic(
        cls,
        permit_license_id,
        applicant_id,
        permit_type,
        purpose,
    ):
        """Create a permit or license using its default status."""
        return cls(
            permit_license_id,
            applicant_id,
            permit_type,
            purpose,
        )

    @staticmethod
    def is_valid_type(permit_type):
        """Check whether a permit or license type is supported."""
        return permit_type in PermitLicense.VALID_TYPES

    def display_info(self):
        """Return basic permit or license information."""
        officer = (
            self.officer_id
            if self.officer_id is not None
            else "Not assigned"
        )

        return (
            f"Permit/License ID: {self.permit_license_id}\n"
            f"Applicant ID: {self.applicant_id}\n"
            f"Type: {self.permit_type}\n"
            f"Purpose: {self.purpose}\n"
            f"Status: {self.status}\n"
            f"Officer ID: {officer}"
        )