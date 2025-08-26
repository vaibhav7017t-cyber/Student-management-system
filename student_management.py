import sqlite3

# Connect (creates students.db if not exists)
conn = sqlite3.connect("students.db")
cur = conn.cursor()

# Create table if not exists
cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT
)
""")

def add_student():
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    cur.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)", (name, age, course))
    conn.commit()
    print("✅ Student added successfully!\n")

def list_students():
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    if not rows:
        print("⚠️ No records found.")
    else:
        print("\n--- Student Records ---")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Course: {row[3]}")

def main():
    print("=== Student Management System ===")
    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            list_students()
        elif choice == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    main()
    conn.close()
