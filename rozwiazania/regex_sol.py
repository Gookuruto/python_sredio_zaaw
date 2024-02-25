import re

# Walidacja adresu e-mail
import datetime


def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

# Wyszukiwanie kodów pocztowych
def find_postal_codes(text):
    pattern = r'\b\d{2}-\d{3}\b'
    return re.findall(pattern, text)

# Sprawdzanie poprawności numeru telefonu
def validate_phone_number(phone_number):
    pattern = r'^(\+\d{2})?\s?\d{3}[-\s]?\d{3}[-\s]?\d{3}$'
    return re.match(pattern, phone_number) is not None

# Wyszukiwanie URL-i
def find_urls(text):
    pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    return re.findall(pattern, text)

# Zastępowanie słów
def replace_word(text, word, replacement):
    pattern = re.compile(r'\b' + re.escape(word) + r'\b')
    return pattern.sub(replacement, text)

# Walidacja numeru karty kredytowej
def validate_credit_card_number(card_number):
    pattern = r'^\d{4}-\d{4}-\d{4}-\d{4}$'
    if re.match(pattern, card_number) is None:
        return False
    digits = [int(digit) for digit in card_number if digit.isdigit()]
    checksum = sum(digits[::-2] + [sum(divmod(2 * digit, 10)) for digit in digits[-2::-2]])
    return checksum % 10 == 0

# Wyszukiwanie haseł
def find_passwords(text, password):
    pattern = re.compile(re.escape(password), re.IGNORECASE)
    return [match.start() for match in pattern.finditer(text)]

# Sprawdzanie poprawności formatu daty
def validate_date_format(date, format):
    try:
        datetime.datetime.strptime(date, format)
        return True
    except ValueError:
        return False

# Wyszukiwanie słów zaczynających się na określoną literę
def find_words_starting_with_letter(text, letter):
    pattern = r'\b' + letter + r'\w*\b'
    return re.findall(pattern, text, re.IGNORECASE)

# Zamiana formatu daty
def change_date_format(date, old_format, new_format):
    return datetime.datetime.strptime(date, old_format).strftime(new_format)

# Przykładowe użycie funkcji
if __name__ == "__main__":
    email = "example@example.com"
    print("Email validation:", validate_email(email))

    text = "Sample text with postal codes 12-345 and 98-765."
    print("Postal codes:", find_postal_codes(text))

    phone_number = "123-456-789"
    print("Phone number validation:", validate_phone_number(phone_number))

    text = "Visit our website at https://www.example.com or http://example.org"
    print("URLs:", find_urls(text))

    text = "The quick brown fox jumps over the lazy dog."
    print("Text with replaced word:", replace_word(text, "fox", "cat"))

    card_number = "1234-5678-9012-3456"
    print("Credit card validation:", validate_credit_card_number(card_number))

    text = "Password123passwordPASSWORD"
    password = "password"
    print("Password positions:", find_passwords(text, password))

    date = "2024-02-29"
    old_format = "%Y-%m-%d"
    new_format = "%d-%m-%Y"
    print("Date in new format:", change_date_format(date, old_format, new_format))
