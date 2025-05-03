import torch
import torchvision
from config.config import Config
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor

def load_model(num_classes):
    model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
    inFeatures = model.roi_heads.box_predictor.cls_score.in_features
    model.roi_heads.box_predictor = FastRCNNPredictor(inFeatures, num_classes)
    model.load_state_dict(torch.load(Config.MODEL_PATH, map_location=Config.DEVICE))
    model.to(Config.DEVICE)

    model.eval()
    return model


