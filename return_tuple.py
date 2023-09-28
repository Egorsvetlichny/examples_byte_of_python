def get_error_details():
    return (2, 'Описание ошибки №2')

errnum, errstr = get_error_details()
print('Ошибка №'+ str(errnum))
print(errstr)

print()

a, *b = [1, 2, 3, 4, 5]
print('a =', a)
print('b =', b)

print()

a = 5; b = 8
print('a =', a)
print('b =', b)
a, b = b, a  # Самый быстрый способ поменять местами 2 значения
print('a =', a)
print('b =', b)