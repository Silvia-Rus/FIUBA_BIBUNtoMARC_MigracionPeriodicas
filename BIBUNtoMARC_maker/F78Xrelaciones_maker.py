from pymarc import Record
from pymarc import Field
from pymarc import Subfield
from gettersSetters.getters import getListaDeCamposEnRegistro, getSubfields
from .diccionarios.BIBUN057r_MARC780ind2 import BIBUN057r_MARC780ind2
from .diccionarios.BIBUN058r_MARC785ind2 import BIBUN058r_MARC785ind2
from regex import borrarString, detectarString, quitarTilde


class F78Xrelaciones_maker:

	def __init__(self, recordBIBUN, recordMARC):
		self.recordBIBUN = recordBIBUN
		self.recordMARC = recordMARC
		self.F786o = Field('786', ['1', '9'], [Subfield('o','AIG')])


	def set78X(self, tagField):
		fieldBIBUN = '057' if tagField == '780' else '058'
		list04XBIBUN = getListaDeCamposEnRegistro(self.recordBIBUN, fieldBIBUN)
		ind2 = '#'
		for item in list04XBIBUN:
			subfieldsMARC = []
			listSFrBIBUN = getSubfields(item, 'r')
			listSFtBIBUN = getSubfields(item, 't')
			listSFiBIBUN = getSubfields(item, 'i')
			listSFiMARC = [];
			listSFtMARC = [];
			listSFxMARC = [];
			if len(listSFrBIBUN) == 0 and len(listSFtBIBUN) == 2:
				ind2 = self.setInd2(tagField, quitarTilde(listSFtBIBUN[0]))
				listSFtMARC.append(Subfield('t', listSFtBIBUN[1]))
			elif len(listSFrBIBUN) > 0 and len(listSFtBIBUN) > 0:
				ind2 = self.setInd2(tagField, quitarTilde(listSFrBIBUN[0]))
				for sfT in listSFtBIBUN:
					listSFtMARC.append(Subfield('t', sfT))
				for sfR in listSFrBIBUN:
					listSFiMARC.append(Subfield('i', sfR))

			for sfI in listSFiBIBUN:
				valueSinISSN = sfI if not detectarString(sfI, 'ISSN') else borrarString(sfI, 'ISSN ')
				value = valueSinISSN if not detectarString(valueSinISSN, 'y ') else borrarString(valueSinISSN, 'y ')
				listSFxMARC.append(Subfield('x', value))
					
			for index, SFtMARC in enumerate(listSFtMARC):
				subfieldsMARC = listSFiMARC + [SFtMARC] 
				if index <= len(listSFxMARC)-1:
					subfieldsMARC += [listSFxMARC[index]]
				print("Formando el Field: "+str(ind2))
				fieldMARC = Field(tagField, ['0', ind2], subfieldsMARC)
				self.recordMARC.add_field(fieldMARC)

	def setInd2(self, tagField, texto):
		retorno = ' '
		diccionario = BIBUN057r_MARC780ind2 if tagField == '780' else BIBUN058r_MARC785ind2
		if texto in diccionario:
			retorno = diccionario[texto]
		else:
			fieldMARC = Field(599, [' ', ' '], [Subfield('i', 'Problema en en'+tagField+'ind2. El contenido del'+tagField+'i es confuso o inexistente. Consultar la fuente.')])
			self.recordMARC.add_field(fieldMARC)
		return retorno

	def set780(self):
		self.set78X('780')

	def set785(self):
		self.set78X('785')

	def addF78Xrelaciones(self):
		self.set780()
		self.set785()
		self.recordMARC.add_field(self.F786o)
