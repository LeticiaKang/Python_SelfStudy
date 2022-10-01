# pika를 임포트합니다.
import pika

# 서버와 연결
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

# 연결 안에서 채널을 생성
channel = connection.channel()

# 채널 안에서 큐를 선언 / 새 큐를 생성함
# 이미 발송기 쪽에서 큐를 만들었지만, 확실히 하기 위해서 여기서 한 번 더 만들어주는 것
channel.queue_declare(queue='hello')

# 큐에서 가져온 메시지를 처리할 "콜백 함수"를 만들기
# channel.basic_publish에서 설정한 body를 가져와서 출력한다.
def callback(ch, method, properties, body):
    print(" # 메시지를 받았습니다: %r" % body)

# 메시지를 보낼 때 어떻게 할 것인지 설정한다.
# 함수, 큐, 응답 여부(no_ack)를 지정
channel.basic_consume(queue='hello', auto_ack=True, on_message_callback=callback)
# channel.basic_consume( queue='hello', on_message_callback=callback , auto_ack=True)
# channel.basic_consume( callback, 'hello', auto_ack=True) #오류로 인해 위코드 바꿈

print('# 메시지를 기다리고 있습니다. 종료하려면 CTRL+C를 누르세요')

# 메시지 보내기를 시작합니다. 명시적으로 종료하기 전까지 계속 실행되면서
# 큐에 메시지가 들어올 때마다 callback이 메시지를 처리합니다.
channel.start_consuming()
