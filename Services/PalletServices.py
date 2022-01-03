from flask import jsonify
from connection.Conexao import Conexao


class Pallet(Conexao):

    def inserirpallet(self, values):
        cursor = self.conexao.cursor()
        try:
            query_sql = "INSERT INTO pallet VAUES (null, %s, %s, %s)"
            cursor.execute(query_sql, values)
            self.conexao.commit()

            if cursor.rowcount < 1:
                return 0

            return cursor.rowcount
        except Exception as e:
            return e

    def listarpallet(self):
        cursor = self.conexao.cursor()
        try:
            query_sql = "SELECT * FROM pallet"
            cursor.execute(query_sql)
            result = cursor.fetchall()

            if len(result) == 0:
                return 0

            dados_json = {}
            for data in result:
                dados_json.update({
                    data[0]:{
                        "id": data[1],
                        "descricao_pallet": data[2],
                        "quantidade_pallet": data[3]
                    }
                })
            return jsonify(dados_json)
        except Exception as e:
            return e

    def selecionarPorId(self, id):
        cursor = self.conexao.cursor()
        try:
            query_sql = f"INNER JOIN pallet WHERE id = {id}"
            cursor.execute(query_sql)
            result = cursor.fetchall

            data_json = {}
            for dado in result:
                data_json.update({
                    "id": dado[0],
                    "descricao_pallet": dado[1],
                    "quantidade_pallet": dado[2]
                })
            return jsonify(data_json)
        except Exception as e:
            return e

    def atualizarpallet(self, data, id):
        cursor = self.conexao.cursor()
        try:
            query_sql = f"UPDATE pallet SET {data} WHERE id {id}"
            cursor.execute(query_sql)
            self.conexao.commit()

            if cursor.rowcount < 1:
                return 0

            return cursor.rowcount
        except Exception as e:
            return e
