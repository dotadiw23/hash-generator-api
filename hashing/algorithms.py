import os
import base64
import hashlib

def crear_fichero(request: dict):
    """
    Crea un fichero en el servidor a partir de una cadena codificada en base64.
    Args:
        self (FileHashController)
        request (dict): body de la petición
    """
    with open(request['nombre'], 'w') as f:
        f.write(base64.b64decode(request['archivo']).decode("utf-8"))

def eliminar_fichero(file_name: str):
    """
    Elimina un fichero en el servidor.
    Args:
        self (FileHashController)
        file_name (str): nombre del fichero
    """
    os.remove(file_name)

def generar_md5(request: dict):
    """
    Genera una cadena de hash usando el algoritmo MD5 para un fichero codificado
    en base64.
    Args:
        self (FileHashController)
        request (dict): body de la petición
    """
    crear_fichero(request)

    with open(request['nombre'], mode='rb') as f:
        hash_file = (hashlib.md5(f.read()).hexdigest())
    
    eliminar_fichero(request['nombre'])
    return {
        'hash': hash_file
    }


def generar_sha1(request: dict):
    """
    Genera una cadena de hash usando el algoritmo SHA1 para un fichero codificado
    en base64.
    Args:
        self (FileHashController)
        request (dict): body de la petición
    """
    crear_fichero(request)

    with open(request['nombre'], mode='rb') as f:
        hash_file = (hashlib.sha1(f.read()).hexdigest())
    
    eliminar_fichero(request['nombre'])
    return {
        'hash': hash_file
    }

def generar_sha256(request: dict):
    return {

    }
