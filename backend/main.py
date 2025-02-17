from flask import Flask, request, render_template, redirect, url_for
import json
import os
from datetime import datetime, timedelta
from collections import defaultdict

app = Flask(__name__)

# Path to the JSON file where feedback is stored
FEEDBACK_FILE = os.path.join(os.path.dirname(__file__), "feedbacks.json")

if not os.path.exists(FEEDBACK_FILE):
    with open(FEEDBACK_FILE, "w") as f:
        json.dump([], f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/feedback", methods=["POST"])
def submit_feedback():
    feedback_text = request.form.get("feedback", "").strip()

    with open(FEEDBACK_FILE, "r") as f:
        feedback_list = json.load(f)

    new_feedback = {
        "id": int(datetime.now().timestamp()),
        "text": feedback_text,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    feedback_list.append(new_feedback)

    with open(FEEDBACK_FILE, "w") as f:
        json.dump(feedback_list, f, indent=2)

    return redirect(url_for("all_feedbacks"))

@app.route("/feedbacks")
def all_feedbacks():
    with open(FEEDBACK_FILE, "r") as f:
        feedback_list = json.load(f)
    return render_template("feedbacks.html", feedbacks=feedback_list)

# ---------------------------
#        DASHBOARD ROUTE
# ---------------------------
@app.route("/dashboard")
def dashboard():
    # Load all feedback
    with open(FEEDBACK_FILE, "r") as f:
        feedback_list = json.load(f)

    total_feedback = len(feedback_list)
    
    # Convert timestamps to datetime objects
    # We'll group by day for a simple chart
    date_format = "%Y-%m-%d %H:%M:%S"
    
    # We'll track counts of feedback per date (YYYY-MM-DD)
    feedback_count_by_date = defaultdict(int)

    for fb in feedback_list:
        ts_str = fb.get("timestamp")
        if not ts_str:
            continue
        try:
            dt_obj = datetime.strptime(ts_str, date_format)
            date_str = dt_obj.strftime("%Y-%m-%d")
            feedback_count_by_date[date_str] += 1
        except:
            # If timestamp invalid, skip
            continue

    # Optional: Calculate feedback in the last 7 days
    # We'll create a list of date strings from oldest to newest
    last_7_days = []
    today = datetime.today()
    for i in range(7):
        day = (today - timedelta(days=(6 - i))).strftime("%Y-%m-%d")
        last_7_days.append(day)

    # Build data for chart labels and counts
    chart_labels = []
    chart_data = []
    for day_str in last_7_days:
        chart_labels.append(day_str)
        chart_data.append(feedback_count_by_date.get(day_str, 0))

    # Optional stats for the dashboard:
    # e.g., find the most recent feedback
    most_recent_feedback = None
    if feedback_list:
        # Sort by timestamp descending
        feedback_sorted = sorted(
            feedback_list, 
            key=lambda x: x["timestamp"], 
            reverse=True
        )
        most_recent_feedback = feedback_sorted[0]

    return render_template(
        "dashboard.html",
        total_feedback=total_feedback,
        chart_labels=chart_labels,
        chart_data=chart_data,
        most_recent_feedback=most_recent_feedback
    )

if __name__ == "__main__":
    app.run(debug=True)