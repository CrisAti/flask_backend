from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User2FA(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    two_factor_enabled = db.Column(db.Boolean, default=False, nullable=False)
    two_factor_secret = db.Column(db.String(32), nullable=True)

    def __repr__(self):
        return f'<User2FA {self.user_id} 2FA: {self.two_factor_enabled}>'
