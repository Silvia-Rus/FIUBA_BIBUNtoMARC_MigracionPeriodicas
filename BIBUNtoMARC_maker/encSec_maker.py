from pymarc import Record
from pymarc import Field
from pymarc import Subfield
from gettersSetters.getters import getListaDeCamposEnRegistro, getSubfields
from regex import esElPrimerCaracter, esElUltimoCaracter, borrarElPrimerCaracter, borrarElUltimoCaracter, separarParteEntreSimbolos


class encSec_maker:

	def __init__(self, recordBIBUN, recordMARC):
		self.recordBIBUN = recordBIBUN
		self.recordMARC = recordMARC

	def set650(self):
		F065BIBUNList = getListaDeCamposEnRegistro(self.recordBIBUN, '065')
		for item in F065BIBUNList:
			for sf in item.subfields:
				if esElPrimerCaracter(sf.value, '<') and esElUltimoCaracter(sf.value, '>'):
					text = borrarElPrimerCaracter(sf.value)
					print('text: '+text)
					text = borrarElUltimoCaracter(text)
					print('text: '+text)
					valueList = separarParteEntreSimbolos(text, '><')
					for item in valueList:
						print(item)
						fieldMARC = Field('650', ['#', '#'], [Subfield('a', item)])
						self.recordMARC.add_field(fieldMARC)
				else:
					fieldMARC = Field('650', ['#', '#'], [Subfield('a', sf.value)])
					self.recordMARC.add_field(fieldMARC)
				

	def set710(self):
		F039BIBUNList = getListaDeCamposEnRegistro(self.recordBIBUN, '039')
		for item in F039BIBUNList:
			subfieldsMARC = []
			ind2 = ''
			listSFe = getSubfields(item, 'e')
			listSF9 = getSubfields(item, '9')
			listSFeAnd9 = listSFe + listSF9
			if len(listSF9) > 0:
				ind2 = '2'
				for i, sfE09 in enumerate(listSFeAnd9):
					if i == 0:
						subfieldsMARC.append(Subfield('a', sfE09))
					else:
						subfieldsMARC.append(Subfield('g', 'Otra forma del nombre: '+sfE09))
			for sf in item.subfields:	
				if sf.code == 'e' or sf.code == '9':
					ind2 = '2'
					subfieldsMARC.append(Subfield('a', sf.value))
				elif sf.code == 'n':
					ind2 = '1'
					listSF = separarParteEntreSimbolos(sf.value, '.')
					for i, item in enumerate(listSF):
						if i == 0:
							subfieldsMARC.append(Subfield('a', item+'.'))
						else:
							subfieldsMARC.append(Subfield('b', item))
				elif sf.code == 'l':
					subfieldsMARC.append(Subfield('g', 'Locación: '+sf.value))
				elif sf.code == 's':
					subfieldsMARC.append(Subfield('g', 'Otra forma del nombre: '+sf.value))
			fieldMARC = Field('710', ['#', ind2], subfieldsMARC)
			self.recordMARC.add_field(fieldMARC)

	def addEncSec(self):
		self.set650()
		self.set710()





