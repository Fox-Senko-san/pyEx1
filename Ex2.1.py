class EmptyFileError(Exception):
    pass

try:
    with open("file.txt", "r", encoding="UTF-8") as f:
        data = [line.strip().split() for line in f]
    if not data: raise EmptyFileError

    print("%-10s%-10s%-10s%-10s" % ("Имя", "Фамилия", "Отчество", "Дата рождения"))
    for line in data:
        print("%-10s%-10s%-10s%-10s" % (line[0], line[1], line[2], line[3]))

except FileNotFoundError: print("Файл не найден!")
except EmptyFileError: print("Файл пуст!")
except UnicodeError: print("Ошибка кодировки!")