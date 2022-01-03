from flask import jsonify
from connection.Conexao import Conexao


class Movimentacao(Conexao):

    def inserirMovimentacao(self, values):
        cursor = self.conexao.cursor()
        try:
            query_sql = "INSERT INTO movimentacao VALUES (null, %s, %s, %s)"
            cursor.execute(query_sql, values)
            self.conexao.commit()

            if cursor.rowcount < 1:
                return 0

            return cursor.rowcount
        except:
            return 0

    def listarMovimentacao(self):
        cursor = self.conexao.cursor()
        try:
            query_sql = "SELECT * FROM movimentacao"
            cursor.execute(query_sql)
            result = cursor.fetchall()

            if len(result) == 0:
                return 0

            dados_json = {}
            for dado in result:
                dados_json.update({
                    dado[0]: {
                        "data_hora_movimento": dado[1],
                        "tipo_movimento": dado[2]
                    }
                })
            return jsonify(dados_json)
        except:
            return 0

    def listarMovimentacaoPorId(self, id):
        cursor = self.conexao.cursor()
        try:
            query_sql = f"SELECT * FROM movimentacao WHERE id = {id}"
            cursor.execute(query_sql)
            result = cursor.fetchall()

            if len(result) == 0:
                return 0

            dados_json = {}
            for dado in result:
                dados_json.update({
                    "id": dado[0],
                    "data_hora_movimento": dado[1],
                    "tipo_movimento": dado[2]
                })
            return jsonify(dados_json)
        except:
            return 0

    def atualizarMovimentacao(self, dados, id):
        cursor = self.conexao.cursor()
        try:
            query_sql = f"UPDATE movimentacao SET {dados} WHERE id = {id}"
            cursor.execute(query_sql)
            self.conexao.commit()

            if cursor.rowcount < 1:
                return 0

            return cursor.rowcount
        except:
            return 0