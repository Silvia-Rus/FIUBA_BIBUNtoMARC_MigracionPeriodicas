from pymarc import Record
from pymarc import Field
from pymarc import Subfield
from gettersSetters.getters import getListaDeCamposEnRegistro, getSubfields
from regex import esElPrimerCaracter, esElUltimoCaracter, borrarElPrimerCaracter, borrarElUltimoCaracter, separarParteEntreSimbolos


class F6XX7XXencSec_maker:

	def __init__(self, recordBIBUN, recordMARC):
		self.recordBIBUN = recordBIBUN
		self.recordMARC = recordMARC

	def set650(self):
		F065BIBUNList = getListaDeCamposEnRegistro(self.recordBIBUN, '065')
		for item in F065BIBUNList:
			for sf in item.subfields:
				text = sf.value
				text = borrarElPrimerCaracter(text) if esElPrimerCaracter(sf.value, '<') else text
				text = borrarElUltimoCaracter(text) if esElUltimoCaracter(sf.value, '<') else text
				text = borrarElUltimoCaracter(text) if esElUltimoCaracter(sf.value, '>') else text

				valueList = separarParteEntreSimbolos(text, '><')
				for item in valueList:
					fieldMARC = Field('650', ['0', '4'], [Subfield('a', item)])
					self.recordMARC.add_field(fieldMARC)

				# if text != sf.value:
				# 	valueList = separarParteEntreSimbolos(text, '><')
				# 	for item in valueList:
				# 		fieldMARC = Field('650', ['0', '4'], [Subfield('a', item)])
				# 		self.recordMARC.add_field(fieldMARC)
				# else:
				# 	fieldMARC = Field('650', ['0', '4'], [Subfield('a', sf.value)])
				# 	self.recordMARC.add_field(fieldMARC)
				

	def set710(self):
		F039BIBUNList = getListaDeCamposEnRegistro(self.recordBIBUN, '039')
		for item in F039BIBUNList:
			subfieldsMARC = []
			ind1 = '2'
			listSFeBIBUN = getSubfields(item, 'e')
			listSF9BIBUN = getSubfields(item, '9')
			listSFnBIBUN = getSubfields(item, 'n')
			listSFeSF9SFn = listSFeBIBUN + listSF9BIBUN + listSFnBIBUN
			listSFaMARC = []
			listSFbMARC = []

			for i, SFeSF9SFn in enumerate(listSFeSF9SFn):
				if i == 0:
					separateByPoint = separarParteEntreSimbolos(SFeSF9SFn, '.')
					for i, separateByPointItem in enumerate(separateByPoint):
						if i == 0:
							listSFaMARC.append(separateByPointItem)
						else:
							ind1 = '1'
							listSFbMARC.append(separateByPointItem.strip())
				else:
					subfieldsMARC.append(Subfield('g', 'Otra forma del nombre: '+SFeSF9SFn))
			
			if len(listSFaMARC) > 0:
				if len(listSFbMARC) == 0:
					subfieldsMARC.append(Subfield('a', listSFaMARC[0]))
				else:
					subfieldsMARC.append(Subfield('a', listSFaMARC[0]+'.'))
					for i_sfBMARC, sfBMARC in enumerate(listSFbMARC):
						if i_sfBMARC != len(listSFbMARC)-1 and len(listSFbMARC) > 1:
							subfieldsMARC.append(Subfield('b', sfBMARC+'.'))
						else: 
							subfieldsMARC.append(Subfield('b', sfBMARC))
			else:
				fieldMARC = Field('599', [' ', ' '], [Subfield('a', 'Problemas en el 710(MARC). Mirar el 039(BIBUN')])
				self.recordMARC.add_field(fieldMARC)

			for sf in item.subfields:	
				if sf.code == 'l':
					subfieldsMARC.append(Subfield('g', 'Locación: '+sf.value))
				elif sf.code == 's':
					subfieldsMARC.append(Subfield('g', 'Otra forma del nombre: '+sf.value))
			fieldMARC = Field('710', [ind1, ' '], subfieldsMARC)
			self.recordMARC.add_field(fieldMARC)

	def addF6XX7XXencSec(self):
		self.set650()
		self.set710()





