from flask import jsonify
from flask_restful import Resource, reqparse
from itens.ItensServices import Itens
from ast import literal_eval


class ItensUpdatePatchRoute(Resource):

    def pach(self, id: int):
        try:
            parametros = reqparse()
            parametros = add_argument('quantidade-itens', type=str, required=False)

            args = parametros.parse.args()
            dicion_args = dict(args)
            values = {chave: valor for chave, valor in dicion_args.items() if valor is not None}

            string_dados = ''
            for chave, valor in values.items():
                string_dados += f"{chave} = '{valor}', "

            itens = Itens()
            resultado_update = itens.atualizaritens(string_dados, id)

            if resultado_update == 0:
                return {
                            "sucesso": False,
                            "mensagem": "Erro ao atualizar dados."
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


class ItensInsertRoute(Resource):

    def post(self):
        try:
            parametros = reqparse.RequestParse()
            parametros.add_argument('quantidade_itens', type=str, required=False)

            args = parametros.parse_args()
            dados = (args["quantidade_itens"])

            itens = Itens()
            resultado_insert = itens.inserirItens(dados)

            if resultado_insert == 0:
                return {
                            "sucesso": False,
                            "mensagem": "Erro ao inserir dados."
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


class ItensListRoute(Resource):

    def get(self):
        try:
            movimentacao = Movimentacao()
            resultset = movimentacao.listarMovimentacao()

            if resultset == 0:
                return {
                           "sucesso": False,
                           "mensagem": "Nenhum dado exibido."
                }, 400
            
            return {
                        "sucesso": True,
                        "mensagem": "Dados inseridos com sucesso!"
            }, 200

            return jsonify(literal_eval(resultset))
        except Exception as e:
            return {
                       "sucesso": False,
                       "mensagem": "Erro de servidor interno."
            }, 500


class ItensListByIdRoute(Resource):

    def get(self, id):
        try:
            itens = Itens()
            resultset = itens.selecionarPorId(id)

            if resultset == 0:
                return {
                            "sucesso": False,
                            "mensagem": "Item não encontrada."
                }, 404
                
            return {
                        "sucesso": True,
                        "mensagem": "Dados inseridos com sucesso!"
            }

                return jsonify(literal_eval(resultset))
            except Exception as e:
                return {
                           "sucesso": False,
                           "mensagem": "Erro de servidor interno."
                }, 500


class ItensUpdateRoute(Resource):

    def put(self, id):
        try:
            parametros = reqparse.RequestParser()
            parametros.add_argument('quantidade_itens', type=str, required=False)

            argumentos = parametros.parse_args()
            valores = f"quantidade_itens = '{argumentos['quantidade_itens']}',"

            itens = Itens()
            resultado_update = itens.atualizarItens(valores, id)

            if resultado_update == 0:
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