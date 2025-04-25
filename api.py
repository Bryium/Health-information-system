# api.py

from flask import Blueprint, request, jsonify
from models import db, Client

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/search-client', methods=['GET'])
def api_search_client():
    client_name = request.args.get('client_name', '')

    if not client_name:
        return jsonify({'error': 'Client name is required'}), 400

    client = Client.query.filter(Client.client_name.ilike(f'%{client_name}%')).first()

    if not client:
        return jsonify({'message': 'Client not found'}), 404

    return jsonify({
        'id': client.id,
        'name': client.client_name,
        'age': client.age,
        'gender': client.gender,
        'programs': [
            {
                'id': program.id,
                'name': program.name,
                'description': program.description
            } for program in client.programs
        ]
    }), 200
