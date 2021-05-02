# Case-study #8-2
# Developers:   Braer P. (90%),
#               Kokorina D. (20%),
#               Novoselov V. (0%)

print("""Case-study Файловая система
Разработчики:
Браер П.С., Кокорина Д.Е., Новоселов В.В.
""")

import os


def check():
    files = []
    direction = []
    path = os.getcwd()
    for element in os.scandir(path):
        if element.is_dir():
            direction.append(element.name)
    print('Папки: ')
    for dir in direction:
        print(dir)
    for element in os.scandir(path):
        if element.is_file():
            files.append(element.name)
    print('Файлы: ')
    for file in files:
        print(file)


# moveUp & moveDown function
def moveUp():
    path = os.getcwd()
    second_path = os.path.dirname(path)
    return os.chdir(second_path)


def moveDown(cur_dir):
    is_true = 0
    while is_true != 1:
        file_name = input()
        second_path = os.path.join(cur_dir, file_name)
        if os.path.exists(second_path) == True:
            is_true = 1
        else:
            print('ERROR')
            is_true = 0
    if os.path.isdir(second_path) == True:
        return os.chdir(second_path)
    return os.startfile(second_path)


# findFiles function
def findFiles(path, second_path, object):
    if os.path.isfile(object) != True:
        print('ERROR')
        return
    dir_list_1 = os.listdir(path)
    dir_list_2 = []
    if len(dir_list_1) != 0:
        for file in dir_list_1:
            if file == object and os.path.isfile(file) == True:
                print(os.path.join(path, file))
            dir_list_2.append(file)
        return findFiles(os.path.join(path, file), second_path, object)
    return



# countFiles function
def first_step_count(path):
    if os.path.isfile(path):
        return 1
    direction_list = os.listdir(path)
    size = 0
    for direction in direction_list:
        second_path = path + '\\' + direction
        size += first_step_count(second_path)
    return size


def second_step_count(path):
    size = 0
    direction_list = os.listdir(path)
    for direction in direction_list:
        new_path = path + '\\' + direction
        if os.path.isdir(new_path):
            size += second_step_count(new_path) + 1
    return size


def countFiles(path):
    return first_step_count(path) + second_step_count(path)


# countBytes function
def countBytes(path):
    if os.path.isfile(path) == True:
        return os.path.getsize(path)
    size = 0
    direction_list = os.listdir(path)
    for direction in direction_list:
        second_path = path + '\\' + direction
        size += countBytes(second_path)
    return size


# acceptCommand function
def acceptCommand():
    print('''
    C:\Python54
    1. Просмотр каталога
    2. На уровень вверх
    3. На уровень вниз
    4. Количество файлов и каталогов
    5. Размер текущего каталога (в байтах)
    6. Поиск файла
    7. Выход из программы''')
    try:
        command = int(input('Введите номер команды: '))
        if command <= 7 and command >= 1:
            return command
        else:
            print('ERROR')
            return acceptCommand()
    except ValueError:
        acceptCommand()


# runCommand function
def runCommand(command):
    if command == 1:
        check()
    if command == 2:
        moveUp()
    path = os.getcwd()
    if command == 3:
        moveDown(path)
    if command == 4:
        print(countFiles(path))
    if command == 5:
        print(countBytes(path))
    if command == 6:
        object = input('Введите полное имя файла: ')
        second_path = path
        print(findFiles(path, second_path, object))



# main function
def main():
    while True:
        print(os.getcwd())
        command = acceptCommand()
        if command == 7:
            print('Работа программы завершена.')
            return
        runCommand(command)


main()
