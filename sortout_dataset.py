import os
import re
import pandas as pd
from collections import Counter

class SortOutDataset:
    def __init__(self, detectium_folder, home_fire_dataset_yolo_ready, smoke_fire_detection_yolo):
        self.detectium = self.get_folder_path(detectium_folder)
        self.home_fire_yolo = self.get_folder_path(home_fire_dataset_yolo_ready)
        self.smoke_fire_yolo = self.get_folder_path(smoke_fire_detection_yolo)

    def get_folder_path(self, folder_path):
        return [os.path.join(folder_path, folder) for folder in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, folder))]

    def get_detectium(self):
        # detectium_fire
        # - preference_dataset
        # - - img1
        # - - - preference_dataset/img1/0005---.png
        # - - img2
        # - - img3
        # - real_images
        # - - real_fire
        # - - - images
        # - - - - real_/images/real_fire/0.039---.png
        # - - - labels
        # - - - - real_fire/labels/0_000.txt
        # - - real_none_fire
        # - - - real_non_fire/0.png
        # - synthetic_images
        # - real_video
        self.d

    def get_home_fire_yolo(self):
        # annotation classes:'fire/smoke'
        return self.get_yolo_files(self.home_fire_yolo, ['fire', 'smoke'])

    def get_smoke_fire_yolo(self):
        return self.get_yolo_files(self.smoke_fire_yolo, ['smoke', 'fire'])

    def get_yolo_files(self, yolo_dataset_folder, classes):
        test, train, val = [], [], []
        for folder in yolo_dataset_folder:
            full_path = f'{folder}/images'
            category = folder[38::]
            files = []
            for file in os.listdir(full_path):
                file_label = {"file": f'{full_path}/{file}', "yolo_label": f'{full_path}/{file.split(".")[0]}.txt', "category": category, "classes": classes}
                files.append(file_label)
            if category == "train":
                train = files
            elif category == "test":
                test = files
            elif category == "val":
                val = files

        return train, test, val

