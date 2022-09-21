from slackbot.bot import Bot
from slackbot.bot import listen_to

bot = Bot()

@listen_to('안녕')
def sample(message):
    message.send("안녕하세요?")

bot.run()