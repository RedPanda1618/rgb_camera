import cv2
import time
import platform

# check port and display image


def check_camera_connection_display(save_flag=False):
    true_camera_is = []

    for camera_number in range(0, 10):
        if platform.system() == "Linux":
            cap = cv2.VideoCapture(camera_number)
        elif platform.system() == "Windows":
            try:
                cap = cv2.VideoCapture(camera_number, cv2.CAP_DSHOW)
            except TypeError:
                cap = cv2.VideoCapture(camera_number)

        else:
            print("Use Linux or Windows.")
            return

        ret, frame = cap.read()

        if ret is True:
            start = time.time()

            while True:
                elasped_time = time.time() - start
                ret2, frame = cap.read()
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                if elasped_time > 1.0:
                    if save_flag:
                        # save data file
                        save_data_name = f"N_{camera_number}.png"
                        cv2.imwrite(save_data_name, gray)

                    break

                cv2.imshow(f"Camera Number: {camera_number}", gray)

                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break

            cap.release()
            cv2.destroyAllWindows()

            true_camera_is.append(camera_number)
            print("port number", camera_number, "Find!")

        else:
            print("port number", camera_number, "None")

    print(f"Number of connected camera: {len(true_camera_is)}")
    print("Camera ports: " + str(true_camera_is))


if __name__ == "__main__":
    check_camera_connection_display(save_flag=False)
