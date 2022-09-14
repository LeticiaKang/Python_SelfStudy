from importlib.resources import path
import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

env_path = ".env"

bot_token = os.environ.get("SLACK_BOT_TOKEN")
app_token = os.environ.get("SLACK_APP_TOKEN")

app = App(token = bot_token)

@app.message("hello")
def message_handler(message, say):
    say(f"Hey there <@{message['user']}>!!")

if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()