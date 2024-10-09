from app import db
class Compra(db.Model):
    __tablename__ = 'compras'
    # Atributos propios
    id: int = db.Column(db.Integer, primary_key = True, autoincrement = True)
    producto_id: str = db.Column(db.Integer, nullable = False)
    fecha_compra = db.Column(db.DateTime, nullable = False)
    direccion_envio: str = db.Column(db.String(80), nullable = False)

