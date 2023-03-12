import shutter


def main():
    cap = shutter.get_capture(4)
    shutter.image_shutter(cap, save_dir="imgs", camera_name="test")


if __name__ == "__main__":
    main()
