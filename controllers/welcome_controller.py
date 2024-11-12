from flask import Blueprint, jsonify
from datetime import datetime

class WelcomeController:
    def __init__(self, app):
        self.logger = app.logger
        # Configura un blueprint para registrar las rutas en Flask
        self.api_bp = Blueprint('api', __name__)
        self.api_bp.add_url_rule('/api/welcome', 'welcome', self.welcome, methods=['GET'])
        app.register_blueprint(self.api_bp)

    def welcome(self):
        welcome_message = 'Hola, acabas de acceder a la API de Tecfood en Python'
        hora_actual = datetime.now().strftime('%H:%M:%S')
        self.logger.info(f'Peticion GET a /api/welcome exitosa: {welcome_message}')
        return jsonify({'message': welcome_message,
                        'current_time': hora_actual})
