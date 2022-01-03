from flask import jsonify
from flask_restful import Resource, reqparse
from services.TecnicoServices import Tecnico
from ast import literal_eval


class TecnicoUpdatePatchRoute(Resource):

    def patch(self, id: int):
        try:
            parametros = reqparse.RequestParse()
            parametros.add_argument('nome_tecnico', type=str, required=False)
            parametros.add_argument('cpf_tecnico', type=srt, required=False)
            parametros.add_argument('matricula_tecnico', type=srt, required=False)

            args = parametros.parse_args()
            dicion_args = dict(args)
            valor = {chave: valor for chave in dicion_args.items() if valor is not None}

            string_dados = ''
            for chave, valor in valor.items():
                string_dados += f"{chave} = '{valor}', "

            tecnico = Tecnico()
            result_update = tecnico.atualizarTecnico(string_dados, id)

            if result_update == 0:
                return {
                            "sucesso": False,
                            "mensagem": "Erro ao atualizar os dados."
                }, 400

            return {
                        "sucesso": True,
                        "mensagem": "Atualizado com sucesso!"
            }, 200
        except Exception as e:
            return {
                        "sucesso": False,
                        "mensagem": "Erro de servidor interno."
            }, 500


class TecnicoInsertRoute(Resource):

    def post(self):
        try:
            parametros = reqparse.RequestParse()
            parametros.add_argument('nome_tecnico', type=str, required=False)
            parametros.add_argument('cpf_tecnico', type=str, required=False)
            parametros.add_argument('matricula_tecnico', type=str, required=False)

            args = parametros.parse_args()
            dados = (args["nome_tecnico"], args["cpf_tecnico"], args["matricula_tecncio"])

            tecnico = Tecnico()
            result_insert = tecnico.InsertTecnico(dados)

            if result_insert == 0:
                return {
                            "sucesso": False,
                            "mensagem": "Erro ao inserir dados."
                }, 400

            return {
                        "sucesso": True,
                        "mensagem": "Dados inseridos com sucesso!"
            }, 201

        except Exception as e:
            return {
                        "sucesso": False,
                        "mensagem": "Erro de servidor interno."
            }, 500


class TecnicoListRoute(Resource):

    def get(self):
        try:
            tecnico = Tecnico()
            resultset = tecnico.ListarTecnico()

            if resultset == 0:
                return {
                            "sucesso": False,
                            "mensagem": "Nenhum dado a ser exibido"
                }, 400
            
            return {
                        "sucesso": True,
                        "mensagem": "Atualizado com sucesso!"
            }

            return jsonify(literal_eval(resultset))
        except Exception as e:
            return {
                        "sucesso": False,
                        "mensagem": "Erro de servidor interno"
            }, 500


class TecncoListByIdRoute(Resource):

    def get(self, id):
        try:
            tecnico = Tecnico()
            resultset = tecnico.selecionarPorId(id)

            if resultset == 0:
                return {
                            "sucesso": False,
                            "mensagem": "Tecnico não encontrado."
                }, 404
            
            return {
                        "sucesso": True,
                        "mensgem": "Atualizado com sucesso!"
            }, 200

            return jsonify(literal_eval(resultset))
        except Exception as e:
            return  {
                        "sucesso": False,
                        "mensagem": "Erro de servidor interno."
            }, 500


class TecnicoUpdateRoute(Resource):

    def put(self, id):
        try:
            parametros = reqparse.RequestParser()
            parametros.add_argument('nome_tecnico', type=str, required=False)
            parametros.add_argument('cpf_tecnico', type=str, required=False)
            parametros.add_argument('matricula_tecnico', type=str, required=False)

            argumentos = parametros.parse_args()
            valores = f"nome_tecnico = '{argumentos['nome_tecnico']}', cpf_tecnico = '{argumentos['cpf_tecnico']}'," \
                      f"matricula_tecnico = {argumentos['matricula_tecnico']}"

            tecnico = Tecnico()
            result_update = tecnico.atualizarTecnico(valores, id)

            if result_update == 0:
                return {
                            "sucesso": False,
                            "mensagem": "Erro ao atualizar os dados."
                }, 400

            return {
                        "sucesso": True,
                        "mensagem": "Atualizado com sucesso!"
            }, 200
        except Exception as e:
            return {
                        "sucesso": False,
                        "mensagem": "Erro no servidor interno."
            }, 500