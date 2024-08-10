from pymarc import Record
from pymarc import Field
from pymarc import Subfield
from gettersSetters.getters import getListaDeCamposEnRegistro, getSubfields

class F5XXnotas_maker:

	def __init__(self, recordBIBUN, recordMARC):
		self.recordBIBUN = recordBIBUN
		self.recordMARC = recordMARC

	def set500desde036(self):
		F036BIBUNList = getListaDeCamposEnRegistro(self.recordBIBUN, '036')
		subfieldsMARC = []
		fieldMARC = ''
		for item in F036BIBUNList:
			sfCList = getSubfields(item, 'c')
			if len(sfCList) > 0:
				for sf in item.subfields:
					if sf.code == 'c':
						subfieldsMARC.append(Subfield('a', 'Enriquecimiento del título: '+sf.value))
				if len(subfieldsMARC) > 0:
					fieldMARC = Field('500', [' ', ' '], subfieldsMARC)
					self.recordMARC.add_field(fieldMARC)

	def set500desde046(self):
		F046BIBUNList = getListaDeCamposEnRegistro(self.recordBIBUN, '046')
		subfieldsMARC = []
		for item in F046BIBUNList:
			sfNList = getSubfields(item, 'n')
			sfVList = getSubfields(item, 'v')
			if len(sfNList) > 0 or len(sfVList) > 0 :
				valueN = ''
				valueV = ''
				for sf in item.subfields:
					if sf.code == 'n':
						valueN = 'Números por volumen: '+sf.value+'. '
					elif sf.code == 'v':
						valueV = 'Volúmenes por año: '+sf.value+'. '

				if valueN != '' or valueV != '':
					subfieldsMARC.append(Subfield('a', valueN + valueV))
				fieldMARC = Field('500', [' ', ' '], subfieldsMARC)
				self.recordMARC.add_field(fieldMARC)

	def set500desde059(self):
		F059BIBUNList = getListaDeCamposEnRegistro(self.recordBIBUN, '059')
		for item in F059BIBUNList:
			subfieldsMARC = []
			for sf in item.subfields:
				subfieldsMARC.append(Subfield('a', sf.value))
			if len(subfieldsMARC) > 0:
				fieldMARC = Field('500', [' ', ' '], subfieldsMARC)
				self.recordMARC.add_field(fieldMARC)

	def addF5XXnotas(self):
		self.set500desde036()
		self.set500desde046()
		self.set500desde059()