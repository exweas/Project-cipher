def vigenere(text, key, mode):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # определение алфавита
    key = key.upper()  # перевод ключа в верхний регистр
    key_length = len(key)  # определение длины ключа
    encrypted_text = ''  # инициализация зашифрованного текста


