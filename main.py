from globals import logger
from start import check
from cli_phone.menu_phonebook import menu
from gui_phone.gui_phonebook import PhonebookApp


# Основная функция для запуска программы
def main():
    while True:  # Добавляем цикл для возможности повторного выбора
        user_choice = input("Выберите интерфейс: (1) Текстовый, (2) Графический, (0) Выход: ")
        if user_choice == "1":
            try:
                menu()  # Запуск главного цикла обработки событий в тектовом режиме
            except KeyboardInterrupt:
                logger.info("Текстовая программа была прервана пользователем.")
                print("\nТекстовая программа была прервана пользователем.")
        elif user_choice == "2":
            app = PhonebookApp()  # Создаем экземпляр класса PhonebookApp
            app.mainloop()  # Запуск главного цикла обработки событий GUI
            break  # Выходим из цикла после закрытия GUI
        elif user_choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод. Пожалуйста, введите 1, 2 или 0.")


if __name__ == "__main__":
    check()  # Проверка перед началом работы программы
    logger.info('Телефонная книга запущена')
    main()  # Запуск основной функции программы
