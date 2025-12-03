from fastapi import FastAPI

app = FastAPI()

trainings = [
    {"title": "Safety Procedures", "completed": True},
    {"title": "Equipment Handling", "completed": True},
    {"title": "Emergency Response", "completed": False},
    {"title": "Advanced Tools", "completed": False},
    {"title": "Leadership Skills", "completed": False},
]

@app.get("/trainings")
def get_trainings():
    return trainings
