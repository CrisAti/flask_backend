from flask import Flask, request, jsonify, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import db, User2FA
from config import Config
import pyotp
import qrcode
import io

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
db.init_app(app)

@app.route('/2fa/status/<int:user_id>', methods=['GET'])
def get_2fa_status(user_id):
    user_2fa = User2FA.query.filter_by(user_id=user_id).first()
    if user_2fa and user_2fa.two_factor_enabled:
        return jsonify({'user_id': user_id, 'two_factor_enabled': True}), 200
    return jsonify({'user_id': user_id, 'two_factor_enabled': False}), 200

@app.route('/2fa/generate_qr/<int:user_id>', methods=['POST'])
def generate_qr(user_id):
    user_2fa = User2FA.query.filter_by(user_id=user_id).first()
    if user_2fa and user_2fa.two_factor_enabled:
        return jsonify({'error': '2FA already enabled'}), 400
    if not user_2fa:
        user_2fa = User2FA(user_id=user_id)
        db.session.add(user_2fa)
    secret = pyotp.random_base32()
    user_2fa.two_factor_secret = secret
    db.session.commit()
    otp_uri = pyotp.totp.TOTP(secret).provisioning_uri(name=f'user{user_id}', issuer_name='MyApp')
    img = qrcode.make(otp_uri)
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)
    return send_file(buf, mimetype='image/png')

@app.route('/2fa/verify', methods=['POST'])
def verify_2fa():
    data = request.json
    user_id = data.get('user_id')
    code = data.get('code')
    user_2fa = User2FA.query.filter_by(user_id=user_id).first()
    if not user_2fa or not user_2fa.two_factor_secret:
        return jsonify({'error': '2FA not initialized for this user'}), 400
    totp = pyotp.TOTP(user_2fa.two_factor_secret)
    if totp.verify(code):
        user_2fa.two_factor_enabled = True
        db.session.commit()
        return jsonify({'success': True, 'message': '2FA verified and enabled'})
    return jsonify({'success': False, 'message': 'Invalid code'}), 400

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5003)
