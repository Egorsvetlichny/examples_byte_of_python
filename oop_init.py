class Person:
    def __init__(self, name):  # Метод __init__ запускается, как только объект класса реализуется
        self.name = name

    def sayHi(self):
        print('Привет! Меня зовут', self.name)


p = Person('Swaroop')
p.sayHi()

# Предыдущие 2 строки можно
# Person('Swaroop').say_hi()
