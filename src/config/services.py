from models.helmetModel import load_model
from PIL import Image, ImageDraw, ImageFont
import torchvision.transforms as T
import torch
import os
from config.config import Config

CLASS_LABELS = ['motorcycle', 'withHelmet', 'withoutHelmet', 'licensePlate']

model = load_model(num_classes=len(CLASS_LABELS) + 1)
transform = T.ToTensor()


def PredictImage(imgPath, fileName):
    image = Image.open(imgPath).convert("RGB")
    imgTensor = transform(image).to(Config.DEVICE)
 
    with torch.no_grad():
        prediction = model([imgTensor])[0]

    boxes = prediction['boxes'].cpu().numpy()
    labels = prediction['labels'].cpu().numpy()
    scores = prediction['scores'].cpu().numpy()

    draw = ImageDraw.Draw(image)
    try:
        font = ImageFont.truetype("arial.ttf", 20)  # System font
    except:
        font = ImageFont.load_default()  # Fallback if no font file available

    for box, score, label_id in zip(boxes, scores, labels):
        if score > 0.7 and label_id > 0:
            x1, y1, x2, y2 = box
            label = CLASS_LABELS[label_id - 1]

            # Text label
            label_text = f"{label} {score:.2f}"

            # Draw bounding box
            draw.rectangle([x1, y1, x2, y2], outline="yellow", width=3)

            # Fixed height background behind text (20 px height buffer)
            draw.rectangle(
                [x1, y1 - 25, x1 + 180, y1],
                fill="black"
            )

            # Draw label text (white on black for contrast)
            draw.text((x1 + 5, y1 - 22), label_text, fill="white", font=font)

    result_path = os.path.join(Config.OUTPUT_FOLDER, fileName)
    image.save(result_path)

    return {
        "boxes": boxes.tolist(),
        "scores": scores.tolist(),
        "labels": [
            {"label": CLASS_LABELS[label_id - 1], "score": round(float(score), 4)}
            for label_id, score in zip(labels, scores)
            if score > 0.5 and label_id > 0
        ],
        "result_image": f"/static/uploads/output/{fileName}",
        "result_input": f"/static/uploads/input/{fileName}"
    }