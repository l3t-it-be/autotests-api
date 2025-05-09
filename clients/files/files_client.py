from typing import TypedDict, Dict, Any

from httpx import Response

from clients.api_client import APIClient


class CreateFileRequestDict(TypedDict):
    """
    Описание структуры запроса на создание файла.
    """

    filename: str
    directory: str
    upload_file: str


class FilesClient(APIClient):
    """
    Клиент для работы с /api/v1/files
    """

    def get_file_api(self, file_id: str) -> Response:
        """
        Метод получения файла.

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f'/api/v1/files/{file_id}')

    def create_file_api(self, request: CreateFileRequestDict) -> Response:
        """
        Метод создания файла.

        :param request: Словарь с filename, directory, upload_file.
        :return: Ответ от сервера в виде объекта httpx.Response
        """

        form_data: Dict[str, Any] = {
            'filename': request['filename'],
            'directory': request['directory'],
        }

        file_to_upload = open(request['upload_file'], 'rb')

        return self.post(
            '/api/v1/files',
            data=form_data,
            files={'upload_file': file_to_upload},
        )

    def delete_file_api(self, file_id: str) -> Response:
        """
        Метод удаления файла.

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f'/api/v1/files/{file_id}')
