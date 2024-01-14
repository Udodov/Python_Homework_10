from globals import logger, path_csv
from core_phone.storage.read_phonebook import FileReader
from core_phone.contacts.new_contact import Contact


class ContactSearcher:
    """Класс для поиска контактов."""

    def __init__(self):
        self.file_reader = FileReader(path_csv)

    def search_contact(self):
        search_query = Contact.input_name(input('Введите имя или фамилию для поиска контакта: ')).lower()
        if not search_query or not isinstance(search_query, str):
            logger.error("Поисковый запрос должен быть непустой строкой.")
            return []

        try:
            contacts = self.file_reader.read_lines_from_file()
            found_contacts = [contact for contact in contacts if search_query.lower() in contact.lower()]
            found_contacts = list(found_contacts)

            if not found_contacts:
                logger.warning(f"Контакт с именем {search_query} не найден.")
            else:
                logger.info(f"Найдено {len(found_contacts)} контакт(ов) с именем {search_query}.")
        except FileNotFoundError as e:
            logger.error(f"Файл не найден: {e}")
            return []
        except IOError as e:
            logger.error(f"Ошибка ввода/вывода при чтении файла: {e}")
            return []

        return found_contacts

    @staticmethod
    def display_contacts(contacts):
        """Отображение найденных контактов."""
        if contacts:
            for contact in contacts:
                print(contact)
        else:
            print("Контакт не найден.")
