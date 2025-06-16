from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, User
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username'], password=data['password']).first()

    if not user:
        return jsonify({'message': 'Invalid username or password'}), 401

    return jsonify({
        'message': 'Login successful',
        'user': {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'rol': user.rol  # ✅ Incluido en la respuesta
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
