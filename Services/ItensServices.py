from flask import jsonify
from connection.Conexao import Conexao


class itens(Conexao):

    def inseriritens(self, values):
        cursor = self.conexao.cursor()
        try:
            query_sql = "INSERT INTO itens VALUE (null , %s, %s)"
            cursor.execute(query_sql, values)
            self.conexao.commit()

            if cursor.rowcount < 0:
                return 0

            return cursor.rowcount
        except Exception as e:
            return e

    # Pendente de elaboração de query com JOINS das tabelas Movimentação e Pallets
    def listaritens(self):
        cursor = self.conexao.cursor()
        try:
            query_sql = "SELECT * FROM itens"
            cursor.execute(query_sql)
            result = cursor.fetchall()

            if len(result) == 0:
                return 0

            dados_json = {}
            for dado in result:
                dados_json.updade({
                    dado[0]: {
                        "id": dado[1],
                        "quantidade_itens": dado[2]
                    }
                })
            return jsonify(dados_json)
        except Exception as e:
            return e

    # Pendente de elaboração de query com JOINS das tabelas Movimentação e Pallets
    def listaritensPorId(self, id):
        cursor = self.conexao.cursor()
        try:
            query_sql = f"INNER JOIN itens WHERE id = {id}"
            cursor.execute(query_sql)
            cursor.fetchall()

            if len(result) == 0:
                return 0

            dados_json = {}
            for dado in result:
                dados_json.update({
                    "id": dado[0],
                    "quantidade_itens": dado[1]
                })
            return jsonify(dados_json)
        except Exception as e:
            return e

    def atualizaritens(self, dados, id):
        cursor = self.conexao.cursor()
        try:
            query_sql = f"UPDATE itens SET {dados} WHERE id = {id}"
            cursor.execute(query_sql)
            self.conexao.commit()

            if cursor.rowcount < 1:
                return 0

            return cursor.rowcount
        except Exception as e:
            return e
