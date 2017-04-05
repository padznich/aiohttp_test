
import os

from .views import Home, Question, Choice


static_path = os.path.join(os.path.dirname(__file__), "../static")


def setup_routes(app):

    app.router.add_static("/static/",
                          path=static_path,
                          name="static")

    app.router.add_route("GET", "/", Home, name="home")
    app.router.add_route("*", "/questions", Question, name="questions")
    app.router.add_route("*", "/choices", Choice, name="choices")
