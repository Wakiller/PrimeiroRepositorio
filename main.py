from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from Routes.ClienteRoute import *
from Routes.ItensRoute import *
from Routes.MovimentacaoRoute import *
from Routes.PalletRoute import *
from Routes.TecnicoRoute import *

app = Flask(__name__)
api = Api(app)
cors = CORS(app)

api.add_resource(ClienteInsertRoute, "/clientes")
api.add_resource(ClienteListByIdRoute, "/clientes/<int:id>")
api.add_resource(ClienteListRoute, "/clientes/<int:id>")
api.add_resource(ClienteUpdateRoute, "/clientes/<int:id>")
api.add_resource(ClienteUpdatePatchRoute, "/clientes/<int:id>")

api.add_resource(TecnicoUpdatePatchRoute, "/tecnico")
api.add_resource(TecnicoInsertRoute, "/tecnico")
api.add_resource(TecnicoListRoute, "/tecnico/<int:id>")
api.add_resource(TecncoListByIdRoute, "/tecnico/<int:id>")
api.add_resource(TecnicoUpdateRoute, "/tecnico/<int:id>")

api.add_resource(MovimentacaoUpdatePatchRoute, "/tecnico/<int:id>")
api.add_resource(MovimentacaoInsertRoute, "/tecnico")
api.add_resource(MovimentacaoListRoute, "/tecnico/<int:id>")
api.add_resource(MovimentacaoListByIdRoute, "/tecnico/<int:id>")
api.add_resource(MovimentacaoUpdateRoute, "/tecnico/<int:id>")

api.add_resource(ItensUpdatePatchRoute, "/tecnico/<int:id>")
api.add_resource(ItensInsertRoute, "/tecnico")
api.add_resource(ItensListRoute, "/tecnico/<int:id>")
api.add_resource(ItensListByIdRoute, "/tecnico/<int:id>")
api.add_resource(ItensUpdateRoute, "/tecnico/<int:id>")

api.add_resource(PalletListRoute, "/pallet/<int:id>")
api.add_resource(PalletUpdateRoute, "/pallet/<int:id>")
api.add_resource(PalletInsertRoute, "/pallet")

if __name__ == "__main__":
    app.run(port=3000, debug=True)