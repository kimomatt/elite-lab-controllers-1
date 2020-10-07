import sys
from app import app
from flask import abort, request, Response

from .models import SandwichManager, MessageManager


@app.route('/')
def index():
    """
    DEMO CODE
    """
    # Flask will autoformat this into an HTML response
    return "Hello World"


@app.route('/sandwiches/<int:sandwich_id>', methods=['GET'])
def get_sandwich(sandwich_id):
    """
    DEMO CODE
    """
    sandwich = SandwichManager.get_sandwich_by_id(sandwich_id)
    if not sandwich:
        abort(404)

    # Flask will autoformat this into JSON response if you return a python dict
    return sandwich.to_dict()


@app.route('/sandwiches/', methods=['GET'])
def get_all_sandwiches():
    """
    DEMO CODE
    """
    response = []
    for sandwich in SandwichManager.get_all_sandwiches():
        response.append(sandwich.to_dict())

    # Flask will autoformat this into JSON response if you return a python dict
    return {"sandwiches": response}


@app.route('/sandwiches/', methods=['POST'])
def create_sandwich():
    """
    DEMO CODE
    """
    body = request.json
    sandwich = SandwichManager.create_sandwich(body)

    # Flask will autoformat this into JSON response if you return a python dict
    return {"id": sandwich.id}


@app.route('/sandwiches/<int:sandwich_id>', methods=['DELETE'])
def delete_sandwich(sandwich_id):
    """
    DEMO CODE
    """
    result = SandwichManager.delete_sandwich(sandwich_id)
    if result:
        return Response(status=200)
    else:
        abort(500)


######################
#   Your Code Below  #
######################
