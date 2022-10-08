# With using prettyTable
from prettytable import PrettyTable

class EmptyFileError(Exception):
    pass

try:
    with open("file.txt", "r", encoding="UTF-8") as f:
        data : list = [line.strip().split() for line in f]
    if not data: raise EmptyFileError

    table = PrettyTable(["Имя", "Фамилия", "Отчество", "Дата рождения"])
    for line in data:
        table.add_row(line)
    print(table)

except FileNotFoundError: print("Файл не найден!")
except EmptyFileError: print("Файл пуст!")
except UnicodeError: print("Ошибка кодировки!")
