import cv2

camera = cv2.VideoCapture(4)

fps = int(camera.get(cv2.CAP_PROP_FPS))
w = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
video = cv2.VideoWriter('video.mp4', fourcc, fps, (w, h))

while True:
    ret, frame = camera.read()
    cv2.imshow('camera', frame)
    video.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
