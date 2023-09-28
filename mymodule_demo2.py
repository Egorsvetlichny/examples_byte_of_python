from mymodule import sayhi, __version__

sayhi()
print("Версия", __version__, "\n")

print(dir(), "\n") # возвращает список имён, определяемых объектом
print(dir("print"))
# при передаче аргумента, функция вернёт список имён, определённых в данном объекте