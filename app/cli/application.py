"""
------------------------------------------------------------
Program Name : Digital Permit & License Management System
Author       : QuantumCodr
Date         : 2026-10-02
Language     : Python
Module       : CLI Application
Description  : Configures and runs the command-line
               application.
------------------------------------------------------------
"""

from pathlib import Path

from app.cli.handlers import Handlers
from app.cli.menu import Menu
from app.repositories.applicant_repository import (
    ApplicantRepository,
)
from app.repositories.officer_repository import OfficerRepository
from app.repositories.permit_license_repository import (
    PermitLicenseRepository,
)
from app.services.applicant_service import ApplicantService
from app.services.officer_service import OfficerService
from app.services.permit_license_service import (
    PermitLicenseService,
)


class Application:
    """Controls the command-line application lifecycle."""

    def __init__(self):
        self.data_directory = (
            Path(__file__).resolve().parents[2] / "data"
        )

        self.data_directory.mkdir(exist_ok=True)

        applicant_repository = ApplicantRepository(
            self.data_directory / "applicants.json"
        )

        officer_repository = OfficerRepository(
            self.data_directory / "officers.json"
        )

        permit_license_repository = PermitLicenseRepository(
            self.data_directory / "permits_licenses.json"
        )

        applicant_service = ApplicantService(
            applicant_repository
        )

        officer_service = OfficerService(
            officer_repository
        )

        permit_license_service = PermitLicenseService(
            permit_license_repository,
            applicant_repository,
            officer_repository,
        )

        self.menu = Menu()

        self.handlers = Handlers(
            applicant_service,
            permit_license_service,
            officer_service,
        )

    def run(self):
        """Start and run the command-line application."""
        print()
        print("=" * 60)
        print("       DIGITAL PERMIT & LICENSE MANAGEMENT SYSTEM")
        print("=" * 60)
        print("Welcome to the system.")

        while True:
            self.menu.display()

            choice = input("Select an option: ").strip()

            if choice == "1":
                self.handlers.register_applicant()

            elif choice == "2":
                self.handlers.register_officer()

            elif choice == "3":
                self.handlers.submit_application()

            elif choice == "4":
                self.handlers.view_permit_license()

            elif choice == "5":
                self.handlers.view_all_permits_licenses()

            elif choice == "6":
                self.handlers.assign_application()

            elif choice == "7":
                self.handlers.approve_application()

            elif choice == "8":
                self.handlers.expire_permit_license()

            elif choice == "9":
                self.handlers.view_applicants()

            elif choice == "10":
                self.handlers.view_officers()

            elif choice == "0":
                print("\nThank you for using the system.")
                break

            else:
                print("Error: Invalid menu option.")