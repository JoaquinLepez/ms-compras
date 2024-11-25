from app.models import Compra
from marshmallow import fields, Schema, post_load

class CompraSchema(Schema):
    id = fields.Integer(dump_only=True)
    producto_id = fields.Integer(required=True)
    fecha_compra = fields.DateTime(dump_only=True)
    direccion_envio = fields.String(required=True, validate=fields.Length(min=1, max=80))

    @post_load
    def make_data(self, data, **kwargs):
        return Compra(**data)
    

