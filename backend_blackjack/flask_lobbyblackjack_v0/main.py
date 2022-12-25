from flask import Flask, request, jsonify

app = Flask(__name__)

lobbies = {}

@app.route('/create', methods=['POST'])
def create_lobby():
    data = request.get_json()
    lobby_id = data['lobby_id']
    lobby_name = data['lobby_name']

    if lobby_id in lobbies:
        return jsonify({'error': 'Lobby with this ID already exists'}), 400

    lobbies[lobby_id] = {'name': lobby_name, 'users': []}
    return jsonify({'success': 'Lobby created successfully'}), 201

@app.route('/join', methods=['POST'])
def join_lobby():
    data = request.get_json()
    lobby_id = data['lobby_id']
    user = data['user']

    if lobby_id not in lobbies:
        return jsonify({'error': 'Lobby with this ID does not exist'}), 404

    lobby = lobbies[lobby_id]
    lobby['users'].append(user)
    return jsonify({'success': 'User added to lobby successfully'}), 200

@app.route('/leave', methods=['POST'])
def leave_lobby():
    data = request.get_json()
    lobby_id = data['lobby_id']
    user = data['user']

    if lobby_id not in lobbies:
        return jsonify({'error': 'Lobby with this ID does not exist'}), 404

    lobby = lobbies[lobby_id]
    lobby['users'].remove(user)
    return jsonify({'success': 'User removed from lobby successfully'}), 200

@app.route('/list', methods=['GET'])
def list_lobbies():
    return jsonify({'lobbies': lobbies}), 200

if __name__ == '__main__':
    app.run()
