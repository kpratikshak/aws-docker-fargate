from flask import Flask, render_template
from datetime import datetime
import random

app = Flask(__name__)

quotes = [
    "Keep pushing forward.",
    "AWS makes life easier.",
    "Containers rule the world.",
    "Cloud is the limit!",
    "Discipline builds character.",
    "Consistency beats intensity.",
    "Automation is your friend."
]

@app.route("/")
def home():
    return render_template(
        "index.html",
        quote=random.choice(quotes),
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
