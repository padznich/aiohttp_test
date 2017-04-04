
import os

from .views import index, questions_handler, choices_handler


static_path = os.path.join(os.path.dirname(__file__), "../static")


def setup_routes(app):

    app.router.add_static('/static/',
                          path=static_path,
                          name='static')

    app.router.add_get('/', index)
    app.router.add_get('/questions', questions_handler)
    app.router.add_get('/choices', choices_handler)
