import uuid
import os
from flask import request, jsonify
from werkzeug.utils import secure_filename
from config.config import Config
from config.services import PredictImage
from utils.allow import allowedFile

def PredictHelmet():
    if 'image' not in request.files:
        return jsonify({'message': 'Proper Image is required'}),400
    
    file = request.files['image']

    if file and allowedFile(file.filename):

        imageId = str(uuid.uuid4())
        originalFileName = secure_filename(file.filename)
        
        rename = originalFileName.rsplit('.',1)[1].lower()

        fileName = f"{imageId}.{rename}"
        savePath = os.path.join(Config.INPUT_FOLDER, fileName)
        os.makedirs(Config.INPUT_FOLDER, exist_ok=True)
        
        file.save(savePath)

        results = PredictImage(savePath, fileName)
        # os.remove(savePath)

        return jsonify({"results": results}), 200
    return jsonify({'message': "Invalid file type"}), 400

def getPredictHelmet():
    try:
        # Full path to output image folder
        output_dir = Config.OUTPUT_FOLDER

        # List all image files in the output directory
        images = [
            f"/static/uploads/output/{f}"
            for f in os.listdir(output_dir)
            if f.rsplit('.', 1)[-1].lower() in Config.ALLOWED_EXTENSION
        ]

        # Return image URLs to frontend
        return jsonify({
            "message": "Output images fetched successfully",
            "images": images
        }), 200

    except Exception as e:
        return jsonify({"message": f"Error fetching images: {str(e)}"}), 500