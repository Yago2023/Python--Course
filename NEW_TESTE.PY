import cv2
import numpy as np
import dlib
from imutils import face_utils

# Iniciando a câmera
cap = cv2.VideoCapture(0)

# Iniciando detecção de rosto e marca em rosto
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("C:/Users/Speedbird/Downloads/shape_predictor_68_face_landmarks.dat")

# Status que serão reconhecidos

sleep = 0
drowsy = 0
active = 0
status = ""
color = (0, 0, 0)
face_frame = 0


def compute(ptA, ptB):
    dist = np.linalg.norm(ptA - ptB)
    return dist


def blinked(a, b, c, d, e, f):
    up = compute(b, d) + compute(c, e)
    down = compute(a, f)
    ratio = up / (2.0 * down)

    # Verificando se está piscando
    if ratio > 0.25:  # considera que está piscando
        return 2
    elif ratio > 0.21 and ratio <= 0.25:
        return 1  # considera que há um potencial de piscada
    else:
        return 0  # caso não estiver piscando


while True:  # verifica em tempo real
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # converte para cinza

    faces = detector(gray)  # procura qualquer rosto em cinza
    # detected face in faces array
    for face in faces:  # extrai informações do rosto que encontro
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()

        face_frame = frame.copy()
        cv2.rectangle(face_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        landmarks = predictor(gray, face)  # procurar pontos específicos do rosto
        landmarks = face_utils.shape_to_np(landmarks)

        # The numbers are actually the landmarks which will show eye
        left_blink = blinked(landmarks[36], landmarks[37],
                              landmarks[38], landmarks[41], landmarks[40], landmarks[39])
        right_blink = blinked(landmarks[42], landmarks[43],
                               landmarks[44], landmarks[47], landmarks[46], landmarks[45])

        # Avaliação do estado de sono/vigília
        if left_blink == 0 or right_blink == 0:
            sleep += 1
            drowsy = 0
            active = 0
        elif left_blink == 1 or right_blink == 1:
            sleep = 0
            drowsy += 1
            active = 0
        else:
            sleep = 0
            drowsy = 0
            active += 1

       # Verificar se a pessoa está sonolenta
        if sleep > 6:  # Se os olhos estiveram fechados por mais de 6 frames
            status = "DORMINDO :( ACORDAAAAA!!!"
            color = (0, 0, 255)
        #elif drowsy > 6:  # Se a pessoa está sonolenta por mais de 6 frames
         #   status = "DORM !"
          #  color = (0, 0, 255)
        elif active > 6:  # Se a pessoa está ativa há mais de 6 frames
            status = "ACORDADO :)"
            color = (0, 255, 0)

        cv2.putText(frame, status, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)

        for n in range(0, 68):
            (x, y) = landmarks[n]
            cv2.circle(face_frame, (x, y), 1, (255, 255, 255), -1)

    cv2.imshow("Frame", frame)
    cv2.imshow("Result of detector", face_frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

# Libera a captura e fecha todas as janelas
cap.release()
cv2.destroyAllWindows()
