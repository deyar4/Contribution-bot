import base64
import datetime
import os
import requests

# Set the environment variables
REPO_NAME = "deyar4/Contribution-bot"
GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
DAD_JOKE_API_URL = "https://icanhazdadjoke.com/"

# Get the current date
now = datetime.datetime.now()

# Fetch a random dad joke from the API
headers = {"Accept": "application/json"}
response = requests.get(DAD_JOKE_API_URL, headers=headers)

if response.status_code == 200:
    joke = response.json()["joke"]
else:
    joke = "Why couldn't the bot commit the joke? Because it was a bit buggy."

# Define the commit payload
payload = {
    "message": f"I am the bot that updated Dyars profile for the day number {now.strftime('%d')}",
    "content": joke.encode("base64").decode("utf-8")
}

# Make the commit request
url = f"https://api.github.com/repos/{REPO_NAME}/contents/dad_joke.txt"
headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}
response = requests.put(url, json=payload, headers=headers)

if response.status_code == 200:
    print(f"Committed successfully! Day {now.strftime('%d')} of the streak.")
else:
    print(f"Failed to commit.")

