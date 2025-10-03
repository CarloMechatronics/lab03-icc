from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.services.usuario_service import UsuarioService

usuario_bp = Blueprint("usuarios", __name__)
usuario_service = UsuarioService()

# ---- LOGIN ----
@usuario_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        resultado = usuario_service.login(email, password)

        if resultado["success"]:
            session["usuario_id"] = resultado["usuario"].id
            flash("Login exitoso", "success")
            return redirect(url_for("usuarios.admin_panel"))
        else:
            flash("Credenciales inválidas", "error")
    return render_template("login.html")

@usuario_bp.route("/logout")
def logout():
    session.clear()
    flash("Sesión cerrada", "success")
    return redirect(url_for("usuarios.index"))

# ---- CRUD ----
@usuario_bp.route("/usuarios")
def index():
    usuarios = usuario_service.listar()
    return render_template("usuario/list.html", usuarios=usuarios)

@usuario_bp.route("/usuarios/admin")
def admin_panel():
    if "usuario_id" not in session:
        flash("Debes iniciar sesión", "error")
        return redirect(url_for("usuarios.login"))
    usuarios = usuario_service.listar()
    return render_template("usuario/admin_panel.html", usuarios=usuarios)

@usuario_bp.route("/usuarios/crear", methods=["GET","POST"])
def crear():
    if "usuario_id" not in session:
        flash("Acceso restringido", "error")
        return redirect(url_for("usuarios.login"))

    if request.method == "POST":
        datos = request.form.to_dict()
        resultado = usuario_service.registrar(datos)
        if resultado["success"]:
            flash("Usuario creado", "success")
            return redirect(url_for("usuarios.admin_panel"))
        else:
            for e in resultado["errores"]:
                flash(e, "error")
    return render_template("usuario/create.html")

@usuario_bp.route("/usuarios/editar/<int:id>", methods=["GET","POST"])
def editar(id):
    if "usuario_id" not in session:
        flash("Acceso restringido", "error")
        return redirect(url_for("usuarios.login"))

    usuario = usuario_service.obtener(id)
    if not usuario:
        flash("Usuario no encontrado", "error")
        return redirect(url_for("usuarios.admin_panel"))

    if request.method == "POST":
        datos = request.form.to_dict()
        resultado = usuario_service.actualizar(id, datos)
        if resultado["success"]:
            flash("Usuario actualizado", "success")
            return redirect(url_for("usuarios.admin_panel"))
    return render_template("usuario/edit.html", usuario=usuario)

@usuario_bp.route("/usuarios/eliminar/<int:id>", methods=["POST"])
def eliminar(id):
    if "usuario_id" not in session:
        flash("Acceso restringido", "error")
        return redirect(url_for("usuarios.login"))

    usuario_service.eliminar(id)
    flash("Usuario eliminado", "success")
    return redirect(url_for("usuarios.admin_panel"))
