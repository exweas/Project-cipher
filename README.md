Добрый день! 
Хочу представить код позволяющий увидеть зашифрованное слово по методу шифра Виженера.
Шифр Виженера — метод полиалфавитного шифрования буквенного текста с использованием ключевого слова.

В шифре Цезаря каждая буква алфавита сдвигается на несколько позиций; например в шифре Цезаря при сдвиге +3, A стало бы D, B стало бы E и так далее.
Шифр Виженера состоит из последовательности нескольких шифров Цезаря с различными значениями сдвига. Для зашифровывания может использоваться таблица алфавитов, называемая tabula recta или квадрат (таблица) Виженера. Применительно к латинскому алфавиту таблица Виженера составляется из строк по 26 символов, причём каждая следующая строка сдвигается на несколько позиций. Таким образом, в таблице получается 26 различных шифров Цезаря. На каждом этапе шифрования используются различные алфавиты, выбираемые в зависимости от символа ключевого слова. Например, предположим, что исходный текст имеет такой вид:
IRNITU
Человек, посылающий сообщение, записывает ключевое слово своего рода ключ  («IRKUTSK»)
Далее сообщение зашифровывается и получается слово : QIXCMM
Зная ключ мы можем узнать исходное слово, для этого вводим в графу исходного текста QIXCMM ,ключ используем прежний IRKUTSK и получаем слово IRNITU 
Для проверки работоспособности можем воспользоваться сервисом https://www.boxentriq.com/code-breaking/vigenere-cipher