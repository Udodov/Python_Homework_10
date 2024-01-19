# Импорт модулей, связанных с функциональностью телефонной книги
import tkinter as tk  # встроенная библиотека для создания GUI
from tkinter import messagebox  # метод для отображения всплывающих окон с информацией.

from globals import logger, path_csv
from core_phone.storage.read_phonebook import FileReader
from gui_phone.contacts_forms.new_contact_forms import ContactGUI
from core_phone.contacts.search_contact import ContactSearcher
from core_phone.contacts.deleting_contact import ContactDeleter


class PhonebookApp(tk.Tk):
    def __init__(self):  # Конструктор класса PhonebookApp
        super().__init__()
        self.title("Телефонная книга")  # устанавливается заголовок окна
        self.create_widgets()  # и вызывается метод create_widgets

    def create_widgets(self):  # Создание кнопок и их размещение в окне приложения
        # Создание меню с кнопками
        tk.Button(self, text="Просмотреть все контакты", command=self.view_contacts).pack(fill=tk.X)
        tk.Button(self, text="Добавить новый контакт", command=self.add_contact).pack(fill=tk.X)
        tk.Button(self, text="Найти существующий контакт", command=self.search_contact).pack(fill=tk.X)
        tk.Button(self, text="Удалить существующий контакт", command=self.delete_contact).pack(fill=tk.X)
        tk.Button(self, text="Выход", command=self.quit).pack(fill=tk.X)

    #  Методы для обработки действий пользователя:
    def view_contacts(self):  # для просмотра всех контактов
        reader = FileReader(path_csv)
        my_file = reader.read_from_file()
        messagebox.showinfo("Контакты", my_file)
        logger.info('Просмотр всех контактов в GUI')

    def add_contact(self):  # для добавления нового контакта
        new_contact_window = tk.Toplevel(self)  # Создаем новое дочернее окно
        ContactGUI(new_contact_window)  # Используем это окно для создания интерфейса добавления контакта
        logger.info('Добавление нового контакта в GUI')

    def search_contact(self):  # для поиска контакта
        searcher = ContactSearcher()
        found_contacts = searcher.search_contact()
        # Эту функцию тоже возможно придется адаптировать под GUI
        searcher.display_contacts(found_contacts)
        logger.info('Поиск контакта в GUI')

    def delete_contact(self):  # для удаления контакта
        deleter = ContactDeleter()
        deleter.delete_contact_record()  # И эту функцию возможно придется адаптировать под GUI
        logger.info('Удаление контакта')
