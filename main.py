"""
------------------------------------------------------------
Program Name : Digital Permit & License Management System
Author       : QuantumCodr
Date         : 2026-10-02
Language     : Python
Module       : Application Entry Point
Description  : Starts the Digital Permit & License
               Management System.
------------------------------------------------------------
"""

from app.cli.application import Application


def main():
    """Start the application."""
    application = Application()
    application.run()


if __name__ == "__main__":
    main()