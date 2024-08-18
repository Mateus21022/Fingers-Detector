import cv2
import mediapipe as mp


mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Erro ao capturar vídeo.")
        break


    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
   
    results = hands.process(rgb_frame)

    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            if hand_landmarks.landmark[4].y<0.8:
                print ("Dedo polegar")
            if hand_landmarks.landmark [12].y<0.5:
                print ("Dedo médio")
            if hand_landmarks.landmark [16].y<0.5:
                print ("Dedo anelar")
            if hand_landmarks.landmark[20].y<0.5:
                print ("Dedo mindinho")
            if hand_landmarks.landmark[8].y < 0.5:
                print("Dedo indicador acima")


    cv2.imshow('Hand Tracking', frame)

   
    if cv2.waitKey(1) & 0xFF == ord('c'):
        break


cap.release()
cv2.destroyAllWindows()