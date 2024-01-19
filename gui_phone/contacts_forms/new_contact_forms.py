import tkinter as tk
from tkinter import messagebox

from globals import logger, path_csv, convert_file
from core_phone.contacts.creating import ContactManager
from core_phone.contacts.new_contact import Contact


class ContactGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Создание контакта")

        # Создаем поля для ввода данных
        tk.Label(root, text="Имя:").grid(row=0, column=0)
        self.firstname_entry = tk.Entry(root)
        self.firstname_entry.grid(row=0, column=1)

        tk.Label(root, text="Фамилия:").grid(row=1, column=0)
        self.lastname_entry = tk.Entry(root)
        self.lastname_entry.grid(row=1, column=1)

        tk.Label(root, text="Номер телефона:").grid(row=2, column=0)
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=2, column=1)

        tk.Label(root, text="E-mail:").grid(row=3, column=0)
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=3, column=1)

        tk.Label(root, text="Описание:").grid(row=4, column=0)
        self.description_entry = tk.Entry(root)
        self.description_entry.grid(row=4, column=1)

        # Кнопка для создания нового контакта
        create_button = tk.Button(root, text="Создать контакт", command=self.create_contact)
        create_button.grid(row=5, columnspan=2)

    def create_contact(self):
        # Получаем данные из полей ввода
        firstname = self.firstname_entry.get()
        lastname = self.lastname_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        description = self.description_entry.get()

        try:
            # Создаем экземпляр класса Contact
            contact = Contact(firstname, lastname, phone, email, description)

            contact_details = contact.get_details().strip().split(';')

            # Здесь должна быть логика добавления контакта в вашу систему управления контактами
            # Например:
            contact_manager = ContactManager(path_csv)
            contact_manager.add_contact(contact_details)
            convert_file()

            logger.info(f'Новая запись в телефонной книге: \n{contact.get_details()} успешно создана!')
            messagebox.showinfo("Успех", f'Новая запись в телефонной книге: \n{contact.get_details()} успешно создана!')
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка при создании нового контакта: {e}")
            logger.error(f"Произошла ошибка при создании нового контакта: {e}")

