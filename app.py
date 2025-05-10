from flask import Flask, render_template, request, redirect
from event_handler import emitter
from agent import handle_question
import json
import uuid
import os
from datetime import datetime

app = Flask(__name__)

# Load or initialize requests
REQUESTS_FILE = "requests.json"
if os.path.exists(REQUESTS_FILE):
    with open(REQUESTS_FILE, "r") as f:
        requests = json.load(f)
else:
    requests = {}

def save_requests():
    with open(REQUESTS_FILE, "w") as f:
        json.dump(requests, f, indent=2)

def on_help_request(question, caller_id):
    req_id = str(uuid.uuid4())
    requests[req_id] = {
        "question": question,
        "caller_id": caller_id,
        "status": "pending",
        "timestamp": str(datetime.now())
    }
    save_requests()
    print(f" Supervisor Alert: Need help answering: {question}")

emitter.on("help_request", on_help_request)

@app.route("/")
def index():
    return render_template("index.html", requests=requests)

@app.route("/submit", methods=["POST"])
def submit():
    req_id = request.form["req_id"]
    answer = request.form["answer"]
    question = requests[req_id]["question"]
    requests[req_id]["answer"] = answer
    requests[req_id]["status"] = "resolved"

    with open("knowledge_base.json", "r+") as f:
        kb = json.load(f)
        kb[question] = answer
        f.seek(0)
        json.dump(kb, f, indent=2)
        f.truncate()

    save_requests()
    print(f" AI replies to caller: {answer}")
    return redirect("/")

@app.route("/ask", methods=["POST"])
def ask():
    question = request.form["question"]
    caller_id = "dummy_001"
    answer = handle_question(question, caller_id)
    return f"<p><b>AI:</b> {answer}</p><a href='/'>Back</a>"

@app.route("/history")
def history():
    return render_template("history.html", requests=requests)

@app.route("/learned")
def learned():
    with open("knowledge_base.json", "r") as f:
        kb = json.load(f)
    return render_template("learned.html", kb=kb)

if __name__ == "__main__":
    app.run(debug=True)