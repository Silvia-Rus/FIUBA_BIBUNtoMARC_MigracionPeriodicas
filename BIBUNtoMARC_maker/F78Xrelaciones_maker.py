from pymarc import Record
from pymarc import Field
from pymarc import Subfield
from gettersSetters.getters import getListaDeCamposEnRegistro, getSubfields
from .diccionarios.BIBUN057r_MARC780ind2 import BIBUN057r_MARC780ind2
from .diccionarios.BIBUN058r_MARC785ind2 import BIBUN058r_MARC785ind2
from regex import borrarString, detectarString, quitarTilde, borrarCaracteresLuegoDeISSN


class F78Xrelaciones_maker:

	def __init__(self, recordBIBUN, recordMARC):
		self.recordBIBUN = recordBIBUN
		self.recordMARC = recordMARC
		self.F786o = Field('786', [' ', ' '], [Subfield('o','AIG')])

	def set78X(self, tagField):
		fieldBIBUN = '057' if tagField == '780' else '058'
		listSf05XBIBUN = getListaDeCamposEnRegistro(self.recordBIBUN, fieldBIBUN)
		diccionario = BIBUN057r_MARC780ind2 if tagField == '780' else BIBUN058r_MARC785ind2

		print('len 05X: '+str(len(listSf05XBIBUN)))
		ind2 = '#'
		for item in listSf05XBIBUN: # nivel campo
			fields = []
			subfieldsMARC = []
			listSFrBIBUN = getSubfields(item, 'r')
			listSFtBIBUN = getSubfields(item, 't')
			# listSFiBIBUN = getSubfields(item, 'i')
			listSFiMARC = [];
			listSFtMARC = [];
			listSFxMARC = [];

			#indicadores 
			if len(listSFrBIBUN) == 0 and len(listSFtBIBUN) == 2:
				ind2 = self.setInd2(tagField, quitarTilde(listSFtBIBUN[0]))
			elif len(listSFrBIBUN) > 0 and len(listSFtBIBUN) > 0:
				ind2 = self.setInd2(tagField, quitarTilde(listSFrBIBUN[0]))
			
			for i, sc in enumerate(item.subfields):
				if i == 0 and quitarTilde(sc.value) in diccionario:
					listSFiMARC.append(Subfield('i', sc.value))
				elif sc.code =='t' and quitarTilde(sc.value) not in diccionario:
					listSFtMARC.append(Subfield('t', sc.value))	
				if sc.code =='i':
					listSFxMARC.append(Subfield('x',borrarCaracteresLuegoDeISSN(sc.value)))
				
				if len(listSFtMARC) > 0 and ((i < len(item.subfields)-1 and item.subfields[i+1].code == 't') or i == len(item.subfields)-1):
					fieldMARC = Field(tagField, ['0', ind2],listSFiMARC + listSFtMARC +listSFxMARC)
					self.recordMARC.add_field(fieldMARC)
					listSFtMARC = []
					listSFxMARC = []


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
