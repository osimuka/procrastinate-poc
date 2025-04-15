from procrastinate.contrib.django import app

@app.task
def add(x, y):
    print(f"Result: {x + y}")
