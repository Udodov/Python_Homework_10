# Импортируем необходимые объекты и функции из модулей проекта
from globals import logger
from start import check
from cli_phone.menu_phonebook import menu


# Основная функция для запуска программы
def main():
    try:
        menu()
    except KeyboardInterrupt:
        logger.info("Программа была прервана пользователем.")
        print("\nПрограмма была прервана пользователем.")

    # Точка входа в программу


if __name__ == "__main__":
    check()  # Проверка перед началом работы программы
    logger.info('Телефонная книга запущена')
    main()  # Запуск основной функции программы
