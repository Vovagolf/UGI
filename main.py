def password_strength(password):
    # Перевірка на мінімальну довжину
    if len(password) < 8:
        return "Слабкий"

    # Перевірка наявності цифр, великих та малих літер
    has_digit = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)

    # Оцінка сили пароля
    if has_digit and has_upper and has_lower:
        return "Сильний"
    elif (has_digit and has_upper) or (has_digit and has_lower) or (has_upper and has_lower):
        return "Середній"
    else:
        return "Слабкий"

# Запит користувача на введення пароля
user_password = input("Введіть пароль: ")

# Оцінка сили пароля та виведення результату
result = password_strength(user_password)
print(f"Оцінка сили пароля: {result}")