from envyaml import EnvYAML
from object_detector.recyclable_object_detector import RecyclableObjectDetector

config = EnvYAML('config.yaml')	
object_detector = RecyclableObjectDetector(config['object_detector'])
print("Object detector created successfully...")

object_detector.execute()
