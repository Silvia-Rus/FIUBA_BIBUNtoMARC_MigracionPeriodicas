
from ..diccionarios.ocurrencias001 import ocurrencias001
from datetime import datetime
from gettersSetters.setters import setCF001, setCF003, setCF005
from gettersSetters.getters import getSubfieldsFromField

class LDRtoCF005_maker:

	def __init__(self, recordMARC):
		self.recordMARC = recordMARC
		self.LDR = '     nas a22     7a 4500'
		self.CF001 = '0'
		self.CF003 = 'AR-BaUFI'
		self.CF005 = 'aaaammddhhmmss.f'
	  
	def __str__(self):
		retorno = 'LDR = ' + self.LDR + '\n' 
		retorno += '001 = ' + self.CF001 + '\n'
		retorno += '003 = ' + self.CF003 + '\n'
		retorno += '005 = ' + self.CF005 + '\n'
		return retorno

	def addLDR(self):
		self.recordMARC.leader = self.LDR

	def addCF001(self):
		self.CF001 = ocurrencias001[0]
		ocurrencias001[0] = self.CF001+1
		setCF001(self.recordMARC, str(self.CF001))
		# F931a = getSubfieldsFromField(self.recordBIBUN, '098', 'a')
		# print(len(F931a))
		# setCF001(self.recordMARC, F931a[0])

	def addCF003(self): 
		setCF003(self.recordMARC, self.CF003)

	def addCF005(self):
		fechaActual = datetime.now()
		fechaActualConFormato = fechaActual.strftime('%Y%m%d%H%M%S.%f')[:-5]
		setCF005(self.recordMARC, fechaActualConFormato)

	def addLDRtoCF005(self):
		self.addLDR()
		self.addCF001()
		self.addCF003()
		self.addCF005()






