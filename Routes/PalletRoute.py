from flask import jsonify
from flask_restful import Resource, reqparse
from Services.PalletServices import Pallet
from ast import literal_eval


class PalletInsertRoute(Resource):

    def post(self):
        try:
            parametros = reqparse.RequestParse()
            parametros.add_argument('descricao_pallet', type=str, required=True,
                                    help="Informe uma descrição ao Pallet")
            argumentos = parametros.parse_args()
            dados = (argumentos["descricao_pallet"])

            pallet = Pallet()
            result_insert = pallet.insertPallet(dados)

            if result_insert == 0:
                return {
                            "sucesso": False,
                            "mensagem": "Erro ao inserir dados"
                }, 400

            return {
                        "sucesso": True,
                        "mensagem": "Dados inseridos com sucesso!"
            }, 201

        except Exception as e:
            return {
                        "sucesso": False,
                        "mensagem": "Erro de servidor interno. Contate o admin para mais detalhes",
            }, 500


class PalletListRoute(Resource):

    def get(self):
        try:
            pallet = Pallet()
            resultset = pallet.listarpallet()

            if resultset == 0:
                return {
                            "sucesso": False,
                            "mensagem": "Nenhum dado a ser exibido"
                }, 400
            
            return {
                        "sucesso": True,
                        "mensagem": "Dados inseridos com sucesso!"
            }, 200

            return jsonify(literal_eval(resultset))
        except Exception as e:
            return {
                        "sucesso": False,
                        "mensagem": "Erro de servidor interno, contate o admin para mais informações."
            }, 500


class PalletUpdateRoute(Resource):

    def put(self, id):
        try:
            parametros = reqparse.RequestParse()
            parametros.add_argument('descricao_pallet', type=str, required=True, help="Informe uma descrição para o Pallet")
            argument = parametros.parse_args()
            values = f"descricao_pallet = '{argument['descricao_pallet']}'"

            pallet = Pallet()
            result_update = pallet.atualizarPallet(values, id)

            if result_update == 0:
                return {
                            "sucesso": False,
                            "mensagem": "Erro ao atualizar os dados."
                }, 400

            return {
                        "sucesso": True,
                        "mensagem": "Dados inseridos com sucesso!"
            }, 200
        except Exception as e:
            return {
                        "sucesso": False,
                        "mensagem": "Erro de servidor interno."
            }, 500