class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   

class Dropping():
    def __init__(self,posicion):
        self.items_list = self.items_list
        self.__drop(posicion)

    def drop(self  , posicion ):
        self.items_list.remove(posicion)

class MappingSubclass( Mapping,Dropping):

    def update(self, values):
        for item in values:
            self.items_list.append(item)

    def drop(self, posicion):
        return super().drop( posicion)
    

import random
# ¿Quién comienza?
comienza = random.randint(0, 1)
if comienza == 0:
    print('Comienza el jugador')
else:
    print('Comienza el PC')
# Número aleatorio del parchís
numero = random.randint(1, 6)