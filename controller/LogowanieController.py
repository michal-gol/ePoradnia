import pymysql
from controller.AdminMainMenuController import *
from controller.AdminUserManagmentController import *
from controller.UserMainMenuController import *

class UserController:
    def __init__(self):
        print('***** Pracujesz w User Controller Constructor')
        u = Logowanie()

# połączenie z bazą danych
class DBController:
    def __init__(self):
        print('***** Pracujesz w DBController')
        # obiekt połączenia
        import secret.auth as secret
        try:
            # ukrywanie danych logowania do DB
            self.conn = pymysql.connect(secret.host, secret.user, secret.passwd, secret.db, charset='utf8')
            print('***** Pierwszy sukces! Połaczenie z bazą danych zostało ustanowione.')
            # obiekt na ktorym wykonujemy zapytania SQL
            self.c = self.conn.cursor()
        except:
            print('***** Błąd krytyczny!!! Brak połączenia z siecią lub błędne dane logowania do bazy danych.')

    def logowanie(self):
        self.a=3
        while self.a:
            login=input('Podaj login: ')
            passwd=input('Podaj hasło: ')
            #login="Admin"
            #passwd="Admin1"
            self.c.execute("SELECT * FROM user WHERE login = %s AND passwd = %s", (login, passwd))
            self.login=login
            self.loginAdmin=login
            self.passwd=passwd
            wynik=self.c.fetchall()
            if(len(wynik)>0):
                if(wynik[0][6] == "1"):
                    self.login='%'
                    self.passwd='%'
                    print('***** Zalogowałeś się. Uprawnienia administratora przyzne. Witaj '+login+'!')
                    while (True):
                        ammc = AdminMainMenuController()
                        ammc.AdminMainMenu()
                else:
                    print('*****  Zalogowałeś się jako user.')
                    while(True):
                        ummc = UserMainMenuController()
                        ummc.UserMainMenu()
            else:
                print("***** Błędne dane logowania. Masz łącznie 3 próby logowania.")
                self.a-=1
