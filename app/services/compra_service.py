from ..repository import CompraRepository
from app.models import Compra
from app import cache

repository = CompraRepository()

class CompraService:

    def all(self) -> list[Compra]:
        result = cache.get('compras')
        if result is None:
            result = repository.all()
            cache.set('compras', result, timeout=15)
        return repository.all()
    
    def add(self, compra: Compra) -> Compra:
        compra = repository.add(compra)
        cache.set(f'compra_{compra.id}', compra, timeout=15)
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