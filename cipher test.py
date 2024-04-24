def vigenere(text, key, mode):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # определение алфавита
    key = key.upper()  # перевод ключа в верхний регистр
    key_length = len(key)  # определение длины ключа
    result_text = ''  # инициализация  текста с результатом

    for i in range(len(text)):  # проход по символам текста
        if text[i].isalpha():  # если символ буквенный
            key_char = key[i % key_length]  # выбор символа ключа для данной итерации
            if mode == 'encrypt':  # если режим зашифровки
                shift = alphabet.index(key_char)
            elif mode == 'decrypt':  # если режим расшифровки
                shift = -alphabet.index(key_char)  # определение сдвига для расшифровки
            result_char = alphabet[(alphabet.index(text[i].upper()) + shift) % 26]  # шифрование/расшифровывание символа
            result_text += result_char if text[i].isupper() else result_char.lower()  # добавление символа к результату, учитывая регистр
        else:
            result_text += text[i]  # добавление символа к результату без шифровки
    return result_text

text = 'What is love'  # исходный текст
key = 'Monkey'  # ключ
encrypted_text = vigenere(text, key, 'encrypt')  # зашифрованный текст
decrypted_text = vigenere(encrypted_text, key, 'decrypt')  # расшифрованный текст

print('Original text:', text)  # вывод исходного текста
print('Encrypted text:', encrypted_text)  # вывод зашифрованного текста
print('Decrypted text:', decrypted_text)  # вывод расшифрованного текста

