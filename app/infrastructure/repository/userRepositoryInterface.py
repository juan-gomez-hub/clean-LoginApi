from abc import ABC, abstractmethod
from app.entities.user import User

class UserRepositoryInterface(ABC):
    @abstractmethod
    def save(self, user: User) -> User:
        """Guarda un usuario en la base de datos y retorna el usuario guardado."""
        pass

    @abstractmethod
    def findByUsername(self, username: str) -> str | None:
        """Busca un usuario por username y retorna el username si existe, sino None."""
        pass

    @abstractmethod
    def getPassword(self, username: str) -> str | None:
        """Obtiene el hash de la contraseña del usuario."""
        pass

    @abstractmethod
    def killToken(self, token: str) -> None:
        """Agrega un token a la blacklist (revocación de token)."""
        pass