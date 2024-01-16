import tkinter as tk
from tkinter import messagebox

from globals import (logger, path_csv,
                     csv_to_txt_converter, csv_to_xml_converter, csv_to_html_converter, csv_to_json_converter)
from core_phone.contacts.creating import ContactManager
from core_phone.contacts.new_contact import Contact


class NewContactForm(tk.Toplevel):
    """Класс для создания нового контакта с помощью графического интерфейса Tkinter."""

    def __init__(self, parent):
        super().__init__(parent)
        self.title("Новый контакт")

        # Создание виджетов для ввода информации о контакте
        tk.Label(self, text="Имя:").grid(row=0, column=0)
        self.firstname_entry = tk.Entry(self)
        self.firstname_entry.grid(row=0, column=1)

        tk.Label(self, text="Фамилия:").grid(row=1, column=0)
        self.lastname_entry = tk.Entry(self)
        self.lastname_entry.grid(row=1, column=1)

        tk.Label(self, text="Телефон:").grid(row=2, column=0)
        self.phone_entry = tk.Entry(self)
        self.phone_entry.grid(row=2, column=1)

        tk.Label(self, text="E-mail:").grid(row=3, column=0)
        self.email_entry = tk.Entry(self)
        self.email_entry.grid(row=3, column=1)

        tk.Label(self, text="Описание:").grid(row=4, column=0)
        self.description_entry = tk.Entry(self)
        self.description_entry.grid(row=4, column=1)

        # Кнопка для создания контакта
        create_button = tk.Button(self, text="Создать", command=self.create_contact)
        create_button.grid(row=5, columnspan=2)

    def create_contact(self):
        # Получение данных из виджетов и их обработка с помощью метода input_name класса Contact
        firstname = Contact.input_name(self.firstname_entry.get())
        lastname = Contact.input_name(self.lastname_entry.get())
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        description = self.description_entry.get()

        # Проверка на заполненность полей
        if not all([firstname, lastname, phone, email]):
            messagebox.showwarning("Предупреждение", "Все поля должны быть заполнены!")
            return

        try:
            # Создание экземпляра ContactManager и добавление нового контакта
            contact_manager = ContactManager(path_csv)
            contact_details = Contact(firstname, lastname, phone, email, description)  # Создаем экземпляр контакта
            contact_manager.add_contact(contact_details)  # Добавляем контакт через contact_manager

            # Методы для конвертации измененного файла в другие форматы
            csv_to_txt_converter.convert()
            csv_to_xml_converter.convert()
            csv_to_json_converter.convert()
            csv_to_html_converter.convert()

            # Логирование и уведомление пользователя об успешном создании контакта
            logger.info(f'Новая запись в телефонной книге: {contact_details} успешно создана!')
            messagebox.showinfo("Успех", "Новый контакт успешно создан!")

            # Закрытие окна после создания контакта
            self.destroy()

        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка при создании нового контакта: {e}")
            logger.error(f"Произошла ошибка при создании нового контакта: {e}")
