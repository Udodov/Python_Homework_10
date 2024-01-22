# Импорт модулей, связанных с функциональностью телефонной книги
import tkinter as tk
from tkinter import messagebox

from globals import logger, path_csv
from core_phone.storage.read_phonebook import FileReader
from gui_phone.contacts_forms.new_contact_forms import ContactGUI
# from gui_phone.contacts_forms.search_contact_forms import ContactSearchGUI
from core_phone.contacts.search_contact import ContactSearcher
from core_phone.contacts.deleting_contact import ContactDeleter


class MainFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.create_widgets()
        self.searcher = ContactSearcher()

    def create_widgets(self):
        tk.Button(self, text="Просмотреть все контакты", command=self.view_contacts).pack(fill=tk.X)
        tk.Button(self, text="Добавить новый контакт", command=self.add_contact).pack(fill=tk.X)
        tk.Button(self, text="Найти существующий контакт", command=self.search_contact).pack(fill=tk.X)
        tk.Button(self, text="Удалить существующий контакт", command=self.delete_contact).pack(fill=tk.X)
        tk.Button(self, text="Выход", command=self.quit_app).pack(fill=tk.X)

    #  Методы для обработки действий пользователя:
    def view_contacts(self):  # для просмотра всех контактов
        reader = FileReader(path_csv)
        my_file = reader.read_from_file()
        messagebox.showinfo("Контакты", my_file)
        logger.info('Просмотр всех контактов в GUI')

    def add_contact(self):  # для добавления нового контакта
        new_contact_window = tk.Toplevel(self)  # Создаем новое дочернее окно
        new_contact_window.title("Добавить контакт")  # Задаем заголовок окна
        ContactGUI(new_contact_window)  # Используем это окно для создания интерфейса добавления контакта
        # Добавляем кнопку "Назад" в дочернее окно
        back_button = tk.Button(new_contact_window, text="Назад", command=new_contact_window.destroy)
        back_button.grid(row=6, column=2)
        logger.info('Добавление нового контакта в GUI')

    def search_contact(self):  # для поиска контакта
        # searcher_window = tk.Toplevel(self)  # Создаем новое дочернее окно
        # ContactSearchGUI(searcher_window)

        searcher = ContactSearcher()
        found_contacts = searcher.search_contact()  # Эту функцию надо адаптировать под GUI
        # Теперь отображаем найденные контакты в виде сообщения
        messagebox.showinfo("Результат поиска", "\n".join(found_contacts))
        logger.info('Поиск контакта в GUI')

    def delete_contact(self):  # для удаления контакта
        deleter = ContactDeleter()
        if deleter.delete_contact_record():  # Эту функцию надо адаптировать под GUI
            messagebox.showinfo("Удаление контакта", "Контакт успешно удалён")
        else:
            messagebox.showwarning("Удаление контакта", "Контакт не найден или ошибка удаления")
        logger.info('Удаление контакта в GUI')

    def quit_app(self):
        self.master.quit()
