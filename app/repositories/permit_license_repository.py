"""
------------------------------------------------------------
Program Name : Digital Permit & License Management System
Author       : QuantumCodr
Date         : 2026-10-02
Language     : Python
Module       : Permit License Repository
Description  : Handles persistence and retrieval of
               PermitLicense objects using JSON storage.
------------------------------------------------------------
"""

import json

from app.models.permit_license import PermitLicense


class PermitLicenseRepository:
    """Provides persistence operations for PermitLicense objects."""

    def __init__(self, file_path):
        self.file_path = file_path

    def generate_id(self):
        """Generate the next sequential permit or license ID."""
        permits_licenses = self._load()

        highest_number = 0

        for permit_license_id in permits_licenses:
            number = int(permit_license_id)

            if number > highest_number:
                highest_number = number

        return highest_number + 1

    def save(self, permit_license):
        """Save a permit or license to persistent storage."""
        permits_licenses = self._load()

        permits_licenses[str(
            permit_license.permit_license_id
        )] = {
            "permit_license_id": permit_license.permit_license_id,
            "applicant_id": permit_license.applicant_id,
            "permit_type": permit_license.permit_type,
            "purpose": permit_license.purpose,
            "status": permit_license.status,
            "officer_id": permit_license.officer_id,
        }

        self._write(permits_licenses)

    def find_by_id(self, permit_license_id):
        """Return a permit or license by ID, or None if not found."""
        permits_licenses = self._load()

        permit_license_data = permits_licenses.get(
            str(permit_license_id)
        )

        if permit_license_data is None:
            return None

        permit_license = PermitLicense(
            permit_license_data["permit_license_id"],
            permit_license_data["applicant_id"],
            permit_license_data["permit_type"],
            permit_license_data["purpose"],
        )

        permit_license.status = permit_license_data["status"]
        permit_license.officer_id = permit_license_data["officer_id"]

        return permit_license

    def find_all(self):
        """Return all stored permits and licenses."""
        permits_licenses = self._load()
        result = {}

        for permit_license_id, permit_license_data in (
            permits_licenses.items()
        ):
            permit_license = PermitLicense(
                permit_license_data["permit_license_id"],
                permit_license_data["applicant_id"],
                permit_license_data["permit_type"],
                permit_license_data["purpose"],
            )

            permit_license.status = permit_license_data["status"]
            permit_license.officer_id = permit_license_data["officer_id"]

            result[permit_license_id] = permit_license

        return result

    def _load(self):
        """Load permits and licenses from JSON storage."""
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def _write(self, permits_licenses):
        """Write permits and licenses to JSON storage."""
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(permits_licenses, file, indent=4)