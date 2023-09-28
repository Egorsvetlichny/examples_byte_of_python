import sys
import os

print("Аргументы командной строки:")
for i in sys.argv:
    print(i)

print('\n\nПеременная PYTHONPATH содержит', sys.path, '\n')

print("Текущий каталог программы: ", os.getcwd()) # вывод текущего каталога программы