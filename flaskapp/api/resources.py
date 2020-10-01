from flask_restful import Resource
from flask import request
import pandas as pd
import json

salaries_df = pd.read_csv('data/salaries.csv', encoding='utf-8', delimiter=',', header=0, index_col=False, low_memory=False)
stats_df = pd.read_csv('data/stats.csv', encoding='utf-8', delimiter=',', header=0, index_col=False, low_memory=False)
demographics_df = pd.read_csv('data/demographics.csv', encoding='utf-8', delimiter=',', header=0, index_col=False, low_memory=False)

salaries_df_json = json.loads(salaries_df.to_json(orient="records"))
stats_df_json = json.loads(stats_df.to_json(orient="records"))
demographics_df_json = json.loads(demographics_df.to_json(orient="records"))

class WelcomeAPI(Resource):
    global salaries_df_json

    def get(self):
        ret = ({"message": "Welcome! Go to /stats for stats on players, or go to /salaries for player salaries"}, 200)
        return ret[0], ret[1]


class SalariesAPI(Resource):
    global salaries_df_json

    def get(self):
        ret = (salaries_df_json, 200)
        return ret[0], ret[1]

class StatsAPI(Resource):
    global stats_df_json

    def get(self):
        ret = (stats_df_json, 200)
        return ret[0], ret[1]


class DemographicsAPI(Resource):
    global demographics_df_json

    def get(self):
        ret = (demographics_df_json, 200)
        return ret[0], ret[1]


