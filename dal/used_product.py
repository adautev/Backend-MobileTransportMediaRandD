from main import db

class UsedProduct(db.Model):
    __tablename__ = 'used_products'
    product_id = db.Column(db.String(20), primary_key=True, nullable=False)
    comsumer_id = db.Column(db.String(20), primary_key=True, nullable=False)
