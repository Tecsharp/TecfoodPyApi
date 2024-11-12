from flask import Blueprint, jsonify

class CallActionController:
    def __init__(self, app):
        self.logger = app.logger
        self.call_action_bp = Blueprint('call_action', __name__)
        self.call_action_bp.add_url_rule('/api/callaction/index', 'call_action', self.call_action_index, methods=['GET'])
        app.register_blueprint(self.call_action_bp)

    def call_action_index(self):
        call_action = {"title": "Recetas libre de gluten", "description": "Recetas totalmente hechas con amor para la familia. Nutrelos con alimentos libres de gluten.", "button_text": "Ver todas las recetas", "button_url": "#","image": "#"}
        self.logger.info(f"Envío de call action en INDEX: {call_action}")
        return jsonify(call_action), 200
