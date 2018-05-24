from flask import jsonify, request
from app.common.client import query_find_to_dictionary
from app.common.db import BaseDb


class Base2(BaseDb):

    def get(self):
        cpf = request.args.get("cpf")
        query = {'cpf': int(cpf)}
        projection = {'_id': 0, 'cpf': 1, 'idade': 1, 'bens': 1, 'endereco': 1, }
        return jsonify(query_find_to_dictionary(self.db, 'baseB', query, projection))
