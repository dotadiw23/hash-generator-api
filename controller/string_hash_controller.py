from http import HTTPStatus

from flask import make_response, request
from flask_apispec import MethodResource, use_kwargs, doc, marshal_with
from flask_restful import Resource

from dto.generar_hash_response_dto import GenerarHashResponseDto


class StringHashController(MethodResource, Resource):

    @doc(description='Generar hash a partir de una cadena de texto', tags=['Hash'])
    @marshal_with(GenerarHashResponseDto, code=HTTPStatus.OK, description='Hash generado correctamente')
    def post(self, metodo: str):
        request_payload: dict = request.get_json()
        return make_response({'resultado': True})
