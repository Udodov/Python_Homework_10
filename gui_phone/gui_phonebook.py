import tkinter as tk

from gui_phone.main_frame import MainFrame


class PhonebookApp(tk.Tk):  # Конструктор класса PhonebookApp
    def __init__(self):
        super().__init__()
        self.title("Телефонная книга")  # Устанавливается заголовок окна
        self.geometry("300x150")  # Устанавливается размер окна
        self.main_frame = MainFrame(self)
        self.create_main_frame()

    def create_main_frame(self):
        # Создаем текущий фрейм
        self.main_frame.pack(fill=tk.BOTH, expand=True)

    def show_frame(self, frame_class):
        # Удаляем текущий фрейм и заменяем его новым
        if self.main_frame is not None:
            self.main_frame.pack_forget()
            self.main_frame.destroy()
        self.main_frame = frame_class(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
