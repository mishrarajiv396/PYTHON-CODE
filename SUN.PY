import subprocess
import re

# Define the path to the uploaded file
file_path = "/mnt/data/glade"

# Run the 'strings' command to extract readable strings from the binary file
try:
    result = subprocess.run(["strings", file_path], stdout=subprocess.PIPE, text=True, check=True)
except FileNotFoundError:
    print("Error: 'strings' command not found. Please ensure it is installed and available in your PATH.")
    exit(1)
except subprocess.CalledProcessError as e:
    print(f"Error while running 'strings': {e}")
    exit(1)

# Collect all lines
all_strings = result.stdout.splitlines()

# Filter for likely candidates that could contain flag info, especially looking for patterns like base64, or keywords like "flag", "user", "pass"
flag_candidates = [
    line for line in all_strings 
    if re.search(r'flag\{.*?\}', line, re.IGNORECASE) or re.search(r'^[A-Za-z0-9+/=]{10,}$', line)
]

# Show first 20 possible candidates for analysis
print(flag_candidates[:20])