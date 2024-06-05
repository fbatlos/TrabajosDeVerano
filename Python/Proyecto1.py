#construirás un juego donde la computadora tiene que adivinar el número correcto.

import random


class inputs:
    def __init__(self):
        self.num = 0
        self.__pedirNum

    def pedirNum(self,text):
        self.num = input(text)
    __pedirNum = pedirNum


class output:

    def showMensage(text , bool):
        if(bool == True):
            print("         ")
            print(text)
        else:
            print(text)


class gameNumber(inputs , output):

    def __init__(self):
       
        self.__comprobarNum

    def comprobarNum(self,numwin):
        try:
            if(int(self.num) == numwin):
                return True
            else:
                output.showMensage("Casi pero no ....",True)
                return False
        except ValueError:
            output.showMensage("No puedes meter letras",True)
            return False
        

    def start(self): 
        winner= False   
        
        output.showMensage("Adivina el numero que estoy pensando del 1-10",True)

        output.showMensage("Se inicia el juego ....",False)
        
        numwin = random.randint(0, 10)

        inputs.pedirNum(self,"Dame tu primer numero : ")

        while(winner == False):
            winner = self.__comprobarNum(numwin)
            if(winner == False):
                inputs.pedirNum(self,"Dame otro numero a ver si ahora si lo adivinas : ")
        
        output.showMensage("Has ganado !!!",True)


    __comprobarNum = comprobarNum

        
game = gameNumber()
game.start()
