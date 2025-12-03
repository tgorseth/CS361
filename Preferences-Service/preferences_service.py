from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Stored
preferences = {
    "admin": {"username": "admin", "role": "Trainer"},
    "test": {"username": "test", "role": "User"},
}

class Preference(BaseModel):
    username: str
    role: str

@app.get("/preferences/{username}")
def get_preferences(username: str):
    return preferences.get(username, {"username": username, "role": "User"})

@app.post("/preferences/{username}")
def set_preferences(username: str, pref: Preference):
    preferences[username] = pref.dict()
    return {"message": f"Preferences updated for {username}"}
