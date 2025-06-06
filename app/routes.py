import os
import json
from flask import request, jsonify
import requests

from . import app

DATA_FILE = os.path.join(os.path.dirname(__file__), 'data.json')


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {
        "drug_crime_rate": "N/A",
        "drug_abuse_deaths": "N/A",
        "updates": []
    }


def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)


@app.route('/api/data', methods=['GET'])
def get_data():
    data = load_data()
    return jsonify(data)


@app.route('/api/data', methods=['POST'])
def update_data():
    data = load_data()
    new_update = request.json.get('update')
    if new_update:
        data['updates'].append(new_update)
        save_data(data)
    return jsonify(data)


@app.route('/api/news')
def get_news():
    api_key = os.environ.get('NEWS_API_KEY')
    if not api_key:
        return jsonify({"error": "NEWS_API_KEY not set"}), 400
    resp = requests.get(
        'https://newsapi.org/v2/top-headlines',
        params={'category': 'health', 'apiKey': api_key, 'q': 'drug'},
        timeout=10
    )
    if resp.ok:
        return jsonify(resp.json())
    return jsonify({"error": "failed to fetch news"}), 500
