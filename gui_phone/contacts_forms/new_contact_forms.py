# import time  # Импортируем модуль time
import tkinter as tk
from tkinter import messagebox

from core_phone.contacts.new_contact import Contact


class ContactForm(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Добавить контакт")

        # Создаем виджеты для формы
        tk.Label(self, text="Имя:").grid(row=0, column=0)
        self.entry_firstname = tk.Entry(self)
        self.entry_firstname.grid(row=0, column=1)

        tk.Label(self, text="Фамилия:").grid(row=1, column=0)
        self.entry_lastname = tk.Entry(self)
        self.entry_lastname.grid(row=1, column=1)

        tk.Label(self, text="Телефон:").grid(row=2, column=0)
        self.entry_phone = tk.Entry(self)
        self.entry_phone.grid(row=2, column=1)

        tk.Label(self, text="E-mail:").grid(row=3, column=0)
        self.entry_email = tk.Entry(self)
        self.entry_email.grid(row=3, column=1)

        tk.Label(self, text="Описание:").grid(row=4, column=0)
        self.entry_description = tk.Entry(self)
        self.entry_description.grid(row=4, column=1)

        # Кнопка для сохранения контакта
        save_button = tk.Button(self, text="Сохранить", command=self.save_contact)
        save_button.grid(row=5, column=0, columnspan=2)

    def save_contact(self):
        firstname = self.entry_firstname.get()
        lastname = self.entry_lastname.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()
        description = self.entry_description.get()

        if firstname and lastname and phone and email:
            try:
                # Генерация уникального ID на основе текущего времени
                contact_id = str(int(time.time() * 1000))

                # Создаем экземпляр контакта с генерированным ID
                contact = Contact(contact_id, firstname, lastname, phone, email, description)

                # Добавляем контакт в словарь контактов
                self.parent.contacts[contact_id] = contact

                messagebox.showinfo("Успех", f"Контакт успешно добавлен:\n{contact.get_details()}")
                self.destroy()
            except Exception as e:
                messagebox.showerror("Ошибка", f"Произошла ошибка при создании нового контакта: {e}")
        else:
            messagebox.showerror("Ошибка", "Необходимо заполнить все поля.")
