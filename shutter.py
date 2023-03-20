import cv2
import datetime
import platform
import os


def get_capture(camera_id, width=640, height=480, fps=15):

    if (platform.system() == "Linux"):
        cap = cv2.VideoCapture(camera_id)
    elif (platform.system() == "Windows"):
        cap = cv2.VideoCapture(camera_id, cv2.CAP_DSHOW)
    else:
        print("Use Linux or Windows.")
        return None

    cap.set(cv2.CAP_PROP_FPS, fps)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1.0)
    return cap


def image_shutter(capture, save_dir=".", camera_name="", auto=True):
    now = datetime.datetime.now()
    now = str(now).replace(" ", "_")
    save_dir = os.path.join(save_dir, now)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    cap = capture
    cnt = 1
    save = False
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Couldn't read any frame from capture.")
            return
        cv2.imshow("Camera " + camera_name, frame)
        key = cv2.waitKey(1)
        if key == 32 and save is False:
            save = True
        elif key == 32 and save is True:
            save = False
        elif key == ord("q"):
            return

        if auto and save:
            save_bmp(frame, save_dir, cnt)
            cnt += 1
            if key == ord("q"):
                return
            continue

        elif key == ord("s"):
            save_bmp(frame, save_dir, cnt)
            cnt += 1


def save_bmp(frame, save_dir, cnt):
    now = datetime.datetime.now()
    now = str(now).replace(" ", "_")
    img_path = os.path.join(save_dir, now + ".bmp")

    print("Saved " + str(cnt) + " img:" + img_path)
    cv2.imwrite(img_path, frame)
