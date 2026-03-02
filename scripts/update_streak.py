import json
from pathlib import Path
from datetime import datetime, date, timedelta

# === Configuration ===
STATE_FILE = Path("streak.json")
README_FILE = Path("README.md")
RESET_IF_MISSED_DAY = True  # If True: reset streak when there's a gap > 1 day

# === Helpers ===
def load_state():
    if not STATE_FILE.exists():
        return {"streak": 0, "last_update_date": None}
    try:
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    except Exception:
        # Fallback if file is corrupted
        return {"streak": 0, "last_update_date": None}

def save_state(state):
    STATE_FILE.write_text(json.dumps(state, indent=2), encoding="utf-8")

def date_from_str(s):
    return datetime.strptime(s, "%Y-%m-%d").date()

def date_to_str(d: date):
    return d.strftime("%Y-%m-%d")

# === Main Logic ===
today = date.today()
state = load_state()
last_update_str = state.get("last_update_date")
streak = int(state.get("streak", 0))

if last_update_str is None:
    # First ever run
    streak = 1
    state["last_update_date"] = date_to_str(today)
elif last_update_str == date_to_str(today):
    # Already updated today: DO NOT change streak
    pass
else:
    # Compare with previous date
    last_update = date_from_str(last_update_str)
    if today == last_update + timedelta(days=1):
        # Consecutive day → increment
        streak += 1
        state["last_update_date"] = date_to_str(today)
    else:
        # Missed one or more days
        if RESET_IF_MISSED_DAY:
            streak = 1  # start over
        else:
            # Or keep streak unchanged if you prefer
            # streak = streak
            pass
        state["last_update_date"] = date_to_str(today)

# Persist state (even if unchanged—it’s safe)
state["streak"] = streak
save_state(state)

# === README Update ===
message = f"""
# 🚀 Learning Tracker
> Consistency builds mastery. This repo chronicles my daily journey of learning, growth, and curiosity.

---

## 📅 Today's Progress
**Date:** {today.strftime("%Y-%m-%d")}

### 🧠 Topics Studied
-

### 📚 Resources Used
-

### 💡 Insights / Challenges
-

---

## 🔥 Learning Streak
### Current Streak: {streak} Days"""

# Always overwrite README with current template (idempotent)
README_FILE.write_text(message, encoding="utf-8")