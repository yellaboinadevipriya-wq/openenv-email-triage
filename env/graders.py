def grade(task, action):
    score = 0.0

    if action.intent == task["intent"]:
        score += 0.3

    if action.action == task["action"]:
        score += 0.3

    if task["level"] == "easy":
        return 1.0 if score >= 0.6 else 0.0

    if task["level"] == "medium":
        return score

    if task["level"] == "hard":
        if action.response:
            text = action.response.lower()
            if "sorry" in text:
                score += 0.2
            if len(text) > 20:
                score += 0.2

    return min(score, 1.0)
