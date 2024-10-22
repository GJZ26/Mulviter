import cv2

cap = None

def read_image(path: str):
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise Exception(f"The image {path} could not be read")

    return image


def relative_resize(image, width, height):
    image_height, image_width = image.shape
    aspect_ratio = image_width / image_height
    new_width = width
    new_height = int(new_width / aspect_ratio)

    if new_height > height:
        new_height = height
        new_width = int(new_height * aspect_ratio)
    return cv2.resize(image, (new_width, new_height))


def check_camera():
    global cap
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("No camera available")
        quit()


def check_video(path: str):
    global cap
    cap = cv2.VideoCapture(path)
    if not cap.isOpened():
        print("There is no capturing device available")
        quit()


def get_frame():
    global cap
    if cap is None:
        print("Capturer not initialized")
        quit()
    ret, frame = cap.read()
    if not ret:
        print("The camera frame could not be captured.")
        quit()
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


def get_video_fps(video_path: str):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise Exception(f"Could not open video {video_path}")

    fps = cap.get(cv2.CAP_PROP_FPS)
    cap.release()

    return fps
