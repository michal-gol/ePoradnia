from controller.LogowanieController import *

class Run:
    def __init__(self):
        dbc=DBController()
        dbc.logowanie()
Run()