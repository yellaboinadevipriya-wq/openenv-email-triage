from fastapi import FastAPI
from env.environment import EmailEnv
from env.models import Action

app = FastAPI()
env = EmailEnv()

@app.post("/reset")
async def reset():
    result = await env.reset()
    return result.dict()

@app.post("/step")
async def step(action: dict):
    action_obj = Action(**action)
    result = await env.step(action_obj)
    return result.dict()

@app.get("/state")
def state():
    return env.state()

@app.get("/")
def home():
    return {"message": "Email Triage Env Running 🚀"}
