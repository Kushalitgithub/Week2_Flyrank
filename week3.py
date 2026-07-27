import sqlite3
from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str

class TaskUpdate(BaseModel):
    title: str
    done: bool

app = FastAPI()
tasks = [
    task1 := {"id": 1, "title": "Task 1", "done": False},
    task2 := {"id": 2, "title": "Task 2", "done": True},
    task3 := {"id": 3, "title": "Task 3", "done": False},
]

DB_NAME = 'tasks.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY ,
            title TEXT NOT NULL,
            done BOOLEAN NOT NULL DEFAULT 0
        )
        
        '''
    )


    cursor.execute("SELECT COUNT(*) FROM tasks")
    count = cursor.fetchone()[0]

    # if there are no tasks in the database, insert some sample tasks
    if count == 0:
        for task in tasks:
            cursor.execute(
                "INSERT INTO tasks (id, title, done) VALUES (?, ?, ?)",
                (task["id"], task["title"], task["done"])
            )

        
    conn.commit()
    conn.close()

def show_tasks():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    for task in tasks:
        print(f"{task[0]}. {task[1]} - {'Done' if task[2] else 'Not Done'}")

    conn.close()



@app.get("/")
def root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{id}")
def get_task(id: int):  
    for task in tasks:
        if task["id"] == id:
            return task
    return {"error": f"Task {id} not found"}




def main():
    init_db()
    show_tasks()

if __name__ == "__main__":
    main()

