import shutter


def main():
    camera_id = 0
    width = 1920
    height = 1080
    fps = 3
    save_dir = "./data"
    cap = shutter.get_capture(camera_id, width=width, height=height, fps=fps)
    shutter.image_shutter(cap, save_dir_root=save_dir)


if __name__ == "__main__":
    main()
