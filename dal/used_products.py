from main import db

class UsedProducts(db.Model):
    __tablename__ = 'used_products'
    product_id = db.Column(db.String(20), primary_key=True)
    comsumer_id = db.Column(db.String(20), primary_key=True)
