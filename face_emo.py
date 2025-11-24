import cv2

# URL do DroidCam (troque pelo seu IP!)
url = "http://172.25.253.86:4747/video"
cap = cv2.VideoCapture(url)

def cartoonize(image):
    # 1 - Converter para cinza
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 2 - Blur para suavizar
    gray_blur = cv2.medianBlur(gray, 7)

    # 3 - Bordas estilo desenho
    edges = cv2.adaptiveThreshold(gray_blur, 255,
                                  cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY,
                                  9, 5)

    # 4 - Suavizar cores (filtro bilateral)
    color = cv2.bilateralFilter(image, 15, 250, 250)

    # 5 - Combinar cores suaves + bordas fortes
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    return cartoon


while True:
    ret, frame = cap.read()
    if not ret:
        print("Não conseguiu acessar o DroidCam!")
        break

    cartoon_frame = cartoonize(frame)

    cv2.imshow("Filtro Cartoon", cartoon_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
