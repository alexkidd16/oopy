# coding: utf-8

"""
Código inicial usado na Lista de Exercícios 1 do curso
"Objetos Pythonicos" de Luciano Ramalho, Python.pro.br.
from __future__ import division
"""

class Contador(object):

    def __init__(self):
        self.ocorrencias = {}

    def incrementar(self, item):
        qtd = self.ocorrencias.get(item, 0) + 1
        self.ocorrencias[item] = qtd

    def contagem(self, item):
        return self.ocorrencias[item]



class ContadorAmigavel(Contador):

	def contagem(self, item):
		try:
			return self.ocorrencias[item]
		except Exception, e:
			return 0

class ContadorTotalizador(Contador):

	def __init__(self):
		Contador.__init__(self)
		self.total = 0

	def incrementar(self, item):
		Contador.incrementar(self, item)
		self.total += 1

	def porcentagem(self, item):
		porc = self.contagem(item)/float(self.total) * 100.0
		return round(porc,1)


class ContadorTotalizadorAmigavel(ContadorAmigavel, ContadorTotalizador): 
		""" 
			Contador Totalizador Amigavel
		"""

