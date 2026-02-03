from flask import Flask
from database import database
from controllers.chamados_routes import chamados_bp

app = Flask(__name__)
app.register_blueprint(chamados_bp)

if __name__ == '__main__': # Com os __
    database.init_database()
    print("HelpDesk rodando na porta 5000")
    app.run(debug=True)
