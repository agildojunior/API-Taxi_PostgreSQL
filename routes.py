from config import create_app
from flask_cors import CORS
from controllers import taxisController, empresasController, corridasController

app = create_app()
cors = CORS(app)

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
#                                   Empresas
# --------------------------------------------------------------------------

'Pegar dados'
@app.route("/empresas",methods=["GET"])
def get_empresas():
  return empresasController.get_all()

'Pegar dados por ID'
@app.route("/empresas/<int:id>" , methods=["GET"])
def get_empresas_by_id(id):
  return empresasController.get_by_id(id)

'Adicionar dados'
@app.route("/empresas", methods=["POST"])
def insert_empresas():
  return empresasController.insert()

'Editar dados'
@app.route("/empresas/<int:id>" , methods=["PUT"])
def update_empresas(id):
  return empresasController.update(id)

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
#                                   Corridas
# --------------------------------------------------------------------------

'Pegar dados'
@app.route("/corridas",methods=["GET"])
def get_corridas():
  return corridasController.get_all()

'Pegar dados por ID'
@app.route("/corridas/<int:id>" , methods=["GET"])
def get_corridas_by_id(id):
  return corridasController.get_by_id(id)

'Adicionar dados'
@app.route("/corridas", methods=["POST"])
def insert_corridas():
  return corridasController.insert()

'Editar dados'
@app.route("/corridas/<int:id>" , methods=["PUT"])
def update_corridas(id):
  return corridasController.update(id)

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
#                                   Taxis
# --------------------------------------------------------------------------

'Pegar dados'
@app.route("/taxis",methods=["GET"])
def get_taxis():
  return taxisController.get_all()

'Pegar dados por ID'
@app.route("/taxis/<int:id>" , methods=["GET"])
def get_taxis_by_id(id):
  return taxisController.get_by_id(id)

'Adicionar dados'
@app.route("/taxis", methods=["POST"])
def insert_taxis():
  return taxisController.insert()

'Editar dados'
@app.route("/taxis/<int:id>" , methods=["PUT"])
def update_taxis(id):
  return taxisController.update(id)

# -------------------------------------------------------------------------

if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0", port=8090)
