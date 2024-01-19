import time

from globals import (logger, path_csv,
                     csv_to_txt_converter, csv_to_xml_converter, csv_to_html_converter, csv_to_json_converter)
from core_phone.contacts.creating import ContactManager


class Contact:
    """Класс для создания контактов."""

    def __init__(self, firstname, lastname, phone, email, description):
        self.id = str(int(time.time() * 1000))  # Генерация уникального ID на основе текущего времени
        self.firstname = self.input_name(firstname)
        self.lastname = self.input_name(lastname)
        self.phone = phone
        self.email = email
        self.description = description

    @staticmethod
    def input_name(name):  # Это статический метод класса Contact, который принимает строку name,
        """Преобразует имя и фамилию в нужный формат."""
        name = name.strip()  # очищает её от лишних пробелов,
        name = name.replace(" ", "_")  # # заменяет пробелы на символ подчеркивания
        name = "_".join(word.capitalize() for word in name.split("_"))  # и делает каждое слово с большой буквы.
        return name

    @classmethod
    def from_string(cls, contact_str):
        """Создает экземпляр Contact из строки с данными."""
        parts = contact_str.split(';')
        if len(parts) != 5:
            raise ValueError("Строка не содержит достаточное количество данных для создания контакта")

        # Создаем и возвращаем экземпляр Contact
        return cls(*parts)

    def get_details(self) -> str:
        """Возвращает детали контакта в виде строки."""
        return f"{self.id};{self.firstname};{self.lastname};{self.phone};{self.email};{self.description}\n"


def new():  # Это основная функция модуля
    """Создает новый контакт."""
    try:
        # которая запрашивает у пользователя данные для создания нового контакта
        firstname = input('Введите имя: ')
        lastname = input('Введите фамилию: ')
        phone = input('Введите номер телефона: ')
        email = input('Введите E-mail: ')
        description = input('Добавьте описание к контакту: ')

        # Создаем экземпляра класса Contact
        contact = Contact(firstname, lastname, phone, email, description)

        contact_details = contact.get_details().strip().split(';')

        # Создаем экземпляр CsvCreator
        contact_manager = ContactManager(path_csv)

        # Создаем экземпляр ContactCreator
        contact_manager.add_contact(contact_details)

        # Методы для конвертации измененного файла в другие форматы
        csv_to_txt_converter.convert()
        csv_to_xml_converter.convert()
        csv_to_json_converter.convert()
        csv_to_html_converter.convert()

        logger.info(f'Новая запись в телефонной книге: \n{contact.get_details()} успешно создана!')
        print(f'Новая запись в телефонной книге: \n{contact.get_details()} успешно создана!')
    except Exception as e:
        print(f"Произошла ошибка при создании нового контакта: {e}")
        logger.error(f"Произошла ошибка при создании нового контакта: {e}")
