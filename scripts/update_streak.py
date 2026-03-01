import os
import re
from datetime import datetime

# ====== CONFIG ======
LOG_DIR = os.path.join("logs", "2026")
README_PATH = "README.md"

# ====== GET TODAY FILE ======
today = datetime.now().strftime("%m-%d")
log_file = os.path.join(LOG_DIR, f"{today}.md")

# Ensure log directory exists
os.makedirs(LOG_DIR, exist_ok=True)

# Create today's log file if not exists
if not os.path.exists(log_file):
    with open(log_file, "w") as f:
        f.write(f"# Log for {today}\n\n")

# ====== READ README ======
with open(README_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# ====== EXTRACT CURRENT STREAK ======
match = re.search(r"Current Streak:\s*(\d+)", content)

if match:
    current_streak = int(match.group(1))
else:
    current_streak = 0

# ====== UPDATE STREAK ======
# If today's log exists → increase streak
if os.path.exists(log_file):
    new_streak = current_streak + 1
else:
    new_streak = current_streak

# Replace only the streak number
if match:
    new_content = re.sub(
        r"(Current Streak:\s*)\d+",
        rf"\g<1>{new_streak}",
        content
    )
else:
    # If line not found, add it
    new_content = content + f"\n\n## 🔥 Current Streak: {new_streak}\n"

# ====== WRITE BACK ======
with open(README_PATH, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"Updated streak to: {new_streak}")