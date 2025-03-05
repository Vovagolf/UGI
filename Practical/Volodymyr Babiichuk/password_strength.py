def password_strength(password):
    if len(password) < 8:
        return "Слабкий"

    has_digit = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)

    if has_digit and has_upper and has_lower:
        return "Сильний"
    elif (has_digit and has_upper) or (has_digit and has_lower) or (has_upper and has_lower):
        return "Середній"
    else:
        return "Слабкий"

user_password = input("Введіть пароль: ")
result = password_strength(user_password)
print(f"Оцінка сили пароля: {result}")