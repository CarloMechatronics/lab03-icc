from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Configuración
    app.config.from_object('app.config.Config')
    
    # Registrar blueprints
    from app.controllers.usuario_controller import usuario_bp
    app.register_blueprint(usuario_bp)
    
    return app