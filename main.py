import shutter


def main():
    camera_id = 8
    width = 1920
    height = 1080
    fps = 6
    save_dir = "./data"
    cap = shutter.get_capture(camera_id, width=width, height=height, fps=fps)
    shutter.image_shutter(cap, save_dir=save_dir)


if __name__ == "__main__":
    main()
