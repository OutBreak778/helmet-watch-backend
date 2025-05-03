from flask import Blueprint
from controllers.homeController import home, hello
from controllers.imageController import PredictHelmet, getPredictHelmet


router = Blueprint('home', __name__)

router.route('/', methods=['GET'])(home)
router.route('/hello', methods=['GET'])(hello)

router.route('/image', methods=['POST'])(PredictHelmet)
router.route('/image', methods=['GET'])(getPredictHelmet)