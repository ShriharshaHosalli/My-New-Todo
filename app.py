from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("database.db")

# Create table
def init_db():
    conn = get_db()
    conn.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, title TEXT)")
    conn.close()

init_db()

@app.route("/")
def home():
    return render_template("index.html")

# GET tasks
@app.route("/tasks", methods=["GET"])
def get_tasks():
    conn = get_db()
    tasks = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()
    return jsonify(tasks)

# ADD task
@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.json
    conn = get_db()
    conn.execute("INSERT INTO tasks (title) VALUES (?)", (data["title"],))
    conn.commit()
    conn.close()
    return {"message": "Task added"}

# DELETE task
@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    conn = get_db()
    conn.execute("DELETE FROM tasks WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return {"message": "Task deleted"}

if __name__ == "__main__":
    app.run(debug=True)