from app.repositories.usuario_repository import UsuarioRepository
from app.models.usuario import Usuario
from werkzeug.security import generate_password_hash, check_password_hash

class UsuarioService:
    def __init__(self):
        self.repo = UsuarioRepository()

    def listar(self):
        return self.repo.obtener_todos()

    def obtener(self, id):
        return self.repo.obtener_por_id(id)

    def registrar(self, datos):
        if not datos.get("nombre") or not datos.get("email") or not datos.get("password"):
            return {"success": False, "errores": ["Todos los campos son obligatorios"]}
        
        hashed_pass = generate_password_hash(datos["password"])
        usuario = Usuario(nombre=datos["nombre"], email=datos["email"], password=hashed_pass)
        user_id = self.repo.crear(usuario)
        return {"success": True, "id": user_id}

    def actualizar(self, id, datos):
        usuario = self.repo.obtener_por_id(id)
        if not usuario:
            return {"success": False, "errores": ["Usuario no encontrado"]}
        
        usuario.nombre = datos.get("nombre", usuario.nombre)
        usuario.email = datos.get("email", usuario.email)
        usuario.rol = datos.get("rol", usuario.rol)

        self.repo.actualizar(usuario)
        return {"success": True}

    def eliminar(self, id):
        return {"success": self.repo.eliminar(id)}

    def login(self, email, password):
        usuario = self.repo.obtener_por_email(email)
        if usuario and check_password_hash(usuario.password, password):
            return {"success": True, "usuario": usuario}
        return {"success": False, "errores": ["Credenciales inválidas"]}
