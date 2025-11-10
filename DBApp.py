import psycopg2

# Database Connection Setup
# connection = psycopg2.connect(
#     "postgresql://neondb_owner:npg_24WjaToldhsY@ep-spring-hall-a4eeeuku-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
# )

# cursor = connection.cursor()

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="password",  # For the TA to test, replace with your local password
    port="5432"
)


cursor = conn.cursor()


# Create table (run this once to set up the database
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student_id SERIAL PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        enrollment_date DATE
    );
""")

#Insert initial sample data (safe to re-run, skips duplicates)
cursor.execute("""
    INSERT INTO students (first_name, last_name, email, enrollment_date)
    VALUES
        ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
        ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
        ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02')
    ON CONFLICT (email) DO NOTHING;
""")
connection.commit()


#        CRUD Operations

def get_all_students():
    """Fetch and print all students from the database."""
    cursor.execute("SELECT * FROM students;")
    students = cursor.fetchall()
    print("\nCurrent Students:")
    for s in students:
        print(s)


def add_student(first_name, last_name, email, enrollment_date):
    """Add a new student record."""
    cursor.execute(
        "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);",
        (first_name, last_name, email, enrollment_date)
    )
    connection.commit()
    print(f"Added student: {first_name} {last_name}")


def update_student_email(student_id, new_email):
    """Update the email for a given student ID."""
    cursor.execute(
        "UPDATE students SET email = %s WHERE student_id = %s;",
        (new_email, student_id)
    )
    connection.commit()
    print(f" Updated student #{student_id}'s email to {new_email}")


def delete_student(student_id):
    """Delete a student record by ID."""
    cursor.execute("DELETE FROM students WHERE student_id = %s;", (student_id,))
    connection.commit()
    print(f"Deleted student with ID {student_id}")


# Testing the CRUD operations
if __name__ == "__main__":
    get_all_students()
    add_student("John", "Walker", "john.walker@example.com", "2023-09-10")
    update_student_email(1, "john.newemail@example.com")
    delete_student(3)
    get_all_students()

# Clean up
cursor.close()
connection.close()
