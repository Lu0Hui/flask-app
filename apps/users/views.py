from flask import Blueprint
from flask import jsonify
from flask_restful import Api, Resource

from apps.users.models import User

user = Blueprint('user', __name__)
api = Api(user)


class UserAPI(Resource):

    def get(self, user_id=None):
        if user_id is None:
            return jsonify(
                request="GET /users/",
                message="Give a list of all users"
            )
        else:
            return jsonify(
                request="GET /users/<user_id>",
                message="Show a single user: {}".format(user_id)
            )

    def post(self):
        user = User(username='wang2gou')
        user.save()
        return jsonify(
            request="POST /users/",
            message="Create a new user",
            username=user.username
        )

    def put(self, user_id):
        return jsonify(
            request="PUT /users/<user_id>",
            message="Update a single user: {}".format(user_id)
        )

    def delete(self, user_id):
        return jsonify(
            request="DELETE /users/<user_id>",
            message="Delete a single user: {}".format(user_id)
        )


api.add_resource(UserAPI, '/', '/<user_id>')
