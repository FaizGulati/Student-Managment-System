# School Management System

A command-line School Management System built in Python using Object-Oriented Programming principles. The system manages two types of users — **Students** and **Teachers** — using an abstract base class to enforce a consistent structure across both. All data is stored persistently in a JSON file (`School_data.json`).

## Features
- Register new students and teachers with email validation
- Prevents duplicate registration (checked via roll number / employee ID)
- View individual student details, including subject-wise grades and calculated average
- View individual teacher details
- Add and update subject-wise grades for students
- Persistent storage using JSON — data is saved automatically after every update

## Tech Stack
- **Language:** Python
- **Data Storage:** JSON
- **Concepts Used:** Object-Oriented Programming, Abstract Base Classes (ABC), Inheritance, Static Methods

## Project Structure
- `Persons` (Abstract Class): Defines a common blueprint (`get_role`, `register`, `show`) that both Student and Teacher must implement, plus a shared static method for email validation.
- `Student`: Handles student registration, viewing details, and grade management.
- `Teacher`: Handles teacher registration and viewing details.

## How It Works
1. Run the program — a menu is displayed with 5 options.
2. Choose to register a student/teacher, add grades, or view details.
3. Data is validated (e.g., email format, duplicate roll number/emp ID) before being saved.
4. All records are stored in and loaded from `School_data.json`, so data persists across runs.

## How to Run
```bash
python main.py
```

## Menu Options
1 - Register Student
2 - Register Teacher
3 - Add Grades
4 - Show Student Detail
5 - Show Teacher Detail


## Future Improvements
- Add a proper looping menu instead of single-run execution
- Add update/delete functionality for existing records
- Improve error handling (e.g., invalid input types)
- Add search by name in addition to roll number/emp ID
- Move from JSON to a database (SQLite) for better scalability
- Build a GUI or web interface (Tkinter/Flask)

## Learning Outcome
This project helped me understand and apply Object-Oriented Programming concepts like abstraction and inheritance in Python, along with file handling, JSON data persistence, and building menu-driven CLI applications.

