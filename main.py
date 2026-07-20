from fastapi import FastAPI, HTTPException, Response


# Stage-0
#app = FastAPI()

# @app.get("/")

# def read_root():
#     return {
#         "message" : "Hello, World!"
#         }

# read_root()

#stage-1
#app = FastAPI()
# @app.get("/")
# def root():
#     return{
#         "name": "Task API",
#         "version": "1.0", 
#         "endpoints": ["/tasks"] 
#     }


# @app.get("/health")
# def health():
#     return{
#         "status": "OK"
#     }


#stage-2
# task1 = {"id": 1, "title": "Task 1", "done": False}
# task2 = {"id": 2, "title": "Task 2", "done": True}
# task3 = {"id": 3, "title": "Task 3", "done": False}

# tasks = [
#     task1,
#     task2,
#     task3
# ]

# app = FastAPI()

# @app.get("/")
# def root():
#     return{
#         "name": "Task API",
#         "version": "1.0",  
#         "endpoints": ["/tasks"] 
#     }

# @app.get("/tasks")
# def get_tasks():
#     return tasks

# @app.get("/tasks/{id}")
# def get_task(id: int):  
#     for task in tasks:
#         if task["id"] == id:
#             return task
#     return {"error": f"Task {id} not found"}


# Stage-3
# push task data to a database and fetch it from there. For now, we will use a list to store the tasks.


from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str

class TaskUpdate(BaseModel):
    title: str
    done: bool

app = FastAPI()
tasks = [
    task1 := {"id": 1, "title": "Task 1", "done": False},
    task2 := {"id": 2, "title": "Task 2", "done": False},
    task3 := {"id": 3, "title": "Task 3", "done": False},
]

@app.get("/")
def root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }

@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    if task.title.strip() == "":
        raise HTTPException(status_code=400, detail="Task title cannot be empty")

    if tasks:
        next_id = max(t['id'] for t in tasks) + 1
    else:
        next_id = 1

    new_task = {"id": next_id, "title": task.title, "done": False}
    tasks.append(new_task)

    return new_task


@app.put("/tasks/{id}")
def update_task(id: int, updated_task: TaskUpdate):
    if updated_task.title.strip() == "":
        raise HTTPException(status_code=400, detail="Task title cannot be empty")

    for t in tasks:
        if t["id"] == id:
            t["title"] = updated_task.title
            t["done"] = updated_task.done
            return t
        
    raise HTTPException(status_code=404, detail=f"Task {id} not found")

@app.delete("/tasks/{id}", status_code=204)
def delete_task(id: int):
    for t in tasks:
        if t["id"] == id:
            tasks.remove(t)
            return Response(status_code=204)
    raise HTTPException(status_code=404, detail=f"Task {id} not found")

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{id}")
def get_task(id: int):  
    for task in tasks:
        if task["id"] == id:
            return task
    return {"error": f"Task {id} not found"}