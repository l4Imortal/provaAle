from flasgger import Swagger

def init_swagger(app):
    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": 'apispec',
                "route": '/apispec.json',
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/swagger/"
    }
    
    template = {
        "swagger": "2.0",
        "info": {
            "title": "Sistema de Gerenciamento Escolar API",
            "description": "API para gerenciar usuários, alunos, turmas e pagamentos",
            "version": "1.0.0"
        },
        "host": "localhost:5000",
        "basePath": "/",
        "schemes": ["http"],
        "securityDefinitions": {
            "Bearer": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": "JWT Authorization header using the Bearer scheme. Example: 'Bearer {token}'"
            }
        }
    }
    
    swagger = Swagger(app, config=swagger_config, template=template)
    return swagger
