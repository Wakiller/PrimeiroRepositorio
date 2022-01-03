from flask import jsonify
from flask_restful import Resource, reqparse
from services.MovimentacaoServices import Movimentacao
from ast import literal_eval


class MovimentacaoUpdatePatchRoute(Resource):

    def patch(self, id: int):
        try:
            parametros = reqparse.RequestParse()
            parametros.add_argument('data_hora_movimento', type=str, required=False)
            parametros.add_argument('tipo_movimento', type=str, required=False)

            args = parametros.parse.args()
            dicion_args = dict(args)
            values = {chave: valor for chave, valor in dicion_args.items() if valor is not None}

            string_dados = ''
            for chave, valor in values.items():
                string_dados += f"{chave} = '{valor}', "

            movimentacao = Movimentacao()
            resultado_update = movimentacao.atualizarmovimentacao(string_dados, id)

            if resultado_update == 0:
                return {
                            "sucesso": False,
                            "mensagem": "Erro ao atualizar os dados."
                }, 400

            return{
                        "sucesso": True,
                        "mensagem": "Atualizado com sucesso!"
            }, 200
        except Exception as e:
            return {
                        "sucesso": False,
                        "mensagem": "Erro de servidor interno."
            }, 500


class MovimentacaoInsertRoute(Resource):

    def post(self):
        try:
            parametros = reqparse.RequestParse()
            parametros.add_argument('data_hora_movimentacao', type=str, required=False)
            parametros.add_argument('tipo_movimentacao', type=str, required=False)

            args = parametros.parse_args()
            dados = (args["data_hora_movimentacao"], args["tipo_movimentacao"])

            movimentacao = Movimentacao()
            resultado_insert = movimentacao.inserirMovimentacao(dados)

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


class MovimentacaoListRoute(Resource):
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
            }

            return jsonify(literal_eval(resultset))
        except Exception as e:
            return {
                        "sucesso": False,
                        "mensagem": "Erro de servidor interno."
            }, 500


class MovimentacaoListByIdRoute(Resource):

    def get(self, id):
        try:
            movimentacao = Movimentacao()
            resultset = movimentacao.selecionarPorId(id)

            if resultset == 0:
                return {
                            "sucesso": False,
                            "mensagem": "Movimentacao não encontrada."
                }, 404
            
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


class MovimentacaoUpdateRoute(Resource):

    def put(self, id):
        try:
            parametros = reqparse.RequestParser()
            parametros.add_argument('data_hora_movimentacao', type=str, required=False)
            parametros.add_argument('tipo_movimentacao', type=str, required=False)

            argumentos = parametros.parse_args()
            valores = f"data_hora_movimentacao = '{argumentos['data_hora_movimentacao']}'," \
                      f"tipo_movimentacao '{argumentos['tipo_movimentacao']}'"

            movimentacao = Movimentacao()
            resultado_update = movimentacao.atualizarMovimentacao(valores, id)

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