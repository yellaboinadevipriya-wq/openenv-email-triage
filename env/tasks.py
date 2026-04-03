import random

TASKS = [
    # EASY
    {
        "level": "easy",
        "email": "I want a refund for my order",
        "intent": "REFUND",
        "action": "REFUND"
    },

    # MEDIUM
    {
        "level": "medium",
        "email": "My payment failed but money was deducted",
        "intent": "PAYMENT_ISSUE",
        "action": "ESCALATE"
    },

    # HARD
    {
        "level": "hard",
        "email": "I received a damaged product",
        "intent": "COMPLAINT",
        "action": "REPLACE"
    }
]

def get_random_task():
    return random.choice(TASKS)
