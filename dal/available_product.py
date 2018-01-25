from main import db

class AvailableProduct(db.Model):
    __tablename__ = 'available_products'
    product_id = db.Column(db.String(20), primary_key=True, nullable=False)
    consumer_id = db.Column(db.String(20), primary_key=True, nullable=False)
