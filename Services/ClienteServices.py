from flask import jsonify
from connection.Conexao import Conexao


class Cliente(Conexao):

    def inserirCliente(self, values):
        cursor = self.conexao.cursor()
        try:
            query_sql = "INSERT INTO Cliente VALUES (null, %s, %s, %s, %s)"
            cursor.execute(query_sql, values)
            self.conexao.commit()

            if cursor.rowcount < 1:
                return 0

            return cursor.rowcount
        except Exception as e:
            return e

    def listarCliente(self):
        cursor = self.conexao.cursor()
        try:
            query_sql = "SELECT * FROM Cliente"
            cursor.execute(query_sql)
            result = cursor.fetchall()

            if len(result) == 0:
                return 0

            dados_json = {}
            for data in result:
                dados_json.update({
                    data[0]: {
                        "nome_cliente": data[1],
                        "cpf_cliente": data[2],
                        "rg_cliente": data[3]
                    }
                })
            return jsonify(query_json)
        except Exception as e:
            return e

    def selecionarPorId(self, id):
        cursor = self.conexao.cursor()
        try:
            query_sql = f"SELECT * FROM Cliente WHERE id = {id}"
            cursor.execute(query_sql)
            result = cursor.fetchall()

            data_json ={}
            for dado in result:
                data_json.update({
                    "id": dado[0],
                    "nome_cliente": dado[1],
                    "cpf_cliente": dado[2],
                    "rg_cliente": dado[3]
                })
            return jsonify(data_json)
        except Exception as e:
            return e

    def atualizarCliente(self,data, id):
        cursor = self.conexao.cursor()
        try:
            query_sql = f"UPDATE Cliente SET {data} WHERE id = {id}"
            cursor.execute(query_sql)
            self.conexao.commit()

            if cursor.rowcount < 1:
                return 0

            return cursor.rowcount
        except Exception as e:
            return e

    def deleteCliente(self, id):
        cursor = self.conexao.cursor()
        try:
            query_sql = f"DELETE FROM Cliente WHERE id = {id}"
            cursor.execute(query_sql)
            self.conexao.commit()

            if cursor.rowcount < 1:
                return 0

            return cursor.rowcount
        except Exception as e:
            return e