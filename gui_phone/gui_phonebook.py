import tkinter as tk
from tkinter import messagebox

from globals import logger, path_csv
from core_phone.storage.read_phonebook import FileReader
from core_phone.contacts.new_contact import new
from core_phone.contacts.search_contact import ContactSearcher
from core_phone.contacts.deleting_contact import ContactDeleter


class PhonebookApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Телефонная книга")
        self.create_widgets()

    def create_widgets(self):
        # Создание меню с кнопками
        tk.Button(self, text="Просмотреть все контакты", command=self.view_contacts).pack(fill=tk.X)
        tk.Button(self, text="Добавить новый контакт", command=self.add_contact).pack(fill=tk.X)
        tk.Button(self, text="Найти существующий контакт", command=self.search_contact).pack(fill=tk.X)
        tk.Button(self, text="Удалить существующий контакт", command=self.delete_contact).pack(fill=tk.X)
        tk.Button(self, text="Выход", command=self.quit).pack(fill=tk.X)

    def view_contacts(self):
        reader = FileReader(path_csv)
        my_file = reader.read_from_file()
        messagebox.showinfo("Контакты", my_file)
        logger.info('Просмотр всех контактов в GUI')

    def add_contact(self):
        new()  # Эту функцию возможно придется адаптировать под GUI
        logger.info('Добавление нового контакта в GUI')

    def search_contact(self):
        searcher = ContactSearcher()
        found_contacts = searcher.search_contact()
        # Эту функцию тоже возможно придется адаптировать под GUI
        searcher.display_contacts(found_contacts)
        logger.info('Поиск контакта в GUI')

    def delete_contact(self):
        deleter = ContactDeleter()
        deleter.delete_contact_record()  # И эту функцию возможно придется адаптировать под GUI
        logger.info('Удаление контакта')
