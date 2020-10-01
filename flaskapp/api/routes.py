from flask import Blueprint, jsonify, request
from flaskapp.api.resources import SalariesAPI, StatsAPI

# Initiating API blueprint
api_bp = Blueprint('api', __name__)

# Intializing API routes function used when intializing the app
def initialise_api_routes(api):
    api.add_resource(SalariesAPI, '/salaries')
    api.add_resource(StatsAPI, '/stats')