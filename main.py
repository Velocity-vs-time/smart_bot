import subprocess
import time
from robot_control.motor_control import move_robot, cleanup

try:
    while True:
        print("Capturing image...")
        subprocess.run(["python3", "camera/camera.py"])

        print("Processing image with DeepStack...")
        command = subprocess.check_output(["python3", "deepstack/deepstack_process.py"]).decode("utf-8").strip()
        print(f"Command received: {command}")

        print("Executing command...")
        move_robot(command.upper())

        time.sleep(5)
except KeyboardInterrupt:
    cleanup()

