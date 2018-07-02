from flask import Blueprint
from flask.views import MethodView

core = Blueprint('core', __name__)


class IndexAPI(MethodView):

    def get(self):
        return "core"


core.add_url_rule('/', view_func=IndexAPI.as_view('core'))
