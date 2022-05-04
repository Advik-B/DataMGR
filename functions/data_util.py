from cryptography.fernet import Fernet
from typing import Union


def GenerateKey():
    k = Fernet.generate_key()
    return {"data": k, "key": Fernet(k)}


def decrpyt_file_and_return_bytes(file: str, key: Union[bytes, str, Fernet]) -> bytes:
    """
    :param file: File path
    :param key: bytes or string or an instance of a Fernet
    :return: decoded bytes
    """
    with open(file, "rb") as file_to_decrypt:
        if isinstance(key, bytes):
            return Fernet(key).decrypt(file_to_decrypt.read())
        if isinstance(key, Fernet):
            return key.decrypt(file_to_decrypt.read())
        if isinstance(key, str):
            return Fernet(bytes(key)).decrypt(file_to_decrypt.read())


def decrpyt_file(
        file: str, key: Union[bytes, str, Fernet], output_file: Union[str, None] = None
) -> str:
    """

    :param file: File path
    :param key: bytes or string or an instance of a Fernet
    :param output_file: name of the output file
    :return: Path of output file
    """
    if output_file is None:
        output_file = file.replace(".enc", "")

    with open(output_file, "wb") as f:
        f.write(decrpyt_file_and_return_bytes(file, key))


def encrypt_file_and_return_bytes(file: str, key: Union[bytes, str, Fernet]) -> bytes:
    """
    :param file: File path
    :param key: bytes or string or an instance of a Fernet
    :return: decoded bytes
    """
    with open(file, "rb") as file_to_encrypt:
        if isinstance(key, bytes):
            return Fernet(key).encrypt(file_to_encrypt.read())
        if isinstance(key, Fernet):
            return key.encrypt(file_to_encrypt.read())
        if isinstance(key, str):
            return Fernet(bytes(key)).encrypt(file_to_encrypt.read())


def encrypt_file(
        file: str, key: Union[bytes, str, Fernet], output_file: Union[str, None] = None
) -> str:
    """

    :param file: File path
    :param key: bytes or string or an instance of a Fernet
    :param output_file: name of the output file
    :return: Path of output file
    """
    if output_file is None:
        output_file = file + ".enc"

    with open(output_file, "wb") as f:
        f.write(encrypt_file_and_return_bytes(file, key))

    return output_file

def get_key_from_file(file: str) -> bytes:
    """

    :param file:
    :return:
    """
    with open(file, "rb") as file_to_decrypt:
        return file_to_decrypt.read()

def get_key_from_string(key: str) -> bytes:
    """

    :param key:
    :return:
    """
    return bytes(key)

def get_key_from_fernet(key: Fernet) -> bytes:
    """

    :param key:
    :return:
    """
    return key.key

def compress_file(file: str, output_file: Union[str, None] = None) -> str:
    """

    :param file:
    :param output_file:
    :return:
    """
    if output_file is None:
        output_file = file + ".zip"

    import zipfile
    with zipfile.ZipFile(output_file, "w") as zf:
        zf.write(file)

    return output_file

def decompress_file(file: str, output_file: Union[str, None] = None) -> str:
    """

    :param file:
    :param output_file:
    :return:
    """
    if output_file is None:
        output_file = file.replace(".zip", "")

    import zipfile
    with zipfile.ZipFile(file, "r") as zf:
        zf.extractall(output_file)

    return output_file
