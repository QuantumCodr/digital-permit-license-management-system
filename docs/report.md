# DIGITAL PERMIT & LICENSE MANAGEMENT SYSTEM

**Author:** QuantumCodr  
**Module:** PROG211 – Object-Oriented Programming 1  
**Language:** Python  
**Date:** 2026-10-02  

---

## 1. Introduction

The Digital Permit & License Management System is a Python command-line application developed to demonstrate Object-Oriented Programming concepts through a government-related real-world problem.

The system manages applicants, licensing officers, and government permit or license applications.

The selected problem is **Digital Permit & License Management System**, which is one of the approved Government problems in the assignment brief.

---

## 2. Problem Statement

Government permit and license processes may involve manual records, making applications difficult to organize and track.

The proposed system provides a simple digital approach for registering applicants, submitting applications, assigning applications to licensing officers, approving applications, and tracking permit or license status.

---

## 3. Objectives

The system is designed to:

- Register applicants.
- Register licensing officers.
- Submit permit and license applications.
- Assign applications to licensing officers.
- Approve applications.
- Track application status.
- Mark approved permits or licenses as expired.
- Demonstrate Object-Oriented Programming concepts.
- Store multiple records using a dictionary.
- Persist records using JSON files.

---

## 4. System Design

The system contains three main classes.

### Applicant

The `Applicant` class represents a person applying for a government permit or license.

It contains applicant information such as:

- Applicant ID
- Name
- Address

### PermitLicense

The `PermitLicense` class represents a permit or license application.

It contains:

- Permit/license ID
- Applicant ID
- Permit/license type
- Purpose
- Status
- Assigned officer

### LicensingOfficer

The `LicensingOfficer` class represents a government officer responsible for processing applications.

It contains:

- Officer ID
- Name
- Department

The relationship between the objects is:

```text
Applicant
    ↓
applies for
    ↓
PermitLicense
    ↓
processed by
    ↓
LicensingOfficer
5. Application Lifecycle

The system uses the following application lifecycle:

Pending → Approved → Expired

A permit or license application must first be assigned to a licensing officer before it can be approved.

The system also prevents invalid operations, such as approving an expired application or assigning an already approved application.

6. Object-Oriented Programming Concepts
Classes and Objects

The application defines three main classes:

Applicant
PermitLicense
LicensingOfficer

Objects are created from these classes when applicants and officers are registered and when permit or license applications are submitted.

Encapsulation

Unique identifiers are encapsulated using private attributes and properties.

Example:

self.__applicant_id = applicant_id

The ID can then be accessed through:

applicant.applicant_id
Instance Methods

Instance methods operate on individual objects.

Examples include:

display_info()
assign_officer()
approve()
expire()
Class Method

The PermitLicense class contains the class method:

create_basic()

It provides a class-level way of creating a new permit or license object.

Static Method

The system contains the static method:

is_valid_type()

It checks whether a selected permit or license type is supported.

7. Python Data Structure

The project uses a dictionary as its selected data structure for storing multiple records.

Records are identified using unique IDs.

Example:

{
    "1": {
        "applicant_id": 1,
        "name": "Mohamed Kamara",
        "address": "Lumley"
    }
}

The dictionary structure allows records to be accessed using their unique identifiers.

8. Data Persistence

The application stores information in JSON files:

data/
├── applicants.json
├── permits_licenses.json
└── officers.json

Repositories are responsible for reading and writing the JSON data.

Unique IDs are generated automatically based on the existing records.

This allows information to remain available when the application is restarted.

9. System Architecture

The project separates responsibilities into different layers:

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

Handle application operations and business rules.

Repositories

Handle JSON persistence and retrieval.

CLI

Handles user input and displays results.

Main

Starts the application.

This separation keeps the different responsibilities of the application organized.

10. Main Features

The command-line application provides the following operations:

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

The application also provides basic validation for user input.

Examples include:

Empty required fields
Invalid IDs
Non-numeric IDs
Zero or negative IDs
Invalid permit/license types
Missing application purpose
Non-existent applicants
Non-existent officers
Invalid application status operations

Invalid input is displayed as an error instead of terminating the application.

11. Example Execution
Applicant Registration
--- Register Applicant ---

Enter applicant name: Mohamed Kamara
Enter address: Lumley

Applicant registered successfully.
Applicant ID: APP-0001
Permit/License Application
--- Submit Permit/License Application ---

Enter applicant ID: 1

Permit/License Types:
1. Driving License
2. Business Permit
3. Building Permit
4. Trading License
5. Other

Select type: 1
Enter purpose: New driving license

Application submitted successfully.
Permit/License ID: LIC-0001
Status: Pending
Approval

After assigning the application to a licensing officer:

Application assigned successfully.
Permit/License ID: LIC-0001
Officer ID: OFF-0001

The application can then be approved:

Application approved successfully.
Permit/License ID: LIC-0001
Status: Approved
12. Digital Public Goods Alignment

The assignment requires the project to consider Digital Public Goods principles.

Open Source

The project's source code is maintained in a GitHub repository.

Inclusive and Accessible Design

The system uses a simple command-line interface with numbered options and clear messages.

Privacy Respecting

The demonstration data uses sample information and does not require sensitive personal information.

Modular and Reusable

The application separates models, services, repositories, and CLI components. Each component has a defined responsibility.

13. Project Structure
digital-permit-license-management-system/
├── README.md
├── main.py
├── app/
│   ├── models/
│   ├── repositories/
│   ├── services/
│   └── cli/
├── data/
└── docs/
    └── report.md
14. Screenshots
Screenshot 1 – Main Menu

Insert screenshot of the application main menu.

Screenshot 2 – Applicant Registration

Insert screenshot showing successful applicant registration.

Screenshot 3 – Application Submission

Insert screenshot showing a permit/license application being submitted.

Screenshot 4 – Application Processing

Insert screenshot showing application assignment and approval.

Screenshot 5 – Application Status

Insert screenshot showing the permit/license status.

15. GitHub Repository

The complete project source code and documentation are maintained in the GitHub repository:

Digital Permit & License Management System

https://github.com/QuantumCodr/digital-permit-license-management-system

16. Conclusion

The Digital Permit & License Management System demonstrates how Python Object-Oriented Programming can be applied to a government-related real-world problem.

The project demonstrates classes and objects, encapsulation, instance methods, class methods, static methods, dictionary data structures, JSON persistence, validation, and modular application design.

The system provides a simple way to manage applicants, licensing officers, and permit or license applications while addressing the Digital Public Goods principles required by the assignment.


### Report length

This version is deliberately **not a long academic paper**. With the screenshots inserted, it should remain reasonably compact for printing while still covering the assignment's major assessed areas: **classes/objects, data structure, methods, DPG standards, documentation, and GitHub**. :contentReference[oaicite:0]{index=0}

One thing I would **not** do yet is put the GitHub URL into the final report if the repository hasn't actually been created. Once you create it, we can verify the repository and then finalize that section.