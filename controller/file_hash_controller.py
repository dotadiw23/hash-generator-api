import base64
import hashlib
import os
from re import M
from xxlimited import foo
from flask import make_response, request
from flask_apispec import MethodResource, doc, use_kwargs, marshal_with
from flask_restful import Resource
from marshmallow import fields

from http import HTTPStatus

from dto.generar_hash_response_dto import GenerarHashResponseDto


class FileHashController(MethodResource, Resource):

    def crear_fichero(self, request: dict):
        with open(request['nombre'], 'w') as f:
            f.write(base64.b64decode(request['archivo']).decode("utf-8"))

    def eliminar_fichero(self, file_name: str):
        os.remove(file_name)

    def generar_md5(self, request: dict):
        """
        Genera una cadena de hash usando el algoritmo MD5 para un fichero codificado
        en base64.
        Args:
            self (FileHashController)
            request (dict): body de la petición
        """
        self.crear_fichero(request)

        with open(request['nombre'], mode='rb') as f:
            hash_file = (hashlib.md5(f.read()).hexdigest())
        
        self.eliminar_fichero(request['nombre'])
        return {
            'hash': hash_file
        }


    def generar_sha1(self, request: dict):
        return {}

    def generar_sha256(self, request: dict):
        return {}

    @doc(description='Generar hash a partir de un archivo', tags=['Hash'])
    @marshal_with(GenerarHashResponseDto, code=HTTPStatus.CREATED, description='Hash generado correctamente')
    def post(self, metodo: str):
        request_payload: dict = request.get_json()
        
        if 'nombre' not in request_payload or 'archivo' not in request_payload:
            return make_response({'hash': None, 'descripcion' : 'Faltan parámetros en el cuerpo de la petición'}, 400)

        if metodo.upper() == 'MD5':
            return make_response(self.generar_md5(request_payload), 201)
        elif metodo.upper() == 'SHA1':
            return make_response(self.generar_sha1(request_payload['archivo']), 201)
        elif metodo.upper() == 'SHA256':
            return make_response(self.generar_sha256(request_payload['archivo']), 201)

        return make_response(
            {
                'hash': None,
                'descripcion' : 'El algoritmo no ha sido encontrado.'
            }, 404
        )
