import json
from event_handler import emitter

with open('knowledge_base.json') as f:
    knowledge = json.load(f)

def handle_question(question, caller_id):
    if question in knowledge:
        return knowledge[question]
    else:
        emitter.emit("help_request", question, caller_id)
        return "Let me check with my supervisor and get back to you."