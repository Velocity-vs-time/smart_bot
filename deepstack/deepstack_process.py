import requests
import json

def process_image(image_path):
    url = "http://localhost:80/v1/vision/detection"  # Local DeepStack endpoint
    with open(image_path, "rb") as image_file:
        response = requests.post(
            url,
            files={"image": image_file},
            data={"min_confidence": 0.5}  # Minimum confidence for object detection
        )
    response_json = response.json()
    if response_json.get("success"):
        predictions = response_json.get("predictions", [])
        if predictions:
            # Example: Take the first detected object and infer a command
            detected_object = predictions[0]["label"]
            print(f"Detected object: {detected_object}")
            if detected_object == "person":
                return "FORWARD"
            elif detected_object == "obstacle":
                return "STOP"
            else:
                return "LEFT"
    return "STOP"  # Default command if nothing is detected

if __name__ == "__main__":
    command = process_image("/data/image.jpg")
    print(command)

