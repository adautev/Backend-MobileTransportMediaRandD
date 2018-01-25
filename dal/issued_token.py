from main import db


class IssuedToken(db.Model):
    __tablename__ = 'issued_tokens'
    product_id = db.Column(db.String(20), primary_key=True, nullable=False)
    consumer_id = db.Column(db.String(20), primary_key=True, nullable=False)
    valid_from = db.Column(db.DateTime(timezone=False), nullable=False)
    valid_to = db.Column(db.DateTime(timezone=False), nullable=False)
