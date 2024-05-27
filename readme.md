# School Software

## What can you do

### CRUD Operations:

- Upload a student (name, last name, course, age, dni, phones, emails, allergies)
- Remove a student
- Show all students
- Fetch some or one student
- Modify student data
- Automatically create backups

## Usage

1. Ensure that the following directories exist in the root folder:

   - `backup`: Used for storing backup files.
   - `data`: Contains the data files where student information is stored.

2. Execute the software and perform CRUD operations using the interface.

## Directory Structure

root/
│
├── backup/ # Directory for storing backup files
│
├── data/ # Directory containing data files
│
├── main.exe # Executable file
│
├── README.md # This file
│
├── ...

## Create Executable (.exe)

To create an executable (.exe) file, use the following command:

**Windows:**
`python setup.py build`

**Linux:**
`wine python setup.py build`

Ensure you have Python and necessary dependencies installed before running these commands.

**Table of Contents**

[TOC]
