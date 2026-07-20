from fastapi import FastAPI

app = FastAPI()

# Stage-0
# @app.get("/")

# def read_root():
#     return {
#         "message" : "Hello, World!"
#         }

# read_root()

#stage-1
@app.get("/")
def root():
    return{
        "name": "Task API",
        "version": "1.0", 
        "endpoints": ["/tasks"] 
    }


@app.get("/health")
def health():
    return{
        "status": "OK"
    }
