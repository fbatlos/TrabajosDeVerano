import random

class inputs:
    def __init__(self):
        self.num = 0
        self.nombre = ""
        self.letra = ""
        self.__pedirNum
        self.__pedirNombre
        self.__pedirLetra

    def pedirNum(self,text):
        self.num = input(text)
    __pedirNum = pedirNum

    def pedirLetra(self,text):
        self.letra = input(text)
    __pedirLetra = pedirLetra

    def pedirNombre(self,text):
        self.nombre = input(text)
    __pedirNombre = pedirNombre

class output:

    def showMensage(text , bool):
        if(bool == True):
            print("         ")
            print(text)
        else:
            print(text)
    



class tablero():
    def __init__(self):
        output.showMensage("el juego comienza",True)
        self.tablero = []
        for columna in range(0,4):
            self.tablero.append([])
            for fila in range(0,8):
                self.tablero[columna].append("")
       
    
    def comprobarInput(self , num:int , letra:str):
        
        if(int(num) in range(1,3)):
            posX = ["A","B","C","D","E","F","G","H"].index(letra)
            player.colocarMarca(self,int(num),posX)
        else:
            raise ValueError        
        
        
        
    

class player():
    def __init__(self,tablero:tablero):
        self.__nombre = inputs.pedirNombre(self,"Dime tu nombre : ")
        self.__tablero = tablero
        
    def colocarBarcos(self):
        contadorDeBarcos = 0

        while(contadorDeBarcos <10):
            contadorDeBarcos = 0
            columna = random.randint(0,3)
            fila = random.randint(0,7)

            match(random.randint(1,2)):
                case 1:
                    self.__tablero.tablero = barcos.barcoDeUno(self.__tablero.tablero,fila,columna)
                    
                    for filas in self.__tablero.tablero:
                        contadorDeBarcos += filas.count("X") 
                    
                case 2:
                    self.__tablero.tablero = (barcos.barcoDeDos(self.__tablero.tablero,fila,columna))
                    for filas in self.__tablero.tablero:
                        contadorDeBarcos += filas.count("X") 
    
    def colocarMarca(self,posY,posX):
        if(self.__tablero.tablero[posY][posX] == ""):
            self.__tablero.tablero[posY][posX]="O"
        elif(self.__tablero.tablero[posY][posX] == "X"):
            self.__tablero.tablero[posY][posX]="T"
        else:
            output.showMensage("Posiciones nos validas.",True)
class barcos:

    def barcoDeUno(tablero:list,posX,posY):
        if(tablero[posY][posX] == ""):
            tablero[posY][posX]="X"
            return tablero
        return tablero
    
    def barcoDeDos(tablero:list,posX , posY):
        if(tablero[posY][posX] == ""):
            if(posX+1 < 8 and tablero[posY][posX+1] == ""):
                tablero[posY][posX] = "X"
                tablero[posY][posX+1]= "X"

                return tablero
            elif( posY+1<4  and tablero[posY+1][posX] == ""):
                tablero[posY][posX] = "X"
                tablero[posY+1][posX]= "X"
                
                return tablero
            else:
                return tablero    
        else:
            return tablero

class mostrar:
    def __init__(self,tableroActual:list):
        self.__tableroActual=tableroActual
        self.comparaTablero = ""
        self.__compararTablero
        

    def mostrarTablero(self):
        index = 1
        output.showMensage("|---A---|---B---|---C---|---D---|---E---|---F---|---G---|---H---|",True)
        tableroAMostrar = []
        for columna in range(0,4):
            tableroAMostrar.append([])
            for fila in range(0,8):
                tableroAMostrar[columna].append(self.__compararTablero(columna,fila))
        

        for i in tableroAMostrar:
            output.showMensage(str(index)+"|---"+i[0]+"---|---"+i[1]+"---|---"+i[2]+"---|---"+i[3]+"---|---"+i[4]+"---|---"+i[5]+"---|---"+i[6]+"---|---"+i[7]+"---|",False)
            index+=1 

    def compararTablero(self,columna,fila):
        if(self.__tableroActual[columna][fila] != "X"):
            return self.__tableroActual[columna][fila]
        else:
            return ""
    
    __compararTablero = compararTablero


wninner =False
tablero1 = tablero()

consola = inputs()

jugador = player(tablero1)
jugador.colocarBarcos()

ver = mostrar(tablero1.tablero)


while(wninner == False):
    try:
        ver.mostrarTablero()
        consola.pedirLetra("Dame la letra: ")
        consola.pedirNum("Dame un numero: ")

        print(consola.num)


        tablero1.comprobarInput(consola.num,consola.letra)

    except ValueError:
            output.showMensage("Datos no validos",True)