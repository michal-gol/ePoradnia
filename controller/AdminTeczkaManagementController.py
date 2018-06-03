import pymysql
import os

class AdminTeczkaManagementController:
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

    def teczkaWypisz(self):
        self.c.execute("SELECT nazwisko_ucznia, imie_ucznia, data_ur_ucznia FROM teczki;")
        wynik = self.c.fetchall()
        print('***** Lista teczek\n%20s | %15s | %15s' % (
        'NAZWISKO', 'IMIĘ', 'DATA UR'))
        for row in wynik:
            print("%20s | %15s | %15s" % (
            row[0], row[1], row[2],))

    def teczkaDodaj(self):
        try:
            nazwiskoUcznia = input('Podaj nazwisko ucznia: \n')
            imieUcznia = input('Podaj imię ucznia: \n')
            dataUr = input('Podaj datę urodzenia rrrr-mm-dd: \n')
            #nrTeczki = input('Podaj numer teczki nadany w Baza3P: \n')
            #rokTeczki = input('Podaj rok szkolny\n')
            self.c.execute(
                "insert into teczki (nazwisko_ucznia, imie_ucznia, data_ur_ucznia) values (%s,%s,%s)",
                (nazwiskoUcznia, imieUcznia, dataUr))
            potwierdzenie = input('Potwierdź wprowadzenie nowej teczki T/N').upper()
            if (potwierdzenie == 'T'):
                # potwierdzenie
                self.conn.commit()
                print('Dodano nową teczkę.')
            else:
                # wycofanie
                self.conn.rollback()
                print('Error! Nowa teczka nie została dodana do bazy danych.')
                self.teczkaWypisz()
        except:
            print('Error! Taki login lub e-mail już istnieje w bazie danych.')

    # def teczkaUsun(self):
    #     self.teczkaWypisz()
    #     login = input('Podaj login użytkownika, którech chcesz usunąć: ')
    #     if (login == self.loginAdmin):
    #         print('Nie możesz usunąć siebie!')
    #     else:
    #         self.c.execute("DELETE FROM user WHERE login = %s", (login))
    #         potwierdzenie = input('Potwierdź usunięcie użytkownika T/N').upper()
    #         if (potwierdzenie == 'T'):
    #             # potwierdzenie usunięcia
    #             self.conn.commit()
    #             print('Usunięto użytkownika.')
    #         else:
    #             # wycofanie
    #             self.conn.rollback()
    #             print('Nie uruchomino usuwania.')

    def teczkaZmien(self):
        nrTeczki1 = int(input('Podaj numer teczki, którą chcesz zmodyfikować: \n'))
        nrTeczki2 = int(input('Weryfikacja: ponownie podaj numer teczki, którą chcesz zmodyfikować: \n'))
        if (nrTeczki1 == nrTeczki2):
            nazwiskoUcznia = input('Podaj nazwisko ucznia: \n')
            imieUcznia = input('Podaj imię ucznia: \n')
            dataUr = input('Podaj datę urodzenia rrrr-mm-dd: \n')
            self.c.execute("UPDATE teczki SET nazwisko_ucznia='%s', imie_ucznia='%s', data_ur_ucznia='%s' WHERE idteczki='%s';"
                           % (nazwiskoUcznia, imieUcznia, dataUr, nrTeczki1))
            self.conn.commit()
            self.c.execute("SELECT nazwisko_ucznia, imie_ucznia, data_ur_ucznia FROM teczki WHERE idteczki = %s" % (nrTeczki1))
            wynik = self.c.fetchall()
            print('***** Zmieniono dane następujacej teczki\n%20s | %15s | %15s' % (
                'NAZWISKO', 'IMIĘ', 'DATA UR'))
            for row in wynik:
                print("%20s | %15s | %15s" % (
                    row[0], row[1], row[2],))
            print('Hasło zostało zmienione.')
        else:
            print('***** Niepowodzenie - numer teczki nie został wskazany jednoznacznie')

    def teczkaSzukajStr(self):
        imie = input("Podaj imię LUB nazwisko szukanego ucznia: \n")
        self.c.execute("SELECT nazwisko_ucznia, imie_ucznia, data_ur_ucznia FROM teczki WHERE imie_ucznia = '%s' OR nazwisko_ucznia = '%s';" % (imie,imie))
        wynik = self.c.fetchall()
        print('***** Lista teczek\n%20s | %15s | %15s' % (
        'NAZWISKO', 'IMIĘ', 'DATA UR'))
        for row in wynik:
            print("%20s | %15s | %15s" % (
            row[0], row[1], row[2],))

    def teczkaSzukajDat(self):
        data = input("Podaj datę urodzenia szukanego ucznia: \n")
        self.c.execute("SELECT nazwisko_ucznia, imie_ucznia, data_ur_ucznia FROM teczki WHERE data_ur_ucznia = '%s';" % (data))
        wynik = self.c.fetchall()
        print('***** Lista teczek\n%20s | %15s | %15s' % (
        'NAZWISKO', 'IMIĘ', 'DATA UR'))
        for row in wynik:
            print("%20s | %15s | %15s" % (
            row[0], row[1], row[2],))

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

