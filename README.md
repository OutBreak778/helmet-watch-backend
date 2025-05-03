Helmet Detection System - Backend
Overview
This is the backend for the Helmet Detection project. It processes image data sent from the frontend, runs object detection using a trained model, and returns results to the frontend.

Installation
Clone the repository:

git clone https://github.com/OutBreak778/helmet-detection-backend.git
cd helmet-detection-backend
Set up the virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
Install dependencies:

pip install -r requirements.txt
Running the Server
To start the backend server:

python app.py  # or flask run if using Flask CLI
Example Response
{ "results": { "boxes": [[100, 150, 200, 250]], "labels": ["helmet", "motorcycle"], "scores": [0.95, 0.88], "result_image": "/static/uploads/output/image.jpg" } }
