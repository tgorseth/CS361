from fastapi import FastAPI

app = FastAPI()

@app.get("/dashboard")
def get_dashboard():
    return {"progress": "75%", "message": "Keep going, you’re almost there!"}
