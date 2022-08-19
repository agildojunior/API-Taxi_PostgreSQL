from flask_cors import CORS
from config import app
from auth import token_required
from controllers import corridasController, empresasController, taxisController, enderecosController, usuariosController
cors = CORS(app)

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
#                                   Empresas
# --------------------------------------------------------------------------

#Pegar dados
@app.route("/empresas",methods=["GET"])
@token_required
def get_empresas(current_empresa):
  return empresasController.get_all(current_empresa)

#Pegar dados por ID
@app.route("/empresas/<int:id>" , methods=["GET"])
@token_required
def get_empresas_by_id(current_empresa,id):
  return empresasController.get_by_id(current_empresa,id)

#Adicionar dados
@app.route("/empresas", methods=["POST"])
@token_required
def insert_empresas(current_empresa):
  return empresasController.insert(current_empresa)

#Editar dados
@app.route("/empresas/<int:id>" , methods=["PUT"])
@token_required
def update_empresas(current_empresa,id):
  return empresasController.update(current_empresa,id)

#Metodo Delete
@app.route("/empresas/<int:id>", methods=["DELETE"])
@token_required
def delete_empresas(current_empresa,id):
  return empresasController.delete(current_empresa,id)

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
#                                   Corridas
# --------------------------------------------------------------------------

#Pegar dados
@app.route("/corridas",methods=["GET"])
@token_required
def get_corridas(current_empresa):
  return corridasController.get_all(current_empresa)

#Pegar dados por ID'
@app.route("/corridas/<int:id>" , methods=["GET"])
@token_required
def get_corridas_by_id(current_empresa,id):
  return corridasController.get_by_id(current_empresa,id)

#Adicionar dados'
@app.route("/corridas", methods=["POST"])
@token_required
def insert_corridas(current_empresa):
  return corridasController.insert(current_empresa)

#Editar dados'
@app.route("/corridas/<int:id>" , methods=["PUT"])
@token_required
def update_corridas(current_empresa,id):
  return corridasController.update(current_empresa,id)

#Metodo Delete
@app.route("/corridas/<int:id>", methods=["DELETE"])
@token_required
def delete_corridas(current_empresa,id):
  return corridasController.delete(current_empresa,id)

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
#                                   Taxis
# --------------------------------------------------------------------------

#Pegar dados
@app.route("/taxis",methods=["GET"])
@token_required
def get_taxis(current_empresa):
  return taxisController.get_all(current_empresa)

#Pegar dados por ID
@app.route("/taxis/<int:id>" , methods=["GET"])
@token_required
def get_taxis_by_id(current_empresa,id):
  return taxisController.get_by_id(current_empresa,id)

#Adicionar dados
@app.route("/taxis", methods=["POST"])
@token_required
def insert_taxis(current_empresa):
  return taxisController.insert(current_empresa)

#Editar dados
@app.route("/taxis/<int:id>" , methods=["PUT"])
@token_required
def update_taxis(current_empresa,id):
  return taxisController.update(current_empresa,id)

#Metodo Delete
@app.route("/taxis/<int:id>", methods=["DELETE"])
@token_required
def delete_taxis(current_empresa,id):
  return taxisController.delete(current_empresa,id)

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
#                                   Usuarios
# --------------------------------------------------------------------------

#Pegar dados
@app.route("/usuarios",methods=["GET"])
@token_required
def get_usuarios(current_empresa):
  return usuariosController.get_all(current_empresa)

#Pegar dados por ID
@app.route("/usuarios/<int:id>" , methods=["GET"])
@token_required
def get_usuarios_by_id(current_empresa,id):
  return usuariosController.get_by_id(current_empresa,id)

#Adicionar dados
@app.route("/usuarios", methods=["POST"])
@token_required
def insert_usuarios(current_empresa):
  return usuariosController.insert(current_empresa)

#Editar dados
@app.route("/usuarios/<int:id>" , methods=["PUT"])
@token_required
def update_usuarios(current_empresa,id):
  return usuariosController.update(current_empresa,id)

#Pegar dados por Email
@app.route("/usuarios/email/<email>" , methods=["GET"])
@token_required
def get_usuarios_by_email(current_empresa,email):
  return usuariosController.get_by_email(current_empresa,email)

#Metodo Delete
@app.route("/usuarios/<int:id>", methods=["DELETE"])
@token_required
def delete_usuarios(current_empresa,id):
  return usuariosController.delete(current_empresa,id)

# -------------------------------------------------------------------------

if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0", port=8090)
