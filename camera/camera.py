import cv2

def capture_image(output_path):
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    if ret:
        downscaled = cv2.resize(frame, (320, 240))  # Adjust resolution
        cv2.imwrite(output_path, downscaled)
    camera.release()

if __name__ == "__main__":
    capture_image("/data/image.jpg")

