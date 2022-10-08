class IncompleteDataError(Exception):
    pass

while True:
    try:
        line : str = input("Введите данные (фамилия, имя, отчество, год рождения): ")
        raw_data : list = line.split()
        
        if len(raw_data) != 4: raise IncompleteDataError

        with open("file.txt", "a", encoding="UTF-8") as f:
            f.write(f"{raw_data[0]} {raw_data[1]} {raw_data[2]} {raw_data[3]}\n")
        print("Даннные записаны")

    except UnicodeError: print("Ошибка кодировки!")
    except FileNotFoundError: print("Файл для записи не найден!")
    except IncompleteDataError: print("Введены не все необходимые данные")
    except KeyboardInterrupt:
        print("\nВвод завершен!")
        break
