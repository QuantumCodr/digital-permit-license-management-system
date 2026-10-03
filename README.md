# Digital Permit & License Management System

A Python-based command-line application for managing government permit and license applications.

## Project Overview

The Digital Permit & License Management System provides a simple way to register applicants, register licensing officers, submit permit or license applications, assign applications to officers, approve applications, and track application status.

This project was developed for the **PROG211 – Object-Oriented Programming 1** individual assignment.

## Problem Being Solved

Government permit and license processes can involve manual records, making applications difficult to organize and track.

This system provides a simple digital approach for managing applicants, permit and license applications, and licensing officers.

## Objectives

- Register applicants.
- Register licensing officers.
- Submit permit and license applications.
- Assign applications to licensing officers.
- Approve applications.
- Track application status.
- Mark approved permits or licenses as expired.
- Store records using JSON files.
- Demonstrate Python object-oriented programming concepts.

## Supported Permit and License Types

The system supports:

- Driving License
- Business Permit
- Building Permit
- Trading License
- Other

## Application Lifecycle

Applications follow this lifecycle:

```text
Pending → Approved → Expired

An application must be assigned to a licensing officer before it can be approved.

Object-Oriented Design

The system contains three main classes.

Applicant

Represents a person applying for a government permit or license.

PermitLicense

Represents a government permit or license application, including its type, purpose, status, applicant, and assigned officer.

LicensingOfficer

Represents a government officer responsible for processing permit and license applications.

The project demonstrates:

Classes and objects
Attributes
Encapsulation
Instance methods
Class methods
Static methods
Object interaction
Data Structure

The project uses a dictionary as its main data structure for storing multiple records.

Records are stored using unique automatically generated IDs.

Example:

{
    "1": {
        "applicant_id": 1,
        "name": "Mohamed Kamara",
        "address": "Lumley"
    }
}
Project Architecture
main.py
   ↓
CLI
   ↓
Services
   ↓
Repositories
   ↓
JSON Data
Models

Represent the main objects in the system.

Services

Contain application logic and business rules.

Repositories

Handle reading and writing JSON data.

CLI

Handles user input and displays application results.

Main

Starts the application.

Project Structure
digital-permit-license-management-system/
├── README.md
├── main.py
├── app/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── applicant.py
│   │   ├── permit_license.py
│   │   └── licensing_officer.py
│   ├── repositories/
│   │   ├── __init__.py
│   │   ├── applicant_repository.py
│   │   ├── permit_license_repository.py
│   │   └── officer_repository.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── applicant_service.py
│   │   ├── permit_license_service.py
│   │   └── officer_service.py
│   └── cli/
│       ├── __init__.py
│       ├── application.py
│       ├── menu.py
│       └── handlers.py
├── data/
│   ├── applicants.json
│   ├── permits_licenses.json
│   └── officers.json
└── docs/
    └── report.md
Validation

The system performs basic input validation, including:

Required applicant name
Required address
Required officer name
Required department
Numeric IDs
Positive IDs
Valid permit/license type
Required application purpose
Existing applicant verification
Existing officer verification
Valid application status transitions

Invalid input is reported to the user without terminating the application.

Data Persistence

The system uses JSON files to store application data:

data/applicants.json
data/officers.json
data/permits_licenses.json

The records remain available when the application is restarted.

Unique IDs are generated automatically from the existing records.

Digital Public Goods Alignment

The project considers the following Digital Public Goods principles required by the assignment.

Open Source

The project source code is maintained in a GitHub repository.

Inclusive and Accessible Design

The system uses a simple command-line interface with clear numbered options and readable messages.

Privacy Respecting

The demonstration data uses sample information and does not require sensitive personal information.

Modular and Reusable

The application is divided into models, repositories, services, and CLI components. Each component has a clear responsibility.

Example Usage

A typical application workflow is:

1. Register Applicant
2. Register Licensing Officer
3. Submit Permit/License Application
4. Assign Application
5. Approve Application
6. View Permit/License
7. Expire Permit/License

Example application:

Permit/License ID: LIC-0001
Applicant ID: APP-0001
Type: Driving License
Purpose: New driving license
Status: Pending
Officer ID: Not assigned

After assignment and approval:

Permit/License ID: LIC-0001
Status: Approved
Officer ID: OFF-0001
How to Run

Make sure Python is installed.

From the project directory, run:

python main.py

The application will display the main menu.

Author

QuantumCodr

PROG211 – Object-Oriented Programming 1


### One deliberate change from the earlier README

I removed claims that aren't necessary for the assignment, such as calling it a "complete" or "production" system. This keeps the README **factual and appropriate for a semester OOP project**.

Also, the architecture section clearly shows the separation we've built:

**CLI → Services → Repositories → JSON**

rather than making the README sound like the CLI itself is part of the business/domain layer.