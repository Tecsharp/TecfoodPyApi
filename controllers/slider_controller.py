from flask import Blueprint, jsonify

class SliderController:
    def __init__(self, app):
        self.logger = app.logger
        self.slides_bp = Blueprint('slides', __name__)
        self.slides_bp.add_url_rule('/api/slides/index', 'slides', self.slides, methods=['GET'])
        app.register_blueprint(self.slides_bp)

    def slides(self):
        slides = [{"id": 1, "name": "Ricas hamburguesas", "description": "Description 1", "url": "#","image": "Image 1"},
                  {"id": 2, "name": "Barbacoa de borrego", "description": "Description 2", "url": "#", "image": "Image 2"},
                  {"id": 3, "name": "Queso Oaxaca picante", "description": "Description 3", "url": "#", "image": "Image 3"}]
        self.logger.info(f"Envío de slides en INDEX: {slides}")
        return jsonify(slides), 200
