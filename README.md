# Database Interaction with PostgreSQL and Application Programming

## Overview  
This project demonstrates a PostgreSQL database connected to a Python application that performs basic CRUD (Create, Read, Update, Delete) operations on a table named **students**.

---

## Database Schema  
**Table:** `students`  

| Field | Type | Constraints |
|--------|------|-------------|
| student_id | Integer | Primary Key, Auto Increment |
| first_name | Text | Not Null |
| last_name | Text | Not Null |
| email | Text | Not Null, Unique |
| enrollment_date | Date |  |

---

## Setup Instructions  

### 1. Database Setup  
1. Ensure PostgreSQL is installed and running.  
2. Run the following SQL commands in **pgAdmin** or **psql**:

```sql
CREATE TABLE IF NOT EXISTS students (
    student_id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    enrollment_date DATE
);

INSERT INTO students (first_name, last_name, email, enrollment_date)
VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');
```

---

### 2. Python Application Setup  
1. Ensure Python is installed and running.  
2. Run the following command to install dependencies:

```bash
pip install psycopg2
```

3. Open **DBApp.py** and update the database connection details if necessary:

```python
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="your_password",  # Replace with your local PostgreSQL password
    port="5432"
)
```

4. Ensure the PostgreSQL server is active.  
5. Run the Python script:

```bash
python DBApp.py
```

---

## Running the Application  

The program demonstrates:  
- Retrieving all students  
- Adding a new student  
- Updating a student’s email  
- Deleting a student  
- Displaying updated records  

---

## Demonstration Video  
A short video demonstrating all CRUD operations can be found here:  
https://youtu.be/sXYDYnFkYgU

---

## Notes for the Grader  
- Replace `"password"` in the script with your local PostgreSQL password before testing.  
- All four CRUD operations are implemented and verified.  
- The code runs with standard PostgreSQL setup on port `5432`.
