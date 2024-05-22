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

# Зададим алфавит и ключ
alphabet = "abcdefghijklmnopqrstuvwxyz"
key = "password"

# Создадим экземпляр класса VigenereCipher
cipher = VigenereCipher(key, alphabet)

# Зашифруем слово 'waffles', а затем передадим результат метода 
# для расшифровки, ожидаем получить исходное слово 'waffles'.
encoded = cipher.encode('waffles')
decoded = cipher.decode(encoded)

# Проверим, получили ли мы слово 'waffles' после шифрования
# и последующего дешифрования, и выведем соответствующее
# сообщение
if decoded == 'waffles':
    print('Your programm is okay')
else:
    print('There are some errors in your programm')
