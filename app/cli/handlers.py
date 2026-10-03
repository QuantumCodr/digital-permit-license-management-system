"""
------------------------------------------------------------
Program Name : Digital Permit & License Management System
Author       : QuantumCodr
Date         : 2026-10-02
Language     : Python
Module       : CLI Handlers
Description  : Handles user input and coordinates command-
               line operations through application services.
------------------------------------------------------------
"""


class Handlers:
    """Handles command-line operations for the application."""

    def __init__(
        self,
        applicant_service,
        permit_license_service,
        officer_service,
    ):
        self.applicant_service = applicant_service
        self.permit_license_service = permit_license_service
        self.officer_service = officer_service

    def register_applicant(self):
        """Register a new applicant."""
        print("\n--- Register Applicant ---")

        name = input("Enter applicant name: ").strip()
        address = input("Enter address: ").strip()

        if not name:
            print("Error: Applicant name is required.")
            return

        if not address:
            print("Error: Address is required.")
            return

        try:
            applicant = self.applicant_service.register_applicant(
                name,
                address,
            )

            print("\nApplicant registered successfully.")
            print(f"Applicant ID: APP-{applicant.applicant_id:04d}")

        except ValueError as error:
            print(f"Error: {error}")

    def register_officer(self):
        """Register a new licensing officer."""
        print("\n--- Register Licensing Officer ---")

        name = input("Enter officer name: ").strip()
        department = input("Enter department: ").strip()

        if not name:
            print("Error: Officer name is required.")
            return

        if not department:
            print("Error: Department is required.")
            return

        try:
            officer = self.officer_service.register_officer(
                name,
                department,
            )

            print("\nLicensing officer registered successfully.")
            print(f"Officer ID: OFF-{officer.officer_id:04d}")

        except ValueError as error:
            print(f"Error: {error}")

    def submit_application(self):
        """Submit a new permit or license application."""
        print("\n--- Submit Permit/License Application ---")

        try:
            applicant_id = self._read_id(
                "Enter applicant ID: "
            )

            permit_type = self._get_permit_type()

            purpose = input("Enter purpose: ").strip()

            if not purpose:
                raise ValueError("Purpose is required.")

            permit_license = (
                self.permit_license_service.submit_application(
                    applicant_id,
                    permit_type,
                    purpose,
                )
            )

            print("\nApplication submitted successfully.")
            print(
                "Permit/License ID: "
                f"LIC-{permit_license.permit_license_id:04d}"
            )
            print(f"Status: {permit_license.status}")

        except ValueError as error:
            print(f"Error: {error}")

    def view_permit_license(self):
        """Display a permit or license by ID."""
        print("\n--- View Permit/License ---")

        try:
            permit_license_id = self._read_id(
                "Enter permit/license ID: "
            )

            permit_license = (
                self.permit_license_service.get_permit_license(
                    permit_license_id
                )
            )

            self._display_permit_license(permit_license)

        except ValueError as error:
            print(f"Error: {error}")

    def view_all_permits_licenses(self):
        """Display all stored permits and licenses."""
        print("\n--- All Permits/Licenses ---")

        permits_licenses = (
            self.permit_license_service.get_all_permits_licenses()
        )

        if not permits_licenses:
            print("No permits or licenses found.")
            return

        for permit_license in permits_licenses.values():
            self._display_permit_license(permit_license)
            print("-" * 60)

    def assign_application(self):
        """Assign a permit or license application to an officer."""
        print("\n--- Assign Application ---")

        try:
            permit_license_id = self._read_id(
                "Enter permit/license ID: "
            )

            officer_id = self._read_id(
                "Enter officer ID: "
            )

            permit_license = (
                self.permit_license_service.assign_application(
                    permit_license_id,
                    officer_id,
                )
            )

            print("\nApplication assigned successfully.")
            print(
                "Permit/License ID: "
                f"LIC-{permit_license.permit_license_id:04d}"
            )
            print(
                "Officer ID: "
                f"OFF-{permit_license.officer_id:04d}"
            )

        except ValueError as error:
            print(f"Error: {error}")

    def approve_application(self):
        """Approve a permit or license application."""
        print("\n--- Approve Application ---")

        try:
            permit_license_id = self._read_id(
                "Enter permit/license ID: "
            )

            permit_license = (
                self.permit_license_service.approve_application(
                    permit_license_id
                )
            )

            print("\nApplication approved successfully.")
            print(
                "Permit/License ID: "
                f"LIC-{permit_license.permit_license_id:04d}"
            )
            print(f"Status: {permit_license.status}")

        except ValueError as error:
            print(f"Error: {error}")

    def expire_permit_license(self):
        """Mark an approved permit or license as expired."""
        print("\n--- Expire Permit/License ---")

        try:
            permit_license_id = self._read_id(
                "Enter permit/license ID: "
            )

            permit_license = (
                self.permit_license_service.expire_permit_license(
                    permit_license_id
                )
            )

            print("\nPermit/License expired successfully.")
            print(
                "Permit/License ID: "
                f"LIC-{permit_license.permit_license_id:04d}"
            )
            print(f"Status: {permit_license.status}")

        except ValueError as error:
            print(f"Error: {error}")

    def view_applicants(self):
        """Display all registered applicants."""
        print("\n--- Applicants ---")

        applicants = self.applicant_service.get_all_applicants()

        if not applicants:
            print("No applicants found.")
            return

        for applicant in applicants.values():
            print(
                f"\nApplicant ID: APP-{applicant.applicant_id:04d}\n"
                f"Name: {applicant.name}\n"
                f"Address: {applicant.address}"
            )

    def view_officers(self):
        """Display all registered licensing officers."""
        print("\n--- Licensing Officers ---")

        officers = self.officer_service.get_all_officers()

        if not officers:
            print("No licensing officers found.")
            return

        for officer in officers.values():
            print(
                f"\nOfficer ID: OFF-{officer.officer_id:04d}\n"
                f"Name: {officer.name}\n"
                f"Department: {officer.department}"
            )

    @staticmethod
    def _read_id(prompt):
        """Read and validate a positive numeric ID."""
        value = input(prompt).strip()

        if not value:
            raise ValueError("ID is required.")

        try:
            identifier = int(value)
        except ValueError:
            raise ValueError("ID must be a number.")

        if identifier <= 0:
            raise ValueError("ID must be greater than zero.")

        return identifier

    @staticmethod
    def _get_permit_type():
        """Display and return a valid permit or license type."""
        print("\nPermit/License Types:")
        print("1. Driving License")
        print("2. Business Permit")
        print("3. Building Permit")
        print("4. Trading License")
        print("5. Other")

        choice = input("Select type: ").strip()

        permit_types = {
            "1": "Driving License",
            "2": "Business Permit",
            "3": "Building Permit",
            "4": "Trading License",
            "5": "Other",
        }

        permit_type = permit_types.get(choice)

        if permit_type is None:
            raise ValueError(
                "Invalid permit or license type selection."
            )

        return permit_type

    @staticmethod
    def _display_permit_license(permit_license):
        """Display permit or license information."""
        officer = (
            f"OFF-{permit_license.officer_id:04d}"
            if permit_license.officer_id is not None
            else "Not assigned"
        )

        print(
            f"\nPermit/License ID: "
            f"LIC-{permit_license.permit_license_id:04d}\n"
            f"Applicant ID: APP-{permit_license.applicant_id:04d}\n"
            f"Type: {permit_license.permit_type}\n"
            f"Purpose: {permit_license.purpose}\n"
            f"Status: {permit_license.status}\n"
            f"Officer ID: {officer}"
        )