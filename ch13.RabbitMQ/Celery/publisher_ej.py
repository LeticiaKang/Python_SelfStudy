# 앞서 만든 태스크 코드를 임포트합니다.
import task_ej

# 태스크 코드에서 태스크로 지정했던 함수를 바로 호출하지 않고 delay를 사용해서 호출합니다.
task_ej.add.delay(2, 2)

# 태스크 코드에서 태스크로 지정했던 함수를 바로 호출하지 않고 delay를 사용해서 호출합니다.
result = task_ej.add.delay(3, 9)

# print("Get result")

# result.get()으로 결과를 받아옵니다
print(result.get(propagate=False))

# 다른 코드에서 다음 코드를 이용해 task_id를 활용할 수도 있습니다.
# task_id = "9f622a26-5ea7-4c39-a0ef-8f39771aa91f"
# task_ej.app.AsyncResult(task_id).get()
