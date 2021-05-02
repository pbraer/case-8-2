# Case-study #8-2
# Developers:   Braer P. (%),
#               Kokorina D. (%),
#               Novoselov V. (%)

print("""Case-study Файловая система
Разработчики:
Браер П.С., Кокорина Д.Е., Новоселов В.В.
""")

import os


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
    command = int(input('Выберите пункт меню: '))
    while command != round(command) or command < 1 or command > 7:
        command = int(input('Выберите пункт меню: '))
    return command



def moveUp():
    os.chdir('..')


def moveDown(currentDir):
    if currentDir in os.listdir(os.getcwd()):
        return os.chdir(currentDir)
    print('ERROR')


# ?
def countFiles_step(path):
    size = len(os.listdir(path))
    if size == 0:
        return 0
    files = os.listdir(path)
    for file in files:
        return size + countFiles(file)


# ?
def countFiles(path):
    os.chdir(path)
    return countFiles_step(path)

def runCommand(command):
    if command == 1:
        return
    if command == 2:
        return
    if command == 3:
        return
    if command == 4:
        return
    if command == 5:
        return
    if command == 6:
        return
    if command == 7:
        return

