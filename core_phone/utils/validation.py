# Добавить проверку на валидность введенных данных (например, номер телефона или E-mail).
# Это может быть важным для предотвращения записи некорректных данных в телефонную книгу.

def validate_contact(contact):
    # Простая проверка на пустые поля
    for value in contact.values():
        if not value.strip():
            return False
    return True
