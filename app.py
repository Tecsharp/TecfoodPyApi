from flask import Flask

from controllers.recipestest import RecipesController
from controllers.welcome_controller import WelcomeController
from controllers.bests_recipes_controller import BestRecipesController
from utils.loki_handler import loki_handler
from controllers.slider_controller import SliderController
from controllers.call_action_controller import CallActionController

app = Flask(__name__)

app.logger.addHandler(loki_handler)
welcome_controller = WelcomeController(app)
bests_recipes_controller = BestRecipesController(app)
slider_controller = SliderController(app)
call_action_controller = CallActionController(app)
recipes_all = RecipesController(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1001)
