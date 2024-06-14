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
        return input(text)
    __pedirNombre = pedirNombre

class output:

    def showMensage(text , bool):
        if(bool == True):
            print("         ")
            print(text)
        else:
            print(text)
    



class Tablero():
    def __init__(self):
        output.showMensage("El juego comienza  ",True)
        self.tablero =  [["" for _ in range(8)] for _ in range(4)]       
    
    def comprobarInput(self, num: int, letra: str, player):
        try:
            num = int(num)
        except ValueError:
            raise ValueError("El número debe ser un entero.")

        if num in range(1, 5):
            posX = ["A", "B", "C", "D", "E", "F", "G", "H"]
            if letra.upper() in posX:
                posY = num - 1
                posX_index = posX.index(letra.upper())
                player.colocarMarca(posY, posX_index)
            else:
                raise ValueError("Letra fuera de rango.")
        else:
            raise ValueError("Número fuera de rango.")     

    def comprobarGanador(self):
        for filas in self.tablero:
            if(filas.__contains__("X")):
                return False
        return True

class Player():
    def __init__(self,tablero:Tablero):
        self.nombre = inputs.pedirNombre(self,"Dime tu nombre : ")
        self.tableroClass = tablero
        self.comprobarMarca
        
    def colocarBarcos(self):
        contadorDeBarcos = 0

        while(contadorDeBarcos <=10):
            contadorDeBarcos = 0
            columna = random.randint(0,3)
            fila = random.randint(0,7)

            match(random.randint(1,2)):
                case 1:
                    self.tableroClass.tablero = Barcos.barcoDeUno(self.tableroClass.tablero,fila,columna)
                    
                case 2:
                    self.tableroClass.tablero = (Barcos.barcoDeDos(self.tableroClass.tablero,fila,columna))
                    
            for filas in self.tableroClass.tablero:
                contadorDeBarcos += filas.count("X")

    def colocarMarca(self, posY, posX):
        if posY < 0 or posY >= len(self.tableroClass.tablero) or posX < 0 or posX >= len(self.tableroClass.tablero[0]):
            output.showMensage("Posiciones no válidas.", True)
            return
        
        if self.tableroClass.tablero[posY][posX] == "":
            self.tableroClass.tablero[posY][posX] = "O"

            output.showMensage("Fue agua mi capitán .",True)
        elif self.tableroClass.tablero[posY][posX] == "X":
            self.tableroClass.tablero[posY][posX] = "T"
            self.comprobarMarca(posY,posX)
            
        else:
            output.showMensage("Posiciones no válidas.", True)


    def comprobarMarca(self , posY , posX):
        barcoTocado = False
        if(posY == 0):
            if (self.tableroClass.tablero[1][posX] == "X"):
                output.showMensage("Se ha tocado barco "+self.nombre , True)
                barcoTocado = True
            if(posX == 0 ):
                if (self.tableroClass.tablero[posY][1] == "X"):
                    output.showMensage("Se ha tocado barco "+self.nombre , True)
                    barcoTocado = True
            elif (posX == 7):
                if (self.tableroClass.tablero[posY][6] == "X"):
                    output.showMensage("Se ha tocado barco "+self.nombre , True)
                    barcoTocado = True
            else:
                if (self.tableroClass.tablero[posY][posX+1] == "X"):
                    output.showMensage("Se ha tocado barco "+self.nombre , True)
                    barcoTocado = True
                if (self.tableroClass.tablero[posY][posX-1] == "X"):
                    output.showMensage("Se ha tocado barco "+self.nombre , True)
                    barcoTocado = True

        elif(posY == 3):
            if (self.tableroClass.tablero[2][posX] == "X"):
                output.showMensage("Se ha tocado barco "+self.nombre , True)
                barcoTocado = True
            if(posX == 0 ):
                if (self.tableroClass.tablero[posY][1] == "X"):
                    output.showMensage("Se ha tocado barco "+self.nombre , True)
                    barcoTocado = True
            elif (posX == 7):
                if (self.tableroClass.tablero[posY][6] == "X"):
                    output.showMensage("Se ha tocado barco "+self.nombre , True)
                    barcoTocado = True
            else:
                if (self.tableroClass.tablero[posY][posX+1] == "X"):
                    output.showMensage("Se ha tocado barco "+self.nombre , True)
                    barcoTocado = True
                if (self.tableroClass.tablero[posY][posX-1] == "X"):
                    output.showMensage("Se ha tocado barco "+self.nombre , True)
                    barcoTocado = True

        elif(posY != 0 and posY!=3 and posX!= 0 and posX!= 7):
            if (self.tableroClass.tablero[posY+1][posX] == "X"):
                output.showMensage("Se ha tocado barco "+self.nombre , True)
                barcoTocado = True
            if (self.tableroClass.tablero[posY-1][posX] == "X"):
                output.showMensage("Se ha tocado barco "+self.nombre , True)
                barcoTocado = True
            if (self.tableroClass.tablero[posY][posX+1] == "X"):
                output.showMensage("Se ha tocado barco "+self.nombre , True)
                barcoTocado = True
            if (self.tableroClass.tablero[posY][posX-1] == "X"):
                output.showMensage("Se ha tocado barco "+self.nombre , True)
                barcoTocado = True

        if(barcoTocado==False):
            output.showMensage(self.nombre+" has undido un barco enemigo ." ,True)



class Barcos:

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


winner =False
tablero1 = Tablero()

consola = inputs()

jugador = Player(tablero1)
jugador.colocarBarcos()

ver = mostrar(tablero1.tablero)

ronda = 1

while(winner == False):

    output.showMensage("Ronda : "+ str(ronda) +"  /  Jugador : " + jugador.nombre , True)

    try:
        ver.mostrarTablero()
        consola.pedirLetra("Dame la letra: ")
        consola.pedirNum("Dame un numero: ")

        tablero1.comprobarInput(consola.num,consola.letra,jugador)

        winner = tablero1.comprobarGanador()
        ronda += 1
    except ValueError as e:
            output.showMensage(str(e),True)

output.showMensage("Has ganado " + jugador.nombre + " , eres de lo mejor.",True)
