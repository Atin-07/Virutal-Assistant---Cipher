import webbrowser
from datetime import datetime
from core.router import skill

@skill(["time"])
def tell_time(text):
    return datetime.now().strftime("It is %I:%M %p")

@skill(["date"])
def tell_date(text):
    return datetime.now().strftime("Today is %A, %d %B %Y")

@skill(["open youtube"])
def open_youtube(text):
    webbrowser.open("https://youtube.com")
    return "Opening YouTube"