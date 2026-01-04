from flask import Flask, render_template_string
from datetime import date
import hashlib

app = Flask(__name__)

SUGGESTIONS = [
    "Say one genuine thank-you to your partner today.",
    "Listen without interrupting for at least 5 minutes.",
    "Send a loving message during the day.",
    "Appreciate something small they usually do.",
    "Give a hug with no expectation attached.",
    "Ask how their day was and really mean it.",
    "Compliment them on something specific.",
    "Do one small task to make their day easier.",
    "Put your phone away when they are talking.",
    "End the day by saying one good thing about them."
]

def get_today_suggestion():
    today = date.today().isoformat()
    hash_value = int(hashlib.md5(today.encode()).hexdigest(), 16)
    index = hash_value % len(SUGGESTIONS)
    return SUGGESTIONS[index]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Daily Relationship Tip</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(to bottom right, #ffe6e6, #fff);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .card {
            background: white;
            padding: 25px;
            max-width: 400px;
            border-radius: 16px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.1);
            text-align: center;
        }
        h1 { font-size: 22px; }
        p { font-size: 16px; color: #444; }
        .heart { font-size: 32px; color: red; }
        footer { font-size: 12px; color: #aaa; margin-top: 15px; }
    </style>
</head>
<body>
    <div class="card">
        <div class="heart">❤️</div>
        <h1>Today's Relationship Tip</h1>
        <p>{{ suggestion }}</p>
        <footer>Same tip for everyone · Changes daily</footer>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    suggestion = get_today_suggestion()
    return render_template_string(HTML_TEMPLATE, suggestion=suggestion)

if __name__ == "__main__":
    app.run(debug=True)
