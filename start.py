import os

from globals import logger, path_csv
from core_phone.contacts.creating import ContactManager


def check():
    try:
        # Логируем начало проверки
        logger.info(f'Проверяем наличие файла {path_csv}...')

        valid_csv = os.path.exists(path_csv)

        if not valid_csv:
            # Логируем отсутствие файла
            logger.warning('Файл *.csv отсутствует. Создаем новый.')
            print('*.csv файла нет')

            # Попытка создать файл
            # Создание экземпляра класса  ContactManager
            csv_creator = ContactManager(path_csv)
            csv_creator.create_csv()

            # Логируем успешное создание файла
            logger.info('Файл *.csv успешно создан.')
        else:
            # Логируем успешное завершение проверки, если файл существует
            logger.info(f'Файл {path_csv} существует и доступен для чтения.')

    except Exception as e:
        # Логируем любые другие ошибки, возникшие в процессе проверки или создания файла
        logger.error(f'Произошла ошибка при проверке или создании файла {path_csv}: {e}')
        raise  # Перебрасываем исключение дальше, если это необходимо
