import mysql
from flask import Blueprint, jsonify
from config.db_config import Database
from mysql.connector import Error

class BestRecipesController:
    def __init__(self, app):
        self.logger = app.logger
        self.bests_bp = Blueprint('bests', __name__)
        self.bests_bp.add_url_rule('/api/recipe/bests', 'bests', self.bests, methods=['GET'])
        app.register_blueprint(self.bests_bp)
        self.database = Database()

    def bests(self):
        try:
            connection = self.database.get_connection()
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM recipes WHERE rating BETWEEN 4 AND 5 LIMIT 6;"
            cursor.execute(query)
            recipes = cursor.fetchall()
            cursor.close()
            connection.close()
            self.logger.info("Consulta de las mejores recetas realizada con éxito" + str(recipes))
            return jsonify(recipes), 200

        except mysql.connector.Error as err:
            self.logger.error(f"Error en la conexión a la base de datos: {err}")
            return jsonify({"error": "Error en la conexión a la base de datos"}), 500
    
