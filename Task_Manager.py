import sqlite3

def create_connection():
    conn = sqlite3.connect('tasks.db')
    return conn

def create_tasks_table(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY,
                        title TEXT NOT NULL,
                        description TEXT,
                        status TEXT NOT NULL
                      )''')
    conn.commit()

def add_task(conn, title, description, status):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title, description, status) VALUES (?, ?, ?)", (title, description, status))
    conn.commit()

def update_task(conn, task_id, title, description, status):
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET title=?, description=?, status=? WHERE id=?", (title, description, status, task_id))
    conn.commit()

def delete_task(conn, task_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()

def view_tasks(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    return tasks

def main():
    conn = create_connection()
    create_tasks_table(conn)

    print("Task Manager")
    print("1. Add Task")
    print("2. Update Task")
    print("3. Delete Task")
    print("4. View Tasks")
    print("5. Exit")

    while True:
        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            status = input("Enter task status (completed/not completed): ")
            add_task(conn, title, description, status)
        elif choice == 2:
            task_id = int(input("Enter task ID: "))
            title = input("Enter updated task title: ")
            description = input("Enter updated task description: ")
            status = input("Enter updated task status (completed/not completed): ")
            update_task(conn, task_id, title, description, status)
        elif choice == 3:
            task_id = int(input("Enter task ID: "))
            delete_task(conn, task_id)
        elif choice == 4:
            tasks = view_tasks(conn)
            print("\nTasks:")
            for task in tasks:
                print(f"ID: {task[0]}, Title: {task[1]}, Description: {task[2]}, Status: {task[3]}")
        elif choice == 5:
            conn.close()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
