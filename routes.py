from flask_cors import CORS
from config import app
from controllers import corridasController, empresasController, taxisController, enderecosController, usuariosController
cors = CORS(app)

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
#                                   Empresas
# --------------------------------------------------------------------------

#Pegar dados
@app.route("/empresas",methods=["GET"])
def get_empresas():
  return empresasController.get_all()

#Pegar dados por ID
@app.route("/empresas/<int:id>" , methods=["GET"])
def get_empresas_by_id(id):
  return empresasController.get_by_id(id)

#Adicionar dados
@app.route("/empresas", methods=["POST"])
def insert_empresas():
  return empresasController.insert()

#Editar dados
@app.route("/empresas/<int:id>" , methods=["PUT"])
def update_empresas(id):
  return empresasController.update(id)

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
#                                   Corridas
# --------------------------------------------------------------------------

#Pegar dados
@app.route("/corridas",methods=["GET"])
def get_corridas():
  return corridasController.get_all()

#Pegar dados por ID'
@app.route("/corridas/<int:id>" , methods=["GET"])
def get_corridas_by_id(id):
  return corridasController.get_by_id(id)

#Adicionar dados'
@app.route("/corridas", methods=["POST"])
def insert_corridas():
  return corridasController.insert()

#Editar dados'
@app.route("/corridas/<int:id>" , methods=["PUT"])
def update_corridas(id):
  return corridasController.update(id)

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
#                                   Taxis
# --------------------------------------------------------------------------

#Pegar dados
@app.route("/taxis",methods=["GET"])
def get_taxis():
  return taxisController.get_all()

#Pegar dados por ID
@app.route("/taxis/<int:id>" , methods=["GET"])
def get_taxis_by_id(id):
  return taxisController.get_by_id(id)

#Adicionar dados
@app.route("/taxis", methods=["POST"])
def insert_taxis():
  return taxisController.insert()

#Editar dados
@app.route("/taxis/<int:id>" , methods=["PUT"])
def update_taxis(id):
  return taxisController.update(id)

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
#                                   Usuarios
# --------------------------------------------------------------------------

#Pegar dados
@app.route("/usuarios",methods=["GET"])
def get_usuarios():
  return usuariosController.get_all()

#Pegar dados por ID
@app.route("/usuarios/<int:id>" , methods=["GET"])
def get_usuarios_by_id(id):
  return usuariosController.get_by_id(id)

#Adicionar dados
@app.route("/usuarios", methods=["POST"])
def insert_usuarios():
  return usuariosController.insert()

#Editar dados
@app.route("/usuarios/<int:id>" , methods=["PUT"])
def update_usuarios(id):
  return usuariosController.update(id)

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
#                                   Enderecos
# --------------------------------------------------------------------------

#Pegar dados
@app.route("/enderecos",methods=["GET"])
def get_enderecos():
  return enderecosController.get_all()

#Pegar dados por ID
@app.route("/enderecos/<int:id>" , methods=["GET"])
def get_enderecos_by_id(id):
  return enderecosController.get_by_id(id)

#Adicionar dados
@app.route("/enderecos", methods=["POST"])
def insert_enderecos():
  return enderecosController.insert()

#Editar dados
@app.route("/enderecos/<int:id>" , methods=["PUT"])
def update_enderecos(id):
  return enderecosController.update(id)

# -------------------------------------------------------------------------

if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0", port=8090)
