from flask import Flask, render_template, request

app = Flask(__name__)

danger_keywords = [
    "give up", "die", "depressed", "suicidal", "end it", "kill myself",
    "hopeless", "alone", "useless", "tired of life", "ending everything","i dont want life"
]

positive_responses = [
    "You're not alone. Please talk to someone you trust.",
    "You're strong, even if it doesn't feel like it right now.",
    "This moment will pass. You matter.",
    "Talking helps. Reach out to a loved one or call a helpline.",
    "You’re not a burden. You’re a human with emotions. Stay strong."
    "ok die no body cares"
]

helpline = "India Helpline: 9152987821 (Free, 24x7)"

@app.route("/", methods=["GET", "POST"])
def home():
    bot_response = ""
    if request.method == "POST":
        user_input = request.form["message"].lower()
        
        danger = any(keyword in user_input for keyword in danger_keywords)
        
        if danger:
            bot_response = f"I'm really sorry you're feeling this way. {positive_responses[0]} <br><br> Helpline: {helpline}"
        else:
            bot_response = positive_responses[1]
    
    return render_template("index.html", bot_response=bot_response)

if __name__ == "__main__":
    app.run(debug=True)
     