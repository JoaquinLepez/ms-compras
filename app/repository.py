from typing import List
from app import db
from app.models import Compra

class CompraRepository:
    def all(self) -> List[Compra]:
        return db.session.query(Compra).all()
    
    def add(self, compra: Compra) -> Compra:
        db.session.add(compra)
        db.session.commit()
        return compra
    
    def delete(self, compra: Compra):
        db.session.delete(compra)
        db.session.commit()
    
    def find(self, id: int) -> Compra:
        return db.session.query(Compra).filter(Compra.id == id).one_or_none()
