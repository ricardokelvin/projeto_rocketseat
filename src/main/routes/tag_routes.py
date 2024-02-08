from flask import Blueprint, request, jsonify
from src.views.http_types.http_request import HttpRequest
from src.views.tag_creator_view import TagCreatorView
from src.errors.error_handler import handle_errors


tags_routes_bp = Blueprint('tags_routes', __name__)

@tags_routes_bp.route('/create_tag', methods=["POST"])
def creat_tags():
    response = None
    try:
        tag_creator_view = TagCreatorView()

        http_request = HttpRequest(body=request.json)
        tag_creator_view.validate_and_create(http_request)
        response = tag_creator_view.validate_and_create(http_request)
    except Exception as exception:
        response = handle_errors(exception)

    return jsonify(response.body), response.status_code
