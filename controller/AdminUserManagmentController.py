import pymysql
import os

class AdminUserManagementController:
    def __init__(self):
        print('***** Pracujesz w AdminUserManagement Constructor')
        # połączenie z bazą danych
        # obiekt połączenia
        import secret.auth as secret
        try:
            # ukrywanie danych logowania do DB
            self.conn = pymysql.connect(secret.host, secret.user, secret.passwd, secret.db, charset='utf8')
            # print('Pierwszy sukces! Połaczenie z bazą danych zostało ustanowione.')
            # obiekt na ktorym wykonujemy zapytania SQL
            self.c = self.conn.cursor()
        except:
            print('***** Błąd krytyczny!!! Brak połączenia z siecią lub błędne dane logowania do bazy danych.')

    def select(self):
        self.c.execute("SELECT * FROM user")
        wynik = self.c.fetchall()
        print('%3s | %20s | %15s | %15s | %15s | %15s | %1s' % (
        'LP', 'NAZWISKO', 'IMIĘ', 'LOGIN', 'HASłO'.upper(), 'E-MAIL', 'TYP'))
        for row in wynik:
            print('%3i | %20s | %15s | %15s | %15s | %15s | %1s' % (
            row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

    def insert(self):
        try:
            nazwisko = input('Podaj nazwisko nowego użytkownika: \n')
            imie = input('Podaj imię nowego użytkownika: \n')
            login = input('Podaj login nowego użytkownika: \n')
            passwd = input('Podaj jego hasło: \n')
            mail = input('Podaj jego e-mail: \n')
            perm = input('Podaj poziom uprawnień (1-admin, 2-user): \n').upper()
            self.c.execute(
                "insert into user (pracownik_nazwisko, pracownik_imie, login, passwd, email, uprawnienia) values (%s,%s,%s,%s,%s,%s)",
                (nazwisko, imie, login, passwd, mail, perm))
            potwierdzenie = input('Potwierdź wprowadzenie nowego użytkownika T/N').upper()
            if (potwierdzenie == 'T'):
                # potwierdzenie
                self.conn.commit()
                print('Dodano nowego pracownika.')
            else:
                # wycofanie
                self.conn.rollback()
                print('Error! Nowy pracownik nie został dodany do bazy danych.')
            self.select()
        except:
            print('Error! Taki login lub e-mail już istnieje w bazie danych.')

    def delete(self):
        self.select()
        login = input('Podaj login użytkownika, którech chcesz usunąć: ')
        if (login == self.loginAdmin):
            print('Nie możesz usunąć siebie!')
        else:
            self.c.execute("DELETE FROM user WHERE login = %s", (login))
            potwierdzenie = input('Potwierdź usunięcie użytkownika T/N').upper()
            if (potwierdzenie == 'T'):
                # potwierdzenie usunięcia
                self.conn.commit()
                print('Usunięto użytkownika.')
            else:
                # wycofanie
                self.conn.rollback()
                print('Nie uruchomino usuwania.')

    def update(self):
        login = input('Podaj login użytkownika do zmiany hasła: \n')
        passwd = input('Podaj nowe hasło: \n')
        passwd2 = input('Powtórz hasło: \n')
        if (passwd == passwd2):
            self.c.execute("UPDATE user SET passwd = %s WHERE login = %s", (passwd, login))
            # hasło nowe hasło i powtórzone hasło zgodne
            self.conn.commit()
            self.select()
            print('Hasło zostało zmienione.')
        else:
            print('Niepowodzenie - weryfikacja haseł = źle')
            self.select()

    def raport(self):
        from os import getcwd, chdir, listdir
        from time import time
        fileName = input('Podaj nazwę pliku')
        chdir('reports')
        if ((fileName + '.csv') in listdir(getcwd())):
            fileName = fileName + '(' + str(time()) + ')'
        filePath = str(getcwd()) + '\\' + fileName
        file = open(filePath + '.csv', 'w')
        self.c.execute("SELECT * FROM user")
        wynik = self.c.fetchall()
        file.write("Raport został wygenerowany przez któregoś administratora\n")
        file.write('%s;%s;%s;%s;%s\n' % ('LP', 'LOGIN', 'HASłO'.upper(), 'E-MAIL', 'TYP'))
        for row in wynik:
            file.write('%s;%s;%s;%s;%s;%s;%s\n' % (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        chdir('..')
        file.close()



class FileController:
    def __init__(self):
        print("Kontroler plików")

    def writeFile(self, fileName, wordList):
        file = open(fileName, "w")
        file.writelines(wordList)
        file.close()

    def appendFile(self, fileName, wordList):
        file = open(fileName, "a")
        file.writelines(wordList)
        file.close()

    def readFile(self, fileName):
        file = open(fileName, "r")
        # print(file.read())
        for line in file:
            if ('slowo1' in line):
                print(line, end='')
        file.close()

class DirController:
    def __init__(self):
        print("DirController")

    def dirInfo(self, path):
        from os import listdir, chdir
        from os.path import getsize, getatime, getmtime
        from time import gmtime, strftime
        try:
            chdir(path)
            print('%50s | %10s | %30s | %30s' % ("Nazwa", "Rozmiar", "Czas stworzenia", "Czas modyfikacji"))
            for i in listdir(path):
                print('%50s | %10i | %30s | %30s' % (
                    i, getsize(i), strftime('%d-%m-%Y %H:%M:%S', gmtime(getatime(i))), getmtime(i)))
        except:
            print('Error! Błędna ścieżka pliku.')

