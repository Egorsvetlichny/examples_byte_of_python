import string

# Переворачиваем текст
def reverse(text):
    return text[::-1]

# Проверяем, является ли текст палиндромом
def is_palindrome(text):
    return text == reverse(text)


# Заполняем множество пробелом и знаками пунктуации
forbidden = set([' '])
for symbol in string.punctuation:
    forbidden.add(symbol)

something = input('Введите текст: ')

# Удаляем все знаки пунктуации, пробелы и переводим текст в нижний регистр
for symbol in something:
    if symbol in forbidden:
        something = something.replace(symbol, '')

if is_palindrome(something.lower()):
    print("Да, это палиндром")
else:
    print("Нет, это не палиндром")
