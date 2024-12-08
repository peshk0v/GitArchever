import myhelp.filework as mf
import myhelp.interface as mi
from os import listdir
from simple_term_menu import TerminalMenu
from tkinter import filedialog
import sys

def choice(opt):
    options = opt
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    return menu_entry_index

def mainMenu(newrepo):
    newRepoFold = listdir(f"{config['Git']['tempFolder']}/{newrepo}")
    mi.update()
    mi.aprint("GitArch")
    print("Что вы хотите сделать?")
    terminal_menu = TerminalMenu(["Сохранить в папку", "Посмотреть содержимое", "Отредактировать содержимое", "Закрыть"])
    menu_entry_index = terminal_menu.show()

    if menu_entry_index == 0:
        direc = filedialog.askdirectory()
        mi.system(f"cp -r {config['Git']['tempFolder']}/{newrepo} {direc}")
        mi.system(f"rm -rf {config['Git']['tempFolder']}/{newrepo}")
        exit()
    elif menu_entry_index == 1:
        mi.update()
        mi.aprint("GitArch")
        print("Вы в режиме просмотра, для выхода нажмите на любой пункт:\n")
        choice(newRepoFold)
        # input()
        mainMenu(newrepo)   
    elif menu_entry_index == 2:
        edcnon = True
        while edcnon == True:
            newRepoFold = listdir(f"{config['Git']['tempFolder']}/{newrepo}")
            newRepoFold.append("ЗАКРЫТЬ")
            mi.update()
            mi.aprint("GitArch")
            print("Вы в режиме редактирования, нажмите по файлу что бы его редактировать:\n")
            file = choice(newRepoFold)
            if file == len(newRepoFold)-1:
                edcnon = False
                mainMenu(newrepo)  
            mi.update()
            mi.aprint("GitArch")
            print(f"Редактирование файла {newRepoFold[file]}\n")
            chedinf = choice(["Открыть в Nano", "Удалить", "Закрыть"])
            if chedinf == 0:
                mi.system(f"nano {config['Git']['tempFolder']}/{newrepo}/{newRepoFold[file]}")
            elif chedinf == 1:
                mi.system(f"rm -rf {config['Git']['tempFolder']}/{newrepo}/{newRepoFold[file]}")

    else:
        mi.system(f"rm -rf {config['Git']['tempFolder']}/{newrepo}")
        exit()

config = mf.load("config.toml", 1)
repoFold = listdir(f"{config['Git']['tempFolder']}")

if len(repoFold) > 0:
    for i in range(len(repoFold)):
        mi.system(f"rm -rf {config['Git']['tempFolder']}/{repoFold[i]}")
    mf.jsDump("repo.json", [])

def nonLinkStart():
    mi.update()
    mi.aprint("GitArch")
    link = input("\nВведите ссылку: ")
    newrepo = link.split("/")[-1]
    mi.system(f"git clone {link} {config['Git']['tempFolder']}/{newrepo}")
    mainMenu(newrepo)

def linkStart(link):
    mi.update()
    mi.aprint("GitArch")
    newrepo = link.split("/")[-1]
    print("Загрузка репозитория...\n")
    mi.system(f"git clone {link} {config['Git']['tempFolder']}/{newrepo}")
    mainMenu(newrepo)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        linkStart(sys.argv[1])
    else:
        nonLinkStart()