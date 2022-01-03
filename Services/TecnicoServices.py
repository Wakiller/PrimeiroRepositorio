from flask import jsonify
from connection.Conexao import Conexao


class Tecnico(Conexao):

    def inserirTecnico(self, values):
        cursor = self.conexao.cursor()
        try:
            query_sql = "INSERT INTO tecnico VALUES (null, %s, %s, %s, %s)"
            cursor.execute(query_sql, values)
            self.conexao.commit()

            if cursor.rowcount < 1:
                return 0

            return cursor.rowcount
        except Exception as e:
            return e

    def listarTecnico(self):
        cursor = self.conexao.cursor()
        try:
            query_sql = "SELECT * FROM tecnico"
            cursor.execute(query_sql)
            result = cursor.fetchall()

            if len(result) == 0:
                return 0

            dados_json = {}
            for dado in result:
                dados_json.update({
                    dado[0]: {
                        "nome_tecnico": dado[1],
                        "cpf_tecnico": dado[2],
                        "matricula_tecnico": dado[3]
                    }
                })
            return cursor.rowcount
        except Exception as e:
            return e

    def listarTecnicoPorId(self, id):
        cursor = self.conexao.cursor()
        try:
            query_sql = f"SELECT * FROM tecnico WHERE id = {id}"
            cursor.execute(query_sql)
            result = cursor.fetchall()

            if len(result) == 0:
                return 0

            dados_json = {}
            for dado in result:
                dados_json.update({
                    "id": dado[0],
                    "nome_tecnico": dado[1],
                    "cpf_tecnico": dado[2],
                    "matricula_tecnico": dado[3]
                })
            return jsonify(dados_json)
        except Exception as e:
            return e

    def atualizarTecnico(self, dados, id):
        cursor = self.conexao.cursor()
        try:
            query_sql = f"UPDATE tecnico SET {dados} WHERE id = {id}"
            cursor.execute(query_sql)
            self.conexao.commit()

            if cursor.rowcount < 1:
                return 0

            return cursor.rowcount
        except Exception as e:
            return e

    def deletarTecnico(self, id):
        cursor = self.conexao.cursor()
        try:
            query_sql = f"DELETE tecncio WHERE id = {id}"
            cursor.execute(query_sql)
            self.conexao.commit()

            if cursor.rowcount < 1:
                return 0

            return cursor.rowcount
        except Exception as e:
            return e