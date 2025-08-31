# 📝 Student Course Management System

This project is a **Python-based command-line tool** that helps manage students and courses efficiently. It follows **Object-Oriented Programming (OOP)** principles and is structured in a modular way for clarity and scalability.  

---

## 📂 Project Files

- **`main.py`** → Program entry point (runs the application).  
- **`model/student.py`** → Defines the `Student` class.  
- **`model/course.py`** → Defines the `Course` class.  
- **`core/system_manager.py`** → Core logic for handling students and courses.  
- **`requirements.txt`** → List of dependencies (currently empty).  

---

## ▶️ Running the Application

1. Ensure **Python 3.10+** is installed on your system.  
2. Run the program using:  

```bash
python main.py
```

3. From the command-line interface, you can:  
   - Add students or courses  
   - Display all students or courses  
   - Enroll students in a course  
   - Exit the system  

---

## ✨ Key Features

- OOP design with separate **Student** and **Course** classes.  
- Clear separation of concerns (models vs. core logic).  
- Easily extendable (e.g., adding persistence with files or databases, or even a GUI).  

---

## 📁 Directory Overview

```
student_course_system/
│
├── main.py
├── requirements.txt
│
├── model/
│   ├── student.py
│   └── course.py
│
└── core/
    └── system_manager.py
```

---

## ℹ️ Additional Notes

- Currently, no external libraries are required.  
- Data is stored **in memory only** (not saved to files or databases).  
- `requirements.txt` remains empty at this stage.  

---

## 👨‍💻 Developer

Created as a practice project to strengthen Python and OOP concepts.  
