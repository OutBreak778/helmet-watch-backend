import os
import torch

class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_DIR = os.path.dirname(BASE_DIR)

    MODEL_PATH = os.path.join(PROJECT_DIR, 'helmet_rcnn1_model.pth')
    DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    INPUT_FOLDER = os.path.join(PROJECT_DIR, 'static', 'uploads', 'input')
    OUTPUT_FOLDER = os.path.join(PROJECT_DIR, 'static', 'uploads', 'output')
    ALLOWED_EXTENSION = {"png", "jpg", "jpeg"}
