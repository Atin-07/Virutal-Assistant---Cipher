SKILLS = []

def skill(keywords):
    def wrapper(func):
        SKILLS.append((keywords, func))
        return func
    return wrapper

def handle(text):
    text = text.lower()
    for keywords, func in SKILLS:
        if any(k in text for k in keywords):
            return func(text)
    return "Sorry, I don't know how to do that yet."