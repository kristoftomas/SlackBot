import slack
import os
from pathlib import Path
from dotenv import load_dotenv
import requests
from datetime import datetime

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)
today = datetime.now()

# slack token stored in .env file; ignore for gitghub
client = slack.WebClient(token=os.environ["SLACK_TOKEN"])

# -- GET THE QUOTE & FORMAT IT --
r = requests.get("https://api.quotable.io/random")
r = r.json()
quotecontent = r["content"]
quoteauthor = r["author"]

# put the above into a nice final string
quote = quotecontent + " " + "– " + quoteauthor + " –"


# -- SEND IT OUT ON WEEKDAYS AT 8 AM --
Days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

if today.strftime("%A") in Days and today.strftime("%H:%M") == "08:00":
    client.chat_postMessage(channel="#testbot", text=quote)