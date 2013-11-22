from random import shuffle
from collections import Iterable

class Tombola(Iterable, object ):
    '''Sorteia itens sem repetir'''

    def carregar(self, seq):
        self.itens = list(seq)

    def misturar(self, misturadora= None):
    	shuffle(self.itens) if misturadora is None else misturadora(self.itens)

    def sortear(self):
        return self.itens.pop()

    def carregada(self):
        return bool(self.itens)

    def __iter__(self):
        for i in reversed(self.itens):
        	yield i