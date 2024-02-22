from flask import Flask, Blueprint
from deescovery import discover, ObjectRule
from deescovery.matchers import MatchByPattern, MatchByType

app = Flask(__name__)

api_blueprint = Blueprint("api", __name__, url_prefix="/api")
admin_blueprint = Blueprint("admin", __name__, url_prefix="/admin")


def register_api_blueprint(blueprint: Blueprint):
    api_blueprint.register_blueprint(blueprint)


def register_admin_blueprint(blueprint: Blueprint):
    admin_blueprint.register_blueprint(blueprint)


discover(
    "example",
    [
        ObjectRule(
            name="API blueprint loader",
            module_matches=MatchByPattern(["example.*.api"]),
            object_matches=MatchByType(Blueprint),
            object_action=register_api_blueprint,
        ),
        ObjectRule(
            name="Admin blueprint loader",
            module_matches=MatchByPattern(["example.*.admin"]),
            object_matches=MatchByType(Blueprint),
            object_action=register_admin_blueprint,
        ),
    ]
)

app.register_blueprint(api_blueprint)
app.register_blueprint(admin_blueprint)

# Show the app URL map
print(app.url_map)
