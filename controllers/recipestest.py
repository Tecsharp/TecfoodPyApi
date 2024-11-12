from flask import Blueprint, jsonify, request
from config.db_config import DBConfig
from services.recipes.recipes_services import update_recipe, get_all_recipes


class RecipesController:
    def __init__(self, app):
        self.logger = app.logger
        self.recipe_bp = Blueprint('recipe', __name__)
        self.recipe_bp.add_url_rule('/api/recipe/all', 'all', self.all, methods=['GET'])
        self.recipe_bp.add_url_rule('/api/recipe/update', 'update', self.update, methods=['POST'])
        app.register_blueprint(self.recipe_bp)
        self.database = DBConfig()

    def all(self):
        return get_all_recipes(self.database, self.logger)

    def update(self):
        return update_recipe(self.database, self.logger)
