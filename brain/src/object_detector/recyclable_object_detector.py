from ultralytics import YOLO


class RecyclableObjectDetector:
    def __init__(self, config: dict):
        print(config)
        self.model = YOLO(config['weights_path'])

        del config['weights_path']
        self.config = config

        self.is_cardboard = False

    def execute(self):
        results = self.model(**self.config)
        
        while True:
            for result in results:
                probs = result.boxes.conf
                if probs.nelement() == 1 and probs.item() >= 0.6:
                    self.is_cardboard = True
                    print(f"Cardboard detected: {self.is_cardboard} | accuracy: {probs.item()}")
