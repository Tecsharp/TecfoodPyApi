from bson.objectid import ObjectId
from flask import jsonify, request

def update_recipe(database, logger):
    try:
        collection = database.get_collection('recetas')
        data = request.get_json()

        # Validar que el ID está presente
        if '_id' not in data:
            return jsonify({"error": "ID de la receta es requerido"}), 400

        recipe_id = ObjectId(data['_id'])
        result = collection.update_one(
            {'_id': recipe_id},
            {
                '$set': {
                    'nombre': data.get('nombre'),
                    'ingredientes': data.get('ingredientes'),
                    'tiempoPreparacion': data.get('tiempoPreparacion'),
                    'categoria': data.get('categoria'),
                    'porciones': data.get('porciones')
                }
            }
        )

        if result.matched_count == 0:
            return jsonify({"error": "Receta no encontrada"}), 404

        logger.info("Receta actualizada con éxito")
        return jsonify({"message": "Receta actualizada con éxito"}), 200

    except Exception as err:
        logger.error(f"Error al actualizar la receta: {err}")
        return jsonify({"error": "Error al actualizar la receta"}), 500


def get_all_recipes(database, logger):
    try:
        collection = database.get_collection('recetas')
        recipes = list(collection.find())

        for recipe in recipes:
            recipe['_id'] = str(recipe['_id'])
        logger.info("Consulta de todas las recetas realizada con éxito")
        return jsonify(recipes), 200

    except Exception as err:
        logger.error(f"Error al consultar las recetas: {err}")
        return jsonify({"error": "Error al consultar las recetas"}), 500
