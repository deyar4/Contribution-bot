import base64
import time
import os
import requests

# Set the environment variables
REPO_NAME = "deyar4/Contribution-bot"
GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
DAD_JOKE_API_URL = "https://icanhazdadjoke.com/"

while True:
    # Fetch a random dad joke from the API
    headers = {"Accept": "application/json"}
    response = requests.get(DAD_JOKE_API_URL, headers=headers)

    if response.status_code == 200:
        joke = response.json()["joke"]
    else:
        joke = "Why couldn't the bot commit the joke? Because it was a bit buggy."

    # Define the commit payload
    payload = {
        "message": f"I am the bot that updated Dyars profile",
        "content": base64.b64encode(joke.encode("utf-8")).decode("utf-8")
    }

    # Make the commit request
    url = f"https://api.github.com/repos/{REPO_NAME}/contents/dad_joke.txt"
    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}
    response = requests.put(url, json=payload, headers=headers)

    if response.status_code == 200:
        print(f"Committed successfully! Day {now.strftime('%d')} of the streak.")
    else:
        print(f"Failed to commit.")

    time.sleep(8 * 60 * 60)

