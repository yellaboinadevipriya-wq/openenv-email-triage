from env.models import Observation, Action, StepResult
from env.tasks import get_random_task
from env.graders import grade

class EmailEnv:

    def __init__(self):
        self.task = None
        self.done = False

    async def reset(self):
        self.task = get_random_task()
        self.done = False

        return StepResult(
            observation=Observation(
                email_text=self.task["email"],
                history=[]
            ),
            reward=0.0,
            done=False,
            info={}
        )

    async def step(self, action: Action):
        if self.done:
            return await self.reset()

        score = grade(self.task, action)
        self.done = True

        return StepResult(
            observation=Observation(
                email_text=self.task["email"],
                history=[]
            ),
            reward=score,
            done=True,
            info={}
        )

    def state(self):
        return self.task

    async def close(self):
        pass
