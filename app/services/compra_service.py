from datetime import datetime
from ..repository import CompraRepository
from app.models import Compra

repository = CompraRepository()

class CompraService:

    def all(self) -> list[Compra]:
        return repository.all()
    
    def add(self, compra: Compra) -> Compra:
        compra.fecha_compra = datetime.now()
        compra = repository.add(compra)
        return compra
    
    def delete(self, id: int) -> bool:
        compra = self.find(id)
        if compra:
            repository.delete(compra)
            return True
        else:
            return False
    
    def find(self, id: int) -> Compra:
        return repository.find(id)