from flask import Flask, request, jsonify,render_template
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


SYSTEM_PROMPT = """
You are an AI travel booking assistant.
Ask for missing travel details.
Do not assume missing values.
"""

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message")

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message}
        ]
    )

    return jsonify({
        "reply": response.choices[0].message.content
    })

if __name__ == "__main__":
    app.run(debug=True)