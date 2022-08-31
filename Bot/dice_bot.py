# AdX : A개의 X면체 주사위

# 1. 슬랙봇 API 토큰 얻기
# 토큰 : xoxb-4027440923633-4039540055472-tvdrtP1ngE3nJ4COwOWs0FBI

from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.dispatcher import Message
import re 
# re : 정규 표현식 패키지

@listen_to("Hello", re.IGNORECASE)
# listen_to : 모든 대화에 반응
# 디코레이터 함수의 첫 번째 파라미터는 정규표현식, 두번때는 플래그

def hello(msg : Message):
    msg.send("World!!")
# 첫 번째 파라미터는 디스패처의 메시지 클래스입니다.
# 반응해야 할 채널에 메시지를 보내는 함수등이 있습니다.
# 여기 없는 두 번째 이후의 파라미터는 위 정규식에 그룹이 있을 경우 매칭된 문자열이 들어갑니다.
# 개수는 상한이 없습니다. 그룹 숫자에 따라 파라미터를 더 늘리면 됩니다.    

def hello(msg: Message):
    # send는 채널에 그냥 말합니다.
    msg.send("World!!")

# respond_to는, @을 이용해서 멘션했을 경우에만 반응합니다. 나머지는 listen_to의 역할과 같습니다.
@respond_to("hi", re.IGNORECASE)
def hi(msg: Message):
    # reply는 해당 반응을 일으킨 사람에게 말합니다.
    # listen_to든 respond_to든 말을 건 사람에게 대답합니다.
    msg.reply("Thank you 39!!")

# 무작위 숫자를 생성하기 위한 random 모듈을 임포트합니다.
import random

from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.dispatcher import Message
import re

# 'roll 던지는횟수d숫자면체' 형식으로 메시지를 입력하는 hello() 함수를 정의합니다.
@listen_to("roll (\d*)d(\d+)", re.IGNORECASE)

# 메시지, 주사위를 던지는 횟수, 주사위의 면체를 지정하는 파라미터를 넣어줍니다.
def hello(msg: Message, number_of_die: str, side_of_die: str):
    #
    roll_result = [random.randrange(1, int(side_of_die), 1) for i in range(int(number_of_die))]

    # 주사위를 던진 횟수만큼 나온 숫자를 모두 더합니다.
    roll_sum = sum(roll_result)

    # 주사위를 던져서 나온 숫자와 합을 메시지로 출력합니다.
    msg.send(str(roll_result))
    msg.send(str(roll_sum))
