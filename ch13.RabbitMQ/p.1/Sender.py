# pika 불러오기
from email import message
import pika

# 서버와 연결.
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

# 연결 안에서 채널을 생성
channel = connection.channel()

# 채널 안에서 큐를 선언 >> 새 큐를 만드는 작업
channel.queue_declare(queue='hello')

# 메시지를 보내기
#  여기서는 교환기excahnge와 routing_key를 다루지 않을 겁니다.
# print("# 메시지를 보냈습니다!")
# message = 'Hello Miku!!!'

for i in range(1000):
    # 10,000개의 메시지를 큐에 쌓습니다.
    # channel.basic_publish(exchange='', routing_key='hello', body=message)
    # print(f"sent message : {message}")
    channel.basic_publish(exchange='', routing_key='hello', body=str(i))
    print("# 메시지를 보냈습니다!" + str(i))
    
# print("# 메시지를 보냈습니다!")

# 서버와의 연결을 끊기
connection.close()
