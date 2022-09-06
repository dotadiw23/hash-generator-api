from flask import make_response, request
from flask_apispec import MethodResource, doc, use_kwargs, marshal_with
from flask_restful import Resource
from marshmallow import fields, validate

from http import HTTPStatus

from dto.generar_hash_response_dto import GenerarHashResponseDto


class HashController(MethodResource, Resource):

    @doc(description='Generar hash a partir de un archivo', tags=['Hash'])
    @marshal_with(GenerarHashResponseDto, code=HTTPStatus.OK, description='Hash generado correctamente')
    def post(self, metodo: str):
        solicitud = request.get_json()
        return make_response({'resultado': True})
