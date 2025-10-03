from app.repositories.usuario_repository import UsuarioRepository
from app.models.usuario import Usuario

class UsuarioService:
    def __init__(self):
        self.repo = UsuarioRepository()

    def listar(self):
        return self.repo.obtener_todos()

    def obtener(self, id):
        return self.repo.obtener_por_id(id)

    def registrar(self, datos):
        # Validaciones básicas
        errores = []
        nombre = (datos.get("nombre") or "").strip()
        email = (datos.get("email") or "").strip()
        password = (datos.get("password") or "").strip()
        rol = (datos.get("rol") or "admin").strip()

        if not nombre:
            errores.append("El nombre es obligatorio")
        if not email:
            errores.append("El email es obligatorio")
        if not password:
            errores.append("La contraseña es obligatoria")
        if rol not in ("admin", "usuario"):
            errores.append("El rol debe ser 'admin' o 'usuario'")

        if errores:
            return {"success": False, "errores": errores}

        usuario = Usuario(
            nombre=nombre,
            email=email,
            password=password,  # ⚠️ texto plano (solo para pruebas)
            rol=rol
        )
        user_id = self.repo.crear(usuario)
        return {"success": True, "id": user_id}

    def actualizar(self, id, datos):
        usuario = self.repo.obtener_por_id(id)
        if not usuario:
            return {"success": False, "errores": ["Usuario no encontrado"]}

        nombre = datos.get("nombre", usuario.nombre)
        email = datos.get("email", usuario.email)
        rol = datos.get("rol", usuario.rol)

        # Normaliza
        usuario.nombre = (nombre or "").strip()
        usuario.email = (email or "").strip()
        usuario.rol = (rol or "admin").strip()

        # No actualizamos contraseña aquí (solo en un endpoint específico si lo agregas)
        self.repo.actualizar(usuario)
        return {"success": True}

    def eliminar(self, id):
        return {"success": self.repo.eliminar(id)}

    def login(self, email, password):
        email = (email or "").strip()
        password = (password or "").strip()

        usuario = self.repo.obtener_por_email(email)
        if not usuario:
            return {"success": False, "errores": ["Credenciales inválidas"]}

        # Comparación en texto plano (solo para pruebas)
        if usuario.password == password:
            return {"success": True, "usuario": usuario}

        return {"success": False, "errores": ["Credenciales inválidas"]}
