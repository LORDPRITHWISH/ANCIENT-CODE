import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


base_options = python.BaseOptions(model_asset_path='models\\hand_landmarker.task')
options = vision.HandLandmarkerOptions(base_options=base_options,
                                       num_hands=2)
detector = vision.HandLandmarker.create_from_options(options)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 840)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 490)
mp_drawing = mp.solutions.drawing_utils

while True:

    ret, frame=cap.read()
    if not ret :
        break
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
    # landmarker.detect_async(mp_image, time.thread_time_ns)
    detection_result = detector.detect(mp_image)
    print('\n'*2)
    print(f'{detection_result}')
    print('\n'*10)
    print(f'{detection_result.hand_landmarks}')

    frame.flags.writeable = True

    mp_drawing.draw_landmarks(
	frame,
	detection_result.hand_landmarks,
	vision.HandLandmarksConnections,
	mp_drawing.DrawingSpec(
		color=(0,255,255),
		thickness=2,
		circle_radius=1)
	)
    cv2.imshow("footage", frame)
    key=cv2.waitKey(1)
    if key== ord("q") :
        break

cv2.destroyAllWindows()