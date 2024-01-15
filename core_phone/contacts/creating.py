import csv
import os


class ContactManager:  # Объединенный класс для управления контактами и CSV-файлом
    def __init__(self, path_file: str):
        self.path_file = path_file
        self.headers = ['ID Контакта', 'Имя', 'Фамилия', 'Номер телефона', 'e-mail', 'Описание']

        self.create_csv()  # Создаем CSV-файл при инициализации объекта

    def create_csv(self):
        if not os.path.exists(self.path_file):
            with open(self.path_file, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file, delimiter=';')  # Указываем разделитель ";"
                writer.writerow(self.headers)

    def add_contact(self, contact_details):
        if len(contact_details) != len(self.headers):
            raise ValueError("Количество предоставленных деталей не соответствует заголовкам.")
        with open(self.path_file, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')  # Указываем разделитель ";"
            writer.writerow(contact_details)
