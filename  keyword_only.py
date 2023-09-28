def func(initial=5, *numbers, extra_number):
    count = initial
    for number in numbers:
        count += number
    count += extra_number
    print(count)

func(10, 1, 2, 3, extra_number=50)
func(10, 1, 2, 3) # ошибка, поскольку мы не указали значение
# аргумента по умолчанию для 'extra_number'.


# Если нам нужны аргументы, передаваемые только по ключу, но не нужен параметр со звёздочкой,
# то можно просто указать одну звёздочку без указания имени:
# def total(initial=5, *, extra_number).
