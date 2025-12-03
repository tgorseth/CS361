from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8081"],  # frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

AUTH_URL = "http://auth-service:3000"
TRAINING_URL = "http://training-service:3001"
DASHBOARD_URL = "http://dashboard-service:3002"
PREFERENCES_URL = "http://preferences-service:3003"

@app.post("/auth")
async def auth_proxy(request: Request):
    data = await request.json()
    async with httpx.AsyncClient() as client:
        resp = await client.post(f"{AUTH_URL}/auth", json=data)
    return Response(content=resp.content, status_code=resp.status_code)

@app.post("/create-user")
async def create_user_proxy(request: Request):
    data = await request.json()
    async with httpx.AsyncClient() as client:
        resp = await client.post(f"{AUTH_URL}/create-user", json=data)
    return Response(content=resp.content, status_code=resp.status_code)

@app.get("/trainings")
async def trainings_proxy():
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{TRAINING_URL}/trainings")
    return Response(content=resp.content, status_code=resp.status_code)

@app.get("/dashboard")
async def dashboard_proxy():
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{DASHBOARD_URL}/dashboard")
    return Response(content=resp.content, status_code=resp.status_code)

@app.get("/preferences/{username}")
async def get_prefs(username: str):
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{PREFERENCES_URL}/preferences/{username}")
    return Response(content=resp.content, status_code=resp.status_code)

@app.post("/preferences/{username}")
async def save_prefs(username: str, request: Request):
    data = await request.json()
    async with httpx.AsyncClient() as client:
        resp = await client.post(f"{PREFERENCES_URL}/preferences/{username}", json=data)
    return Response(content=resp.content, status_code=resp.status_code)
