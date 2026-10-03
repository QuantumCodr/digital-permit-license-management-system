# Digital Permit & License Management System

## Individual Assignment Report

**Course:** PROG211 – Object-Oriented Programming 1  
**Assignment:** Real-World Solutions under DPG Standards  
**Institution:** Limkokwing University of Creative Technology, Sierra Leone  
**Department:** ICT  
**Semester:** Semester 03, September 2026 – February 2027  
**Student:** QuantumCodr  
**Project:** Digital Permit & License Management System  
**Language:** Python

---

## 1. Introduction

The Digital Permit & License Management System is a Python-based Object-Oriented Programming project developed to address the government problem of managing permit and license applications digitally.

The system allows applicants to be registered, permit or license applications to be submitted, applications to be assigned to licensing officers, applications to be approved, and approved permits or licenses to expire when necessary.

The project demonstrates fundamental Object-Oriented Programming concepts including classes, objects, attributes, instance methods, class methods, static methods, object interaction, and data structures.

The system also follows the Digital Public Goods (DPG) principles required by the assignment by using open-source development through GitHub, modular design, accessibility through a simple command-line interface, and privacy-conscious sample data.

---

## 2. Problem Statement

Government permit and license processes can involve several stages, including registering applicants, submitting applications, assigning applications to responsible officers, reviewing applications, and tracking their status.

Without a structured digital system, managing these activities can become difficult and information can be harder to organize.

This project provides a simple digital solution for managing applicants, permit and license applications, and licensing officers in one system.

---

## 3. Objectives

The main objectives of the system are:

1. To register applicants.
2. To register licensing officers.
3. To submit permit and license applications.
4. To assign applications to licensing officers.
5. To approve permit and license applications.
6. To track the status of applications.
7. To allow approved permits or licenses to expire.
8. To demonstrate Object-Oriented Programming concepts.
9. To use a dictionary as the main data structure for storing multiple objects.
10. To provide a modular and reusable system aligned with DPG principles.

---

## 4. System Design

The system contains three main classes:

- `Applicant`
- `PermitLicense`
- `LicensingOfficer`

The relationship between the classes is:

```text
Applicant
   ↓ applies for
PermitLicense
   ↓ processed by
LicensingOfficer
4.1 Applicant

The Applicant class represents a person applying for a government permit or license.

Its main attributes are:

Applicant ID
Name
Address

The class also contains a method for displaying applicant information.

4.2 PermitLicense

The PermitLicense class represents a permit or license application.

Its main attributes are:

Permit/License ID
Applicant ID
Permit Type
Purpose
Status
Officer ID

The supported permit and license types are:

Driving License
Business Permit
Building Permit
Trading License
Other
4.3 LicensingOfficer

The LicensingOfficer class represents an officer responsible for processing applications.

Its main attributes are:

Officer ID
Name
Department
5. Application Lifecycle

The system uses a simple application lifecycle:

Pending → Approved → Expired
Pending

A newly submitted application starts with the Pending status.

Approved

An application can be approved after it has been assigned to a licensing officer.

Expired

An approved permit or license can later be marked as Expired.

This provides a simple way to track the state of each application.

6. Object-Oriented Programming Concepts

The project demonstrates several OOP concepts covered in the course.

6.1 Classes

The system uses classes to represent real-world entities.

Examples:

class Applicant:
    ...
class PermitLicense:
    ...
class LicensingOfficer:
    ...
6.2 Objects

Objects are created from the classes to represent individual applicants, applications, and officers.

For example:

applicant = Applicant(
    1,
    "Mohamed Kamara",
    "Lumley"
)

The object represents a specific applicant in the system.

6.3 Attributes

Each object stores information using attributes.

For example:

self.name = name
self.address = address
6.4 Instance Methods

Instance methods operate on individual objects.

For example, the PermitLicense class contains methods such as:

def assign_officer(self, officer_id):
    self.officer_id = officer_id
def approve(self):
    self.status = self.APPROVED
def expire(self):
    self.status = self.EXPIRED
6.5 Class Method

The PermitLicense class contains a class method for creating a basic permit or license object:

@classmethod
def create_basic(
    cls,
    permit_license_id,
    applicant_id,
    permit_type,
    purpose
):
    return cls(
        permit_license_id,
        applicant_id,
        permit_type,
        purpose
    )

This demonstrates the use of a class method with cls.

6.6 Static Method

The PermitLicense class also contains a static method used to validate permit types:

@staticmethod
def is_valid_type(permit_type):
    return permit_type in PermitLicense.VALID_TYPES

The method does not depend on a particular object instance.

7. Data Structure

The project uses one main data structure: a dictionary.

This follows the assignment requirement to use either a list or dictionary for storing multiple objects.

Each record uses a unique ID as the dictionary key.

For example:

{
    "1": applicant_object,
    "2": applicant_object,
    "3": applicant_object
}

The same approach is used when storing permit/license and officer records.

The dictionary structure allows records to be accessed using their unique IDs.

8. JSON Persistence

The system stores its data in JSON files so that information can remain available after the program is closed.

The project contains:

data/
├── applicants.json
├── permits_licenses.json
└── officers.json

The repositories are responsible for reading and writing these JSON files.

For example:

ApplicantRepository
        ↓
applicants.json
PermitLicenseRepository
        ↓
permits_licenses.json
OfficerRepository
        ↓
officers.json

This keeps file handling separate from the models and services.

9. Application Architecture

The project follows a modular architecture:

main.py
   ↓
CLI
   ↓
Services
   ↓
Repositories
   ↓
JSON Data
Main

main.py acts as the entry point of the program.

It starts the application but does not contain the application's business logic.

CLI

The command-line interface handles interaction with the user.

It contains:

application.py
menu.py
handlers.py
Services

The service layer contains the application's business logic.

The services are:

ApplicantService
PermitLicenseService
OfficerService
Repositories

Repositories are responsible for persistence and retrieving objects from JSON files.

The repositories are:

ApplicantRepository
PermitLicenseRepository
OfficerRepository
Models

The model layer represents the main objects in the system:

Applicant
PermitLicense
LicensingOfficer
10. Features and Validation

The system provides the following features:

Register Applicant
Register Licensing Officer
Submit Permit/License Application
View Permit/License
View All Permits/Licenses
Assign Application
Approve Application
Expire Permit/License
View Applicants
View Licensing Officers

The system also performs basic validation.

Examples include:

Applicant IDs must exist.
Officer IDs must exist.
IDs must be numeric.
IDs must be greater than zero.
Permit types must be valid.
An application must have an assigned officer before approval.
An expired application cannot be assigned.
An approved application cannot be assigned again.
An application can only be expired after it has been approved.
11. Example Execution

When the program starts, the main menu is displayed:

============================================================
       DIGITAL PERMIT & LICENSE MANAGEMENT SYSTEM
============================================================
1. Register Applicant
2. Register Licensing Officer
3. Submit Permit/License Application
4. View Permit/License
5. View All Permits/Licenses
6. Assign Application
7. Approve Application
8. Expire Permit/License
9. View Applicants
10. View Licensing Officers
0. Exit
============================================================

A typical workflow is:

Register Applicant
        ↓
Submit Application
        ↓
Assign Application
        ↓
Approve Application
        ↓
Expire Permit/License

For example, an applicant may submit a Driving License application.

The application initially has:

Status: Pending
Officer ID: Not assigned

After assigning a licensing officer:

Status: Pending
Officer ID: 1

After approval:

Status: Approved
Officer ID: 1

When the permit or license expires:

Status: Expired
Officer ID: 1
12. Digital Public Goods (DPG) Alignment

The project follows the DPG requirements stated in the assignment.

12.1 Open Source

The project source code is maintained in a public GitHub repository.

GitHub Repository:

https://github.com/QuantumCodr/digital-permit-license-management-system

This allows the source code to be reviewed and reused.

12.2 Inclusive and Accessible

The system uses a simple command-line interface.

Users interact with clear numbered menu options and text prompts.

This keeps the application lightweight and does not require specialized hardware or complicated software.

12.3 Privacy-Respecting

The system does not require sensitive personal information.

The sample data uses basic information such as:

Name
Address
Applicant ID

The project uses demonstration data for academic purposes.

12.4 Modular and Reusable

The system is separated into models, repositories, services, and CLI components.

This allows different parts of the system to be maintained independently.

For example:

Models
   ↓
Services
   ↓
Repositories
   ↓
Data

The separation also makes the application easier to extend in the future.

13. Project Structure

The final project structure is:

digital-permit-license-management-system/
│
├── README.md
├── main.py
│
├── app/
│   ├── __init__.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── applicant.py
│   │   ├── permit_license.py
│   │   └── licensing_officer.py
│   │
│   ├── repositories/
│   │   ├── __init__.py
│   │   ├── applicant_repository.py
│   │   ├── permit_license_repository.py
│   │   └── officer_repository.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── applicant_service.py
│   │   ├── permit_license_service.py
│   │   └── officer_service.py
│   │
│   └── cli/
│       ├── __init__.py
│       ├── application.py
│       ├── menu.py
│       └── handlers.py
│
├── data/
│   ├── applicants.json
│   ├── permits_licenses.json
│   └── officers.json
│
└── docs/
    └── report.md
14. Screenshots

The following screenshots should be included in the hardcopy report to demonstrate the program running.

Screenshot 1 – Main Menu

Show the main application menu after starting the program.

[Insert Screenshot Here]

Screenshot 2 – Applicant and Officer Registration

Show the registration of an applicant and/or licensing officer.

[Insert Screenshot Here]

Screenshot 3 – Permit/License Submission and Assignment

Show an application being submitted and assigned to a licensing officer.

[Insert Screenshot Here]

Screenshot 4 – Approval and Status Tracking

Show an application being approved and its status being displayed.

[Insert Screenshot Here]

15. GitHub Submission

The complete project has been uploaded to GitHub.

Repository:

https://github.com/QuantumCodr/digital-permit-license-management-system

The repository contains:

Python source code
Project documentation
README
JSON demonstration data
Project structure
DPG alignment information
16. Conclusion

The Digital Permit & License Management System provides a simple object-oriented solution to the government problem of managing permit and license applications.

The project demonstrates the use of classes, objects, attributes, instance methods, class methods, static methods, object interaction, dictionaries, JSON persistence, and modular application architecture.

The system also addresses the Digital Public Goods requirements by being open-source, modular, accessible through a simple command-line interface, and designed with privacy considerations.

The project demonstrates how Object-Oriented Programming concepts can be applied to a real-world government problem using Python.

17. Assignment Checklist
Requirement	Completed
Real-world government problem selected	Yes
At least two relevant classes	Yes
Attributes implemented	Yes
Objects created	Yes
Objects interact	Yes
Instance methods implemented	Yes
Class method implemented	Yes
Static method implemented	Yes
One main data structure used	Yes – Dictionary
Data persistence implemented	Yes – JSON
DPG alignment documented	Yes
GitHub repository created	Yes
README included	Yes
Example usage included	Yes
Screenshots prepared	To be inserted
Hardcopy report prepared	Yes

Author: QuantumCodr
Project: Digital Permit & License Management System
Course: PROG211 – Object-Oriented Programming 1