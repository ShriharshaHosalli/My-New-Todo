# models.py

import sqlite3

def get_db():
    return sqlite3.connect("database.db")

def get_all_tasks():
    conn = get_db()
    tasks = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()
    return tasks

def add_task(title):
    conn = get_db()
    conn.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = get_db()
    conn.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()

def update_task(task_id, completed):
    conn = get_db()
    conn.execute(
        "UPDATE tasks SET completed=? WHERE id=?",
        (completed, task_id)
    )
    conn.commit()
    conn.close()

def init_db():
    conn = get_db()
    conn.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        completed INTEGER DEFAULT 0
    )
    """)
    conn.close()