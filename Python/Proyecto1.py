#construirás un juego donde la computadora tiene que adivinar el número correcto.

from random import Random


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
        self.__obtenerNum
        self.__comprobarNum
        
    def obtenerNum(self) -> int:
        return Random.randint(1,10)

    def comprobarNum(self):
        if(self.num == self.numWin):
            self.winner = True
        else:
            output.showMensage("Casi pero no ....",True)

    def start(self): 
        self.winner= False   
        
        output.showMensage("Adivina el numero que estoy pensando del 1-10",True)

        output.showMensage("Se inicia el juego ....",False)
        
        self.numwin = self.__obtenerNum

        inputs.pedirNum(self,"Dame tu primer numero : ")

        while(self.winner == False):
            self.__comprobarNum(self)
            inputs.pedirNum(self,"Dame otro numero a ver si ahora si lo adivinas : ")
        
        output.showMensage("Has ganado !!!")
    
    __obtenerNum = obtenerNum

    __comprobarNum = comprobarNum

        
game = gameNumber()
game.start()
