from pymarc import Record
from pymarc import Field
from pymarc import Subfield
from gettersSetters.getters import getListaDeCamposEnRegistro, getSubfields
from .diccionarios.BIBUN057r_MARC780ind2 import BIBUN057r_MARC780ind2
from .diccionarios.BIBUN058r_MARC785ind2 import BIBUN058r_MARC785ind2

class F78Xrelaciones_maker:

	def __init__(self, recordBIBUN, recordMARC):
		self.recordBIBUN = recordBIBUN
		self.recordMARC = recordMARC
		self.F786o = Field('780', ['#', '#'], [Subfield('o','AIG')])


	def set78X(self, tagField):
		fieldBIBUN = '057' if tagField == '780' else fieldBIBUN = '058'
		list04XBIBUN = getListaDeCamposEnRegistro(self.recordBIBUN, fieldBIBUN)
		ind2 = '#'
		for item in list04XBIBUN:
			subfieldsMARC = []
			listSFr = getSubfields(item, 'r')
			listSFt = getSubfields(item, 't')
			if len(listSFr) == 0 and len(listSFt) == 2:
				ind2 = self.setInd2(tagField, listSFt[0])
				subfieldsMARC.append(Subfield('t', listSFt[1]))
			elif len(listSFr) > 0 and len(listSFt) > 0::
				ind2 = self.setInd2(tagField, listSFr[0])
				subfieldsMARC.append(Subfield('t', listSFt[0]))
			for sf in item.subfields:
				if sf.code == 'r':
					subfieldsMARC.append(Subfield('i', sf.value))
				elif sf.code == 'i':
					subfieldsMARC.append(Subfield('x', sf.value))
			fieldMARC = Field(tagField, ['0', ind2], subfieldsMARC)
			self.recordMARC.add_field(fieldMARC)

	def setInd2(self, tagField, texto):
		retorno = '#'
		diccionario = BIBUN057r_MARC780ind2 if tagField == '780' else BIBUN058r_MARC785ind2
		if texto in diccionario:
			retorno = diccionario[texto]
		return retorno

	def set780(self):
		self.set78X('780')

	def set785(self):
		self.set78X('785')

	def addF78Xrelaciones(self):
		self.set780()
		self.set785()
		self.recordMARC.add_field(self.F786o)
