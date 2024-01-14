import logging
from pathlib import Path


class PhonebookLogger:
    def __init__(self, log_path_str: str):
        self.log_path = Path(log_path_str)
        self.logger = logging.getLogger('PhonebookLogger')
        self.configure_logger()

    def configure_logger(self):
        # Создаем директорию, если она не существует
        self.log_path.parent.mkdir(parents=True, exist_ok=True)

        # Настраиваем логгер
        handler = logging.FileHandler(filename=str(self.log_path))
        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)s | %(message)s',
            datefmt='%Y-%m-%d | %H:%M:%S'
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.DEBUG)
        self.logger.propagate = False

    # Отдельные методы для каждого уровня логирования
    def debug(self, message: str):
        """Метод для логирования отладочных сообщений."""
        self.logger.debug(message)

    def info(self, message: str):
        """Метод для логирования информационных сообщений."""
        self.logger.info(message)

    def warning(self, message: str):
        """Метод для логирования предупреждающих сообщений."""
        self.logger.warning(message)

    def error(self, message: str):
        """Метод для логирования сообщений об ошибках."""
        self.logger.error(message)

    def critical(self, message: str):
        """Метод для логирования критических сообщений."""
        self.logger.critical(message)
