from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
users = []

class LoginRequest(BaseModel):
    username: str
    password: str

class UserCreateRequest(BaseModel):
    username: str
    password: str
    role: str

@app.post("/auth")
def authenticate(request: LoginRequest):
    for user in users:
        if user["username"] == request.username and user["password"] == request.password:
            return {"token": f"fake-jwt-token-for-{request.username}"}
    raise HTTPException(status_code=401, detail="Invalid credentials")


@app.post("/create-user")
def create_user(user: UserCreateRequest):
    users.append(user.dict())
    return {"message": f"User {user.username} created successfully as {user.role}"}
