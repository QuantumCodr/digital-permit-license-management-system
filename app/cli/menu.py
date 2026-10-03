"""
------------------------------------------------------------
Program Name : Digital Permit & License Management System
Author       : QuantumCodr
Date         : 2026-10-02
Language     : Python
Module       : CLI Menu
Description  : Displays the main command-line menu.
------------------------------------------------------------
"""


class Menu:
    """Displays the application's command-line menu."""

    def display(self):
        """Display the main application menu."""
        print()
        print("=" * 60)
        print("       DIGITAL PERMIT & LICENSE MANAGEMENT SYSTEM")
        print("=" * 60)
        print("1. Register Applicant")
        print("2. Register Licensing Officer")
        print("3. Submit Permit/License Application")
        print("4. View Permit/License")
        print("5. View All Permits/Licenses")
        print("6. Assign Application")
        print("7. Approve Application")
        print("8. Expire Permit/License")
        print("9. View Applicants")
        print("10. View Licensing Officers")
        print("0. Exit")
        print("=" * 60)