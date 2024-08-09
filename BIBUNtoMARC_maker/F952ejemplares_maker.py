from pymarc import Record
from pymarc import Field
from pymarc import Subfield
from datetime import datetime
from gettersSetters.getters import getListaDeCamposEnRegistro, getSubfieldsFromField
from .diccionarios.ocurrencias import F952p
from .diccionarios.BIBUN091t_MARC952e import BIBUN091t_MARC952e
from .diccionarios.BIBUN091t_MARC952x import BIBUN091t_MARC952x
from regex import borrarString, detectarString

class F952ejemplares_maker:

	def __init__(self, recordBIBUN, recordMARC):
		self.recordBIBUN = recordBIBUN
		self.recordMARC = recordMARC
		self.subfieldsMARC = []

	def getPrimerSF(self, field, subfield):
		listSubfields = getSubfieldsFromField(self.recordBIBUN, field, subfield)
		return listSubfields[0] if len(listSubfields) > 0 else False

	def getSFfrom091(self, SF952):
		value091t = self.getPrimerSF('091', 't')
		diccionario = BIBUN091t_MARC952e if SF952 == 'e' else BIBUN091t_MARC952x
		if not value091t:
			return False
		elif value091t in diccionario:
			return diccionario[value091t]

	def get952o(self):
		retorno = False
		F075c = self.getPrimerSF('075', 'c')
		F0759sinFiltro = self.getPrimerSF('075', 'c')
		if F075c:
			retorno = F075c
		elif F0759sinFiltro :
			retorno = F0759sinFiltro if not detectarString(sf.value, '[err3]') else borrarString(sf.value, '[err3]')
		return retorno

	def set952e(self):
		F952eValue = self.getSFfrom091('e')
		if F952eValue:
			self.subfieldsMARC.append(Subfield('e', F952eValue))
	
	def set952i(self):
		F952iValue = self.getPrimerSF('077', 'a')
		if F952iValue:
			self.subfieldsMARC.append(Subfield('i', F952iValue))

	def set952o(self):
		F952oValue = self.get952o()
		if F952oValue:
			self.subfieldsMARC.append(Subfield('o', F952oValue))

	def set952p(self):
		self.subfieldsMARC.append(Subfield('p', F952p[0]))
		F952p[0] += 1

	def set952r(self):
		F952rvalue = datetime.now().strftime('%Y-%m-%d')
		self.subfieldsMARC.append(Subfield('r', F952rvalue))

	def set952x(self):
		F952xValue = self.getSFfrom091('x')
		if F952xValue:
			self.subfieldsMARC.append(Subfield('x', F952xValue))


	def set952(self):
		self.subfieldsMARC.append(Subfield('0', '0'))
		self.subfieldsMARC.append(Subfield('1', '0'))
		self.subfieldsMARC.append(Subfield('3', '0'))
		self.subfieldsMARC.append(Subfield('7', '0'))
		self.subfieldsMARC.append(Subfield('7', '0'))
		self.subfieldsMARC.append(Subfield('a', 'BC'))
		self.subfieldsMARC.append(Subfield('b', 'BC'))
		self.set952e()
		self.set952i()
		self.set952o()
		self.set952p()
		self.set952r()
		self.set952x()
		self.subfieldsMARC.append(Subfield('y', 'CR'))
		fieldMARC = Field('952', ['#', '#'], self.subfieldsMARC)
		self.recordMARC.add_field(fieldMARC)

	def addF952ejemplares(self):
		self.set952()