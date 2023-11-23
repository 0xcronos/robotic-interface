from ultralytics import YOLO
import time


class RecyclableObjectDetector:
    def __init__(self, path: str):
        self.model = YOLO(path)
        self.is_cardboard = False

    def execute(self, conf: dict):
        results = self.model(**conf)
        
        while True:
            print("Executing loop")
            for result in results:
                probs = result.boxes.conf
                print(f"{self.is_cardboard=} | {probs.nelement()=} | probs.items={probs.item() if probs.nelement() == 1 else ''}")
                if probs.nelement() == 1 and probs.item() >= 0.6:
                    self.is_cardboard = True
                    time.sleep(2)