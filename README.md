# lab03-icc
Desarrollo de aplicación Flask


# Steps for creating a Flask project (with CMD)

1. Create and enter to a new project
    mkdir lab03-icc
    cd lab03-icc

2. Create virtual enviroment
    py -m venv env

3. Activate virtual enviroment
    env\Scripts\activate

4. Create necessary directories and files
    mkdir app
    mkdir app\model
    mkdir app\repository
    mkdir app\service
    mkdir app\controller
    mkdir template
    mkdir template\usuario
    mkdir static\css

    echo run.py
    echo requirements.txt
    echo env> .gitignore

5. Install the project requirements
    py -m pip install -r requirements.txt

6. Execute the application
    py run.py


# Estructura de carpetas

LAB03-ICC/
│
├── app/
│   ├── controllers/
│   │   └── usuario_controller.py
│   │
│   ├── models/
│   │   └── usuario.py
│   │
│   ├── repositories/
│   │   └── usuario_repository.py
│   │
│   ├── services/
│   │   └── usuario_service.py
│   │
│   ├── __init__.py
│
├── static/
│   └── css/
│       └── style.css
│
├── templates/
│   ├── base.html
│   ├── login.html                  # Login de acceso
│   ├── admin_panel.html            # Panel de administración (CRUD completo)
│   │
│   └── usuario/                    # Vistas CRUD
│       ├── crear.html
│       ├── editar.html
│       ├── index.html              # Vista pública (sin login)
│       └── ver.html
│
├── config.py
├── database.sql
├── .env
├── .gitignore
├── requirements.txt
├── run.py
└── README.md
