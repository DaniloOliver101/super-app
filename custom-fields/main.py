# main.py
import requests
from time import sleep  
from flask import Flask
from clientes import clientes
from campos import campos

app = Flask(__name__)
app.register_blueprint(clientes)
app.register_blueprint(campos)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)  # Iniciar o servidor
