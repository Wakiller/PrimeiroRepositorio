from flask import jsonify
from flask_restful import Resource, reqparse
from services.ClienteServices import Cliente
from ast import literal_eval


class ClienteUpdatePatchRoute(Resource):
    
    def patch(self, id: int):
        try:
            parametros = reqparse.RequestParse()
            parametros.add_argument('nome_cliente', type=str, required=False)
            parametros.add_argument('cpf_cliente', type=srt, required=False)
            parametros.add_argument('rg_cliente', type=srt, required=False)

            args = parametros.parse_args()
            dicion_args = dict(args)
            valor = {chave: valor for chave in dicion_args.items() if valor is not None}

            string_dados = ''
            for chave, valor in valor.items():
                string_dados += f"{chave} = '{valor}', "

            cliente = Cliente()
            result_update = cliente.atualizarCliente(string_dados, id)
            
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
        

class ClienteInsertRoute(Resource):

    def post(self):
        try:
            parametros = reqparse.RequestParse()
            parametros.add_argument('nome_cliente', type=str, required=False)
            parametros.add_argument('cpf_cliente', type=str, required=False)
            parametros.add_argument('rg_cliente', type=str, required=False)

            args = parametros.parse_args()
            dados = (args["nome_cliente"], args["cpf_cliente"], args["rg_cliente"])

            cliente = Cliente()
            result_insert = cliente.InsertCliente(dados)

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

        
class ClienteListRoute(Resource):

    def get(self):
        try:
            cliente = Cliente()
            resultset = cliente.ListarCliente()

            if resultset == 0:
                return {
                            "sucesso": False,
                            "mensagem": "Nenhum dado a ser exibido."
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
        
        
class ClienteListByIdRoute(Resource):

    def get(self, id):
        try:
            cliente = Cliente()
            resultset = cliente.selecionarPorId(id)

            if resultset == 0:
                return {
                            "sucesso": False,
                            "mensagem": "Tecnico não encontrado."
                }, 404
            
            return {
                        "sucesso": True,
                        "mensagem": "Dados inseridos com sucesso!"
            }, 200

            return jsonify(literal_eval(resultset))
        except Exception as e:
            return  {
                        "sucesso": False,
                        "mensagem": "Erro de servidor interno."
            }, 500


class ClienteUpdateRoute(Resource):

    def put(self, id):
        try:
            parametros = reqparse.RequestParser()
            parametros.add_argument('nome_cliente', type=str, required=False)
            parametros.add_argument('cpf_cliente', type=str, required=False)
            parametros.add_argument('rg_cliente', type=str, required=False)

            argumentos = parametros.parse_args()
            valores = f"nome_cliente = '{argumentos['nome_cliente']}', cpf_cliente = '{argumentos['cpf_cliente']}'," \
                      f"rg_cliente = {argumentos['rg_cliente']}"

            cliente = Cliente()
            result_update = cliente.atualizarCliente(valores, id)

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
                        "mensagem": "Atualizado com sucesso!"
            }, 500