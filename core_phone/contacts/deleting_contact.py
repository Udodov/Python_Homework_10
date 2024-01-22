from globals import logger, path_csv, convert_file
from core_phone.storage.read_phonebook import FileReader
from core_phone.contacts.new_contact import Contact


class ContactDeleter:
    def __init__(self):
        self.file_reader = FileReader(path_csv)

    def delete_contact_record(self):
        del_name = Contact.input_name(input('Введите имя или фамилию для удаления контакта: '))
        my_file = self.file_reader.read_lines_from_file()
        matching_contacts = []

        for index, line in enumerate(my_file):
            if del_name.lower() in line.lower():
                matching_contacts.append((index, line))

        if not matching_contacts:
            print(f'Контакт с именем или фамилией "{del_name}" не найден.')
            logger.warning(f'Контакт "{del_name}" не найден для удаления.')
            return

        if len(matching_contacts) == 1:
            index_to_delete = matching_contacts[0][0]
        else:
            print("Найдены следующие контакты:")
            for idx, (index, contact) in enumerate(matching_contacts):
                print(f"{idx + 1}: {contact.strip()}")

            try:
                selected = int(input("Введите номер контакта для удаления: "))
                index_to_delete = matching_contacts[selected - 1][0]
            except (ValueError, IndexError):
                logger.error('Введен некорректный номер контакта для удаления.')
                print("Введен некорректный номер контакта.")
                return

        confirm = input(f'Вы уверены, что хотите удалить этот контакт? (y/n): ')
        if confirm.lower() == 'y':
            with open(path_csv, 'w', encoding='utf-8') as f:
                for index, line in enumerate(my_file):
                    if index != index_to_delete:
                        f.write(line + '\n')

            # Вызов глобальной функции для конвертации измененного файла в другие форматы
            convert_file()

            print("Контакт удален из телефонной книги.")
            logger.info(f'Контакт "{del_name}" успешно удален.')
        else:
            print("Удаление отменено пользователем.")
            logger.info('Пользователь отменил удаление контакта.')