# 🏫 School Database

This project provides a **relational database schema** for managing a school system. The schema is implemented using **SQL** and covers students, groups, subjects, teachers, and marks.

---

## 📦 Database Structure

The database is named **`school_db`** and includes the following tables:

- **`Groups`** → Stores information about student groups.  
- **`Students`** → Stores student details and their group association.  
- **`Subjects`** → Stores subjects taught in the school.  
- **`Teachers`** → Stores teacher details.  
- **`Subject_teacher`** → Defines which teachers teach which subjects to which groups (many-to-many relationship).  
- **`Marks`** → Stores student grades for different subjects, along with the date.  

---

## 🗂 Table Details

### 1. `Groups`
| Column     | Type          | Description                |
|------------|--------------|----------------------------|
| group_id   | SERIAL (PK)  | Unique ID for each group.  |
| name       | VARCHAR(100) | Name of the group.         |

### 2. `Students`
| Column     | Type          | Description                          |
|------------|--------------|--------------------------------------|
| student_id | SERIAL (PK)  | Unique ID for each student.          |
| first_name | VARCHAR(100) | Student's first name.                |
| last_name  | VARCHAR(100) | Student's last name.                 |
| group_id   | INTEGER (FK) | References `Groups(group_id)`.       |

### 3. `Subjects`
| Column     | Type          | Description                |
|------------|--------------|----------------------------|
| subject_id | SERIAL (PK)  | Unique ID for each subject.|
| title      | VARCHAR(100) | Subject title.             |

### 4. `Teachers`
| Column     | Type          | Description                |
|------------|--------------|----------------------------|
| teacher_id | SERIAL (PK)  | Unique ID for each teacher.|
| first_name | VARCHAR(100) | Teacher's first name.      |
| last_name  | VARCHAR(100) | Teacher's last name.       |

### 5. `Subject_teacher`
| Column     | Type    | Description                                  |
|------------|---------|----------------------------------------------|
| subject_id | INTEGER | References `Subjects(subject_id)`.           |
| teacher_id | INTEGER | References `Teachers(teacher_id)`.           |
| group_id   | INTEGER | References `Groups(group_id)`.               |
| **PK**     | subject_id + teacher_id + group_id (composite key).    |

### 6. `Marks`
| Column     | Type         | Description                            |
|------------|-------------|----------------------------------------|
| mark_id    | SERIAL (PK) | Unique ID for each mark record.        |
| student_id | INTEGER (FK)| References `Students(student_id)`.     |
| subject_id | INTEGER (FK)| References `Subjects(subject_id)`.     |
| date       | TIMESTAMP   | Date of the exam/assessment.           |
| mark       | INTEGER     | The actual mark received.              |

---

## 🚀 Usage

1. Open your SQL environment (e.g., PostgreSQL, MySQL if adapted).  
2. Run the script:  

```sql
\i school_db.sql
```

3. The schema and tables will be created.  

---

## 🧠 Features

- Organizes **students, teachers, and groups**.  
- Maintains a record of **subjects taught by specific teachers to groups**.  
- Stores **students' marks with timestamps**.  
- Implements **relationships via foreign keys**.  

---

## 👨‍💻 Author

This schema was created as a learning task to practice **database design and normalization**.  
