import cv2 #importando OpenCV para processmentos básicos de imagem
import numpy as np #para funções 
import dlib #usado para modulos de deep learning e detecção de marcas em rosto

from imutils import face_utils #face_utils para operações basicas de converção


#Iniciando a camera 
cap = cv2.VideoCapture(0)

#iniciando detecção de rosto e marca em rosto
detector = dlib.get_frontal_face_detector() #returns a face detector
predictor = dlib.shape_predictor("C:/Users/Downloads/shape_predictor_68_face_landmarks.dat") #modelo de aprendizado de máquina baseado em conjunto de árvores de regressão

#status que serão reconhecidos
sleep = 0
drowsy = 0
active = 0
status=""
color=(0,0,0)

def compute(ptA,ptB): #que calcula a distância entre dois pontos
	dist = np.linalg.norm(ptA - ptB)
	return dist

def blinked(a,b,c,d,e,f):
	up = compute(b,d) + compute(c,e)
	down = compute(a,f)
	ratio = up/(2.0*down)

	#verificando se está piscando 
	if(ratio>0.25): #considera que está piscando
		return 2
	elif(ratio>0.21 and ratio<=0.25):
		return 1 #coonsidera que há um potencial de piscada
	else:
		return 0 #caso não estiver piscando


while True: #verifica em tempo real 
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #converte para cinza

    faces = detector(gray) #procura qualquer rosto em cinza
    #detected face in faces array
    for face in faces: #extrai informações do rosto que encontro
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()

        face_frame = frame.copy()
        cv2.rectangle(face_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        landmarks = predictor(gray, face) #procurar pontos específicos do rosto
        landmarks = face_utils.shape_to_np(landmarks)

        #The numbers are actually the landmarks which will show eye
        left_blink = blinked(landmarks[36],landmarks[37], 
        	landmarks[38], landmarks[41], landmarks[40], landmarks[39])
        right_blink = blinked(landmarks[42],landmarks[43], 
        	landmarks[44], landmarks[47], landmarks[46], landmarks[45])
        
        #Now judge what to do for the eye blinks
    if(left_blink==0 or right_blink==0):
        sleep+=1
        drowsy=0
        active=0
    if(sleep>6):
        status="DORMINDO !!!"
        color = (255,0,0)

    elif(left_blink==1 or right_blink==1):
        sleep=0
        active=0
        drowsy+=1
    if(drowsy>6):
        status="SONOLENTO !"
        color = (0,0,255)
    else:
        drowsy=0
        sleep=0
        active+=1
    if(active>6):
        status="ACORDADO :)"
        color = (0,255,0)
        	
    cv2.putText(frame, status, (100,100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color,3)

    for n in range(0, 68):
        (x,y) = landmarks[n]
        cv2.circle(face_frame, (x, y), 1, (255, 255, 255), -1)

    cv2.imshow("Frame", frame)
    cv2.imshow("Result of detector", face_frame)
    key = cv2.waitKey(1)
    if key == 27:
      	break