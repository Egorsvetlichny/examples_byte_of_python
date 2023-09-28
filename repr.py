# Функция repr используется для получения канонического строкового представления объекта.

i = []
i.append('item')
print(repr(i))
print(eval(repr(i)))

# Любопытно, что в большинстве случаев eval(repr(object)) == object.
print(eval(repr(i)) == i)