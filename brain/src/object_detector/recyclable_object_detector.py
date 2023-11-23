from ultralytics import YOLO
import time


class RecyclableObjectDetector:
    def __init__(self, path: str):
        self.model = YOLO(path)
        self.is_carboard = False

    def execute(self, conf: dict):
        results = self.model(**conf)
        while True:
            for result in results:
                probs = result.boxes.conf
                if probs.nelement() == 1 and probs.item() >= 0.6:
                    self.is_cardboard = True
                    print("Prob:", probs.item())
                    time.sleep(5)