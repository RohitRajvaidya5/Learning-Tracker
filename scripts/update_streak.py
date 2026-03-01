import os
import re

# -----------------------------
# Paths
# -----------------------------
base_dir = os.getcwd()
log_dir = os.path.join(base_dir, "logs", "2026")
readme_path = os.path.join(base_dir, "README.md")

# -----------------------------
# Get latest log file
# -----------------------------
latest_log = max(
    os.listdir(log_dir),
    key=lambda x: os.path.getmtime(os.path.join(log_dir, x))
)

with open(os.path.join(log_dir, latest_log), "r", encoding="utf-8") as f:
    content = f.read().strip()

# -----------------------------
# Read README
# -----------------------------
with open(readme_path, "r", encoding="utf-8") as f:
    readme = f.read()

# -----------------------------
# Update Last Logs Section
# -----------------------------
last_logs_pattern = r"(## Last Logs\s*\n---\s*\n)(.*?)(?=\n## |\Z)"

readme = re.sub(
    last_logs_pattern,
    lambda m: m.group(1) + content + "\n",
    readme,
    flags=re.DOTALL
)

# -----------------------------
# Update Current Streak
# -----------------------------
current_pattern = r"(## Current Streak\s*\n---\s*\n)(\d+)"

match = re.search(current_pattern, readme)
current_streak = int(match.group(2)) if match else 0
new_current = current_streak + 1

readme = re.sub(
    current_pattern,
    lambda m: m.group(1) + str(new_current),
    readme
)

# -----------------------------
# Update Total Streak
# -----------------------------
total_pattern = r"(## Total Streak\s*\n---\s*\n)(\d+)"

match = re.search(total_pattern, readme)
total_streak = int(match.group(2)) if match else 0
new_total = total_streak + 1

readme = re.sub(
    total_pattern,
    lambda m: m.group(1) + str(new_total),
    readme
)

# -----------------------------
# Write back
# -----------------------------
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(readme)

print("README updated successfully.")