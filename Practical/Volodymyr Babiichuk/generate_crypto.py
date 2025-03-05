import random

def generate_crypto_price():
    crypto = "bitcoin"
    price = random.uniform(20000, 110000)  # Генерація випадкового курсу
    print(f"Поточний курс {crypto}: ${price:.2f}")

if __name__ == "__main__":
    generate_crypto_price()