from main import db

class AvailableProducts(db.Model):
    __tablename__ = 'available_products'
    product_id = db.Column(db.String(20), primary_key=True)
    comsumer_id = db.Column(db.String(20), primary_key=True)
