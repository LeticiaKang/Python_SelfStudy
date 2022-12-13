# import cv2
# import numpy as np
#
# isDragging = False  # 마우스 드래그 상태 저장
# x0, y0, w, h = -1, -1, -1, -1  # 영역 선택 좌표 저장
# blue, red = (255, 0, 0), (0, 0, 255)  # 색상 값
#
#
# def onMouse(event, x, y, flags, param):  # 마우스 이벤트 핸들 함수
#     global isDragging, x0, y0, img  # 전역 변수 참조
#     if event == cv2.EVENT_LBUTTONDOWN:  # 왼쪽 마우스 버튼 다운, 드래그 시작
#         isDragging = True
#         x0 = x
#         y0 = y
#
#     elif event == cv2.EVENT_MOUSEMOVE:  # 마우스 움직임
#         if isDragging:  # 드래그 진행 중
#             img_draw = img.copy()  # 사각형 그림 표현을 위한 이미지 복제 (매번 같은 이미지에 그려지면 이미지가 더러워짐)
#             cv2.rectangle(img_draw, (x0, y0), (x, y), blue, 2)  # 드래그 진행 영역 표시
#             cv2.imshow('img', img_draw)  # 사각형으로 표시된 그림 화면 출력
#
#     elif event == cv2.EVENT_LBUTTONUP:  # 왼쪽 마우스 버튼 업
#         if isDragging:  # 드래그 중지
#             isDragging = False
#             w = x - x0  # 드래그 영역 폭 계산
#             h = y - y0  # 드래그 영역 높이 계산
#             print("x%d, y%d, w%d, h%d" % (x0, y0, w, h))
#             if w > 0 and h > 0:  # 폭과 높이가 양수이면 드래그 방향이 옳음
#                 img_draw = img.copy()  # 선택 영역에 사각형 그림을 표시할 이미지 복제
#                 cv2.rectangle(img_draw, (x0, y0), (x, y), red, 2)  # 선택 영역에 빨간색 사각형 표시
#                 cv2.imshow('img', img_draw)  # 빨간색 사각형이 그려진 이미지 화면 출력
#                 roi = img[y0:y0 + h, x0:x0 + w]  # 원본 이미지에서 선택 영역만 ROI로 지정
#                 cv2.imshow('cropped', roi)  # ROI 지정 영역을 새 창으로 표시
#                 cv2.moveWindow('cropped', 0, 0)  # 새 창을 화면 좌측 상단으로 이동
#                 cv2.imwrite('../CV2/img/cropped.jpg', roi)  # ROI 영역만 파일로 저장
#                 print('cropped.')
#
#             else:
#                 # 드래그 방향이 잘못된 경우 사각형 그림이 없는 원본 이미지 출력
#                 cv2.imshow('img', img)
#                 print('좌측 상단에서 우측 하단으로 영역을 드래그하세요.')
#
#
# img = cv2.imread(r'C:\Self_Study\PythonStudy\ImageClassification\image_data\blackpink_channel.jpg')
# resize_img = cv2.resize(img, (550, 700))
# cv2.imshow('img', resize_img)
# cv2.setMouseCallback('img', onMouse)  # 마우스 이벤트 등록
# cv2.waitKey()
# cv2.destroyAllWindows()

# 1. cv2라이브러리로 간단히 하기
import cv2, numpy as np

img = cv2.imread(r'C:\Self_Study\PythonStudy\ImageClassification\image_data\blackpink_channel.jpg')
# resize_img = cv2.resize(img, (550, 700))

# cv2.selectROI( [win_name,], img[, showCrossHair=True, fromCenter=Flase] ) - ROI 지정
# 입력 : win_name - ROI 선택을 진행할 창의 이름, str
#       ing - ROI 선택을 진행할 이미지, numpy ndarray
#       showCrissHair - 선택 영역 중심에 십자 모양 표시 여부
#       fromCenter - 마우스 시작 지점을 영역의 중심으로 지정
#       ret - 선택한 영역 좌표와 크기( x, y, w, h ), 선택을 취소한 경우 모두 0

x, y, w, h = cv2.selectROI('img', img, False)
if w and h:
    roi = img[y:y + h, x:x + w]
    cv2.imshow('cropped', roi)  # ROI 지정 영역을 새창으로 표시
    cv2.moveWindow('cropped', 0, 0)  # 새창을 화면 측 상단으로 이동
    cv2.imwrite(r'C:\Self_Study\PythonStudy\ImageClassification\image_data\cropped2.jpg', roi)  # ROI 영역만 파일로 저장

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()