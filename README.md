# Frontdesk.ai – AI Supervisor Simulation Project

This is a simulated AI call-handling system built using Python and Flask for the Frontdesk.ai coding assessment. It handles known customer queries, escalates unknown ones to a supervisor, and learns new answers over time.

---

##  Tech Stack

- Python 3
- Flask – Web framework (for routing and HTML rendering)
- HTML/Jinja2 – Simple admin UI
- JSON – For persistent storage (knowledge_base.json and requests.json)

---

##  Features

- AI answers known questions from a JSON-based knowledge base
- Unknown questions are escalated to a supervisor
- Supervisor can view pending requests and submit answers
- Answers are saved to the knowledge base permanently
- AI "texts back" the user via console log once supervisor responds
- `/history` page shows resolved questions
- `/learned` page shows current knowledge base
- All data is persisted using requests.json

---

##  How to Run the Project

1. Clone this repo:
   git clone https://github.com/Anindita-Mandal/frontdesk-ai-supervisor.git  
   cd frontdesk-ai-supervisor

2. Install dependencies:
   pip install flask

3. Run the Flask app:
   python app.py

4. Open in your browser:
   - Dashboard: http://127.0.0.1:5000  
   - View resolved requests: http://127.0.0.1:5000/history  
   - View learned answers: http://127.0.0.1:5000/learned

---

##  Project Structure

- app.py – Main app with all routes  
- agent.py – AI logic  
- event_handler.py – Lightweight event system  
- knowledge_base.json – Stored Q&A  
- requests.json – All help requests (pending/resolved)  
- templates/  
  ├── index.html – Supervisor dashboard  
  ├── history.html – View resolved help requests  
  └── learned.html – View knowledge base

---

##  Key Design Decisions

- **Modularity**: The AI agent logic, event system, and Flask routes are separated into different files for clarity and maintainability.
- **Storage**: Used JSON files for knowledge and help requests to keep the system lightweight and persistent without a database.
- **Escalation logic**: Used a simple EventEmitter class to simulate "help request" events when the AI doesn’t know something.
- **Learning**: Supervisor responses are permanently added to the knowledge base so the AI improves over time.
- **Console Simulation**: All messaging is simulated via console logs — just like how you'd text a human-in-the-loop.

---

##  Improvements for the Future

- Replace JSON storage with a real-time database (e.g., Firebase or Firestore)
- Integrate LiveKit or Twilio for actual call/audio support
- Add supervisor notifications (email, Slack, or webhook)
- Implement request timeouts → mark as "unresolved" if unanswered
- Add login/authentication for secure supervisor access
- Improve UI with filters, search, or real-time updates

---

##  Demo Video

*A 2-minute screen recording demo showing:*
- Asking a known & unknown question
- Supervisor resolving a help request
- AI learning and answering it next time
- Viewing history and knowledge base

 [Insert your Loom or Drive video link here]

---

**Created by Anindita Mandal – Frontdesk.ai Assessment – May 2025**
