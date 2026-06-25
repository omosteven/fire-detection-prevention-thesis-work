from sortout_dataset import SortOutDataset
from train_inference_pipeline import TrainInferencePipeline

class FireClassifier:
    def __init__(self):
        self.folder_name = ''
        # Sortout = SortOutDataset("datasets/detectium_fire", "datasets/home_fire_dataset_yolo_ready", "datasets/smoke_fire_detection_yolo")
        # print(Sortout.get_home_fire_yolo())
        self.Trainer = TrainInferencePipeline()

    def with_yolo(self):
        self.Trainer.train_yolo()

fire = FireClassifier()
fire.with_yolo()