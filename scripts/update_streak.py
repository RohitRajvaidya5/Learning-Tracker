import os
from datetime import datetime

LOG_DIR = "logs\\2026"

today = datetime.now().strftime("%m-%d")
print(today)
log_file = os.path.join(LOG_DIR, f"{today}.md")
print(log_file)

streak = 0

if os.path.exists(log_file):
    streak = streak + 1  # basic example

readme_path = "README.md"

with open(readme_path, "r") as f:
    content = f.read()
    

new_content = content.replace(
    "0 days",
    f"{streak} days"
)

print(new_content)

with open(readme_path, "w") as f:
    f.write(new_content)