import cv2
import numpy as np

def cartoonize_image(image_path):
    # 이미지 불러오기
    img = cv2.imread(image_path)
    if img is None:
        print("이미지를 불러오는 데 실패했습니다.")
        return

    # 그레이스케일 변환 및 중간값 블러링
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)

    # 윤곽선 감지
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    # 색상 단순화 (파라미터 조정)
    color = cv2.bilateralFilter(img, 5, 100, 100) # d, sigmaColor, sigmaSpace 값을 조정

    # 윤곽선과 색상 결합
    cartoon = cv2.bitwise_and(color, color, mask=edges)


    # 결과 이미지 표시
    cv2.imshow("Original Image", img)
    cv2.imshow("Cartoonized Image", cartoon)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 사용 예시
input_image_path = "input.jpg"  # 변환할 이미지 파일 경로
cartoonize_image(input_image_path)
