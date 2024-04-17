def vigenere(text, key, mode):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # определение алфавита
    key = key.upper()  # перевод ключа в верхний регистр
    key_length = len(key)  # определение длины ключа
    encrypted_text = ''  # инициализация зашифрованного текста

    for i in range(len(text)):  # проход по символам текста
        if text[i].isalpha():  # если символ буквенный
            key_char = key[i % key_length]  # выбор символа ключа для данной итерации
            if mode == 'encrypt':  # если режим зашифровки
                shift = alphabet.index(key_char)
            elif mode == 'decrypt':  # если режим расшифровки
                shift = -alphabet.index(key_char)  # определение сдвига для расшифровки
            encrypted_char = alphabet[(alphabet.index(text[i].upper()) + shift) % 26]  # шифрование символа
            encrypted_text += encrypted_char if text[i].isupper() else encrypted_char.lower()  # добавление символа к зашифрованному тексту, учитывая регистр
        else:
            encrypted_text += text[i]  # добавление символа к зашифрованному тексту без шифровки
            return encrypted_text
