from config.config import Config

def allowedFile(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSION

def addFilename(item1, item2):
    return item1 + item2