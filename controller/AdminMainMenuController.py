from controller.AdminUserManagmentController import *
from controller.AdminTeczkaManagementController import *

class AdminMainMenuController:
    def __init__(self):
        print('***** Pracujesz w AdminMainMenuController Constructor')

    def AdminMainMenu(self):
        print('***** Menu administratora')
        while (True):
            decyzja = input(
                "***** Co chcesz zrobić:\n[1]\t\t- zarządzanie użytkownikami,\n[2]\t\t- zarządzanie teczkami uczniów,\n[3]\t\t- zarządzanie pismami (eKancelaria, JRWA),\n[Ex]it\t- wyjście z programu.\n").upper()
            if (decyzja == '1'):
                self.userManagement()
            elif (decyzja == '2'):
                self.teczkaManagement()
            elif (decyzja == '3'):
                self.pismaManagement()
            elif (decyzja == 'EX'):
                print('***** Bye, bye!')
                print(exit())
            else:
                print('***** Error! Wybierz inną opcję.')

    def userManagement(self):
        print('***** Rozpoczynasz pracę w userManagement')
        while (True):
            decyzja = input(
                "***** Co chesz zrobić:\n[1]\t- wylistuj użytkowników,\n[2]\t- dodaj użytkownika,\n[3]\t- zmiana hasła dowolnego użytkownika,\n[4]\t- usuń innego użytkownika,\n[5]\t- rzut danych o użytkownikach do pliku,\n[Q]uit\t\t- wyjście do głównego menu,\n[Ex]it\t\t- wyjście z programu.\n").upper()
            if (decyzja == '1'):
                aumc = AdminUserManagementController()
                aumc.select()
            elif (decyzja == '2'):
                aumc = AdminUserManagementController()
                aumc.insert()
            elif (decyzja == '3'):
                aumc = AdminUserManagementController()
                aumc.delete()
            elif (decyzja == '4'):
                aumc = AdminUserManagementController()
                aumc.update()
            elif (decyzja == '5'):
                aumc = AdminUserManagementController()
                aumc.raport()
            elif (decyzja == 'Q'):
                print('Wyjście poziom wyzej')
                self.AdminMainMenu()
            elif (decyzja == 'EX'):
                print('***** Bye, bye!')
                print(exit())
            else:
                print('***** Błędny wybór między [S]elect a [Q]uit. Podaj właściwy znak.')

    def teczkaManagement(self):
        print('***** Rozpoczynasz pracę w teczkaManagement')
        while (True):
            decyzja = input(
                "***** Co chesz zrobić:\n[1]\t- dodaj nową teczkę\n[2]\t- wypisz istniejące teczki\n[3]\t- zmień dane teczki\n[4]\t- szukaj teczki (imie, nazwisko)\n[5]\t- szukaj teczki (data urodzenia)\n[Q]uit\t\t- wyjście do głównego menu,\n[Ex]it\t\t- wyjście z programu.\n").upper()
            if (decyzja == '1'):
                atmc = AdminTeczkaManagementController()
                atmc.teczkaDodaj()
            elif (decyzja == '2'):
                atmc = AdminTeczkaManagementController()
                atmc.teczkaWypisz()
            elif (decyzja == '3'):
                atmc = AdminTeczkaManagementController()
                atmc.teczkaZmien()
            elif (decyzja == '4'):
                atmc = AdminTeczkaManagementController()
                atmc.teczkaSzukajStr()
            elif (decyzja == '5'):
                atmc = AdminTeczkaManagementController()
                atmc.teczkaSzukajDat()
            elif (decyzja == 'Q'):
                print('Wyjście poziom wyzej')
                self.AdminMainMenu()
            elif (decyzja == 'EX'):
                print('***** Bye, bye!')
                print(exit())
            else:
                print('***** Błędny wybór między [S]elect a [Q]uit. Podaj właściwy znak.')

    def pismaManagement(self):
        print('***** Rozpoczynasz pracę w pismaManagement')
        while (True):
            decyzja = input(
                "***** Co chesz zrobić:\n[P]\t\t- Zarejstruj pismo przychodzące\n[W]\t\t- Zarejestruj pismo wychodzące\n[S]\t\t- Szukaj pisma wg słowa kluczowego\n[Q]uit\t- wyjście do głównego menu,\n[Ex]it\t- wyjście z programu.\n").upper()
            if (decyzja == 'S'):
                # self.metoda()
                continue
            elif (decyzja == 'I'):
                # self.metoda()
                continue
            elif (decyzja == 'D'):
                # self.metoda()
                continue
            elif (decyzja == 'U'):
                # self.metoda()
                continue
            elif (decyzja == 'R'):
                # self.metoda()
                continue
            elif (decyzja == 'Q'):
                print('***** Wyjście poziom wyzej')
                self.AdminMainMenu()
            elif (decyzja == 'EX'):
                print('***** Bye, bye!')
                print(exit())
            else:
                print('***** Błędny wybór między [S]elect a [Q]uit. Podaj właściwy znak.')