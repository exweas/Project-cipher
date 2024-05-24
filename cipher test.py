class VigenereCipher(object):
    """
    Класс реализует шифр Виженера.
    """
    def __init__(self, key, alphabet):
        self.alphabet = alphabet
        self.key = key

    def chiper(self, text, mode):
        """
        Метод реализует шифровку/дешифровку в зависимости от параметра mode.

        Аргументы:
            text: текст для шифровки/дешифровки
            mode: режим работы метода: 'encode' (шифровка) или 'decode' (дешифровки).
        """
        PLUS_OR_MINUS = 1 if mode == 'encode' else -1

        result = ''
        for text_index, char in enumerate(text):
            if char in self.alphabet:
                alphabet_index = self.alphabet.index(char)
                key_index = text_index % len(self.key)
                key_char = self.key[key_index]
                bias_index = self.alphabet.index(key_char)
                encode_index = (
                    alphabet_index + PLUS_OR_MINUS * bias_index
                ) % len(self.alphabet)
                result += self.alphabet[encode_index]
            else:
                result += char

        return result

    def encode(self, text):
        """
        Метод для шифровки текста, вызывает метод chiper с mode='encode'.
        """
        return self.chiper(text, 'encode')

    def decode(self, text):
        """
        Метод для дешифровки текста, вызывает метод chiper с mode='decode'.
        """
        return self.chiper(text, 'decode')


# Зададим алфавит
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Запросим у пользователя ключ
key = input("Enter key: ")

# Запросим у пользователя слово, которое нужно зашифровать
word = input("Enter word: ")

# Создадим экземпляр класса VigenereCipher
cipher = VigenereCipher(key, alphabet)

# Отделим результат работы пустой строкой
print()
# Выведем исходный текст
print(f"Original text: {word}")

# Зашифруем текст и выведем результат шифрования
encoded = cipher.encode(word)
print(f"Encoded text: {encoded}")

# Расшифруем текст и выведем результат расшифровки
print(f"Decoded text: {cipher.decode(encoded)}")
