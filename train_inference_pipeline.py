from ultralytics import YOLO

model = YOLO("yolo11n.pt")
class TrainInferencePipeline:
    def __init__(self):
        d = 2

    def train_yolo(self):
        model.train(
            data="dataset.yaml",
            epochs=20,
            imgsz=320,
            workers=4
        )

        preds = model.val(
            data="dataset.yaml",
        )
        print('preds:',preds)
