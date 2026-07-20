from fastapi import FastAPI


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
task1 = {"id": 1, "title": "Task 1", "done": False}
task2 = {"id": 2, "title": "Task 2", "done": True}
task3 = {"id": 3, "title": "Task 3", "done": False}

tasks = [
    task1,
    task2,
    task3
]

app = FastAPI()

@app.get("/")
def root():
    return{
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