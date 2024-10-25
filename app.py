from flask import Flask
import pymongo
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

app.secret_key="sdsadasd233242"

app.config['UPLOAD_FOLDER']='./static/imagenes'

miConexion = pymongo.MongoClient("mongodb://localhost:27017")

baseDatos = miConexion['Tienda2']

productos = baseDatos['Productos1']

usuarios = baseDatos['Usuarios']

if __name__=="__main__":
    from controlador.productoController import *
    from controlador.usuarioController import * 
    app.run(port=8000,debug=True)
    
    
