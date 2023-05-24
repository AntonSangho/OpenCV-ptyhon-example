import cv2 

img = cv2.imread("cat.jpg")
print(img) 

#이미지를 흑백으로 전환하고, img_gray라는 변수에 저장
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

if img is not None: #이미지파일 있으면 아래 실행
    cv2.imshow('original', img) #원본이미지 보이기
    cv2.imshow('gray', img_gray) #흑백이미지 보이기

    cv2.waitKey()           #사용자 키 입력시 기다리기
    cv2.destroyAllWindow()  # 모든 창 종료

else: #이미지가 없는 경우 에러메시지 출력
    print('No imge file.')

