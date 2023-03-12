import cv2
import datetime
import platform
import os


def get_capture(camera_id):

    if (platform.system() == "Linux"):
        cap = cv2.VideoCapture(camera_id)
    elif (platform.system() == "Windows"):
        cap = cv2.VideoCapture(camera_id, cv2.CAP_DSHOW)
    else:
        print("Use Linux or Windows.")
        return None
    return cap


def image_shutter(capture, save_dir="./", camera_name=""):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    cap = capture
    cnt = 1
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Couldn't read any frame from capture.")
            return
        cv2.imshow("Camera " + camera_name, frame)
        key = cv2.waitKey(1)
        if key == ord("s"):
            now = datetime.datetime.now()
            now = str(now).replace(" ", "_")
            img_path = os.path.join(save_dir, now + ".png")

            print("Saved " + str(cnt) + " img:" + img_path)
            cv2.imwrite(img_path, frame)
            cnt += 1
        elif key == ord("q"):
            return
