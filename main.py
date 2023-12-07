# Need to install ( pip install opencv-python )
import cv2

# Specifying the camera
camera = cv2.VideoCapture(0)

ret, frame = camera.read()
if ret:
    cv2.imwrite("spycame.png", frame)
camera.release()
cv2.destroyAllWindows()
