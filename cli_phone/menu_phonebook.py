from globals import logger, path_csv
from core_phone.storage.read_phonebook import FileReader
from core_phone.contacts.new_contact import new
from core_phone.contacts.search_contact import ContactSearcher
from core_phone.contacts.deleting_contact import ContactDeleter


def menu():
    while True:
        print('\nМЕНЮ Телефонной книги\n'
              '1. Просмотреть все существующие контакты\n'
              '2. Добавить новый контакт\n'
              '3. Найти существующий контакт\n'
              '4. Удалить существующий контакт\n'
              '5. Выход\n')
        choice = input('Выберите пункт меню: ')

        match choice:
            case '1':
                reader = FileReader(path_csv)
                my_file = reader.read_from_file()
                print(my_file)
                logger.info('Просмотр всех контактов')
                input('Вернуться в меню? Нажмите Enter')
                continue
            case '2':
                new()
                logger.info('Добавление нового контакта')
                input('Вернуться в меню? Нажмите Enter')
                continue
            case '3':
                searcher = ContactSearcher()
                found_contacts = searcher.search_contact()
                searcher.display_contacts(found_contacts)
                logger.info('Поиск контакта')
                input('Вернуться в меню? Нажмите Enter')
                continue
            case '4':
                deleter = ContactDeleter()
                deleter.delete_contact_record()
                logger.info('Удаление контакта')
                input('Вернуться в меню? Нажмите Enter')
                continue
            case '5':
                print('Спасибо, что используете эту телефонную книгу!')
                logger.info('Выход из программы')
                break
            case _:
                logger.warning(f'Неверный выбор в меню: {choice}')
                input('Нет такого пункта...\nДля продолжения нажмите Enter и повторите ввод\n')
                continue
