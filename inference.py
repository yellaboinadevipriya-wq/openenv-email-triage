import os
import asyncio
from openai import OpenAI
from env.environment import EmailEnv
from env.models import Action

API_KEY = os.getenv("HF_TOKEN")
BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
MODEL = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-72B-Instruct")

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

def log_start(task, env, model):
    print(f"[START] task={task} env={env} model={model}", flush=True)

def log_step(step, action, reward, done, error):
    print(f"[STEP] step={step} action={action} reward={reward:.2f} done={str(done).lower()} error={error or 'null'}", flush=True)

def log_end(success, steps, rewards):
    rewards_str = ",".join(f"{r:.2f}" for r in rewards)
    print(f"[END] success={str(success).lower()} steps={steps} rewards={rewards_str}", flush=True)

async def main():
    env = EmailEnv()
    rewards = []

    log_start("email_task", "email_env", MODEL)

    res = await env.reset()

    email = res.observation.email_text

    prompt = f"""
    Read the email and respond in JSON:
    {{
        "intent": "...",
        "action": "...",
        "response": "..."
    }}

    Email: {email}
    """

    completion = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100
    )

    text = completion.choices[0].message.content

    try:
        import json
        data = json.loads(text)
    except:
        data = {"intent": "", "action": "", "response": ""}

    action = Action(**data)

    result = await env.step(action)

    rewards.append(result.reward)

    log_step(1, str(data), result.reward, result.done, None)

    success = result.reward > 0.5

    log_end(success, 1, rewards)

    await env.close()

asyncio.run(main())
