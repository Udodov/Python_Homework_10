from typing import List  # для аннотации типов

from globals import logger


class FileReader:
    def __init__(self, path: str):
        self.path = path

    def _open_file(self):
        """Приватный метод для открытия файла."""
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            logger.error(f'Файл не найден: {self.path}')
        except Exception as e:
            logger.error(f'Произошла ошибка при чтении файла {self.path}: {e}')
        return None

    def read_from_file(self) -> str:
        """Метод для чтения всего содержимого файла и возвращает строку с этим содержимым."""
        data = self._open_file()
        if data is not None:
            logger.info(f'Успешное чтение данных из файла {self.path}')
            return data
        return ""

    def read_lines_from_file(self) -> List[str]:
        """Метод для построчного чтения файла и возвращает список строк."""
        data = self._open_file()
        if data is not None:
            return data.splitlines()
        return []
