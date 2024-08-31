from pymarc import Record
from pymarc import Field
from pymarc import Subfield
from gettersSetters.getters import getListaDeCamposEnRegistro
from regex import separarParteEntreParentesis, hacePrimeraLetraMinus, hacePrimeraLetraMayus

class F2XXtitulos_maker:
	def __init__(self, recordBIBUN, recordMARC):
		self.recordBIBUN = recordBIBUN
		self.recordMARC = recordMARC

	def set210_222(self, field):
		fieldBIBUN = '037' if field == '210' else '035'
		ind = ['0', ' '] if field == '210' else [' ', ' ']
		FBIBUNList = getListaDeCamposEnRegistro(self.recordBIBUN, fieldBIBUN)
		if len(FBIBUNList) > 0:
			for item in FBIBUNList:
				subfieldsMARC = []
				for sf in item.subfields:
					if sf.code == 't':
						texto = separarParteEntreParentesis(sf.value)
						sfA = texto[0]
						subfieldsMARC.append(Subfield('a', sfA))
						if len(texto) > 1:
							sfB = texto[1]
							subfieldsMARC.append(Subfield('b', '('+sfB+')'))
					elif sf.code == 'c':
						subfieldsMARC.append(Subfield('b', '('+sf.value+')'))
				fieldMARC = Field(field, ind, subfieldsMARC)
				fieldMARC.subfields.sort(key=lambda x: x.code)
				self.recordMARC.add_field(fieldMARC)

	def set210(self):
		self.set210_222('210')

	def set222(self):
		self.set210_222('222')

	def get245(self):
		F036BIBUNList = getListaDeCamposEnRegistro(self.recordBIBUN, '036')
		sfAList = []
		sfBValues = []
		sfBList = []
		sfNList = []
		sfPList = []
		sfCList = []
		retorno = []
		if len(F036BIBUNList) > 0:
			for item in F036BIBUNList:
				subfieldsMARC = []
				for sf in item.subfields:
					if sf.code == 't':
						if len(sfAList) == 0:
							sfAList.append(Subfield('a', sf.value))
						else:
							sfBValues.append(sf.value)
					elif sf.code == 's':
						sfBValues.append(sf.value)
					elif sf.code == 'd':
						sfNList.append(Subfield('n', sf.value))
					elif sf.code == 'u':
						sfPList.append(Subfield('p', sf.value))
					elif sf.code == 'r':
						sfCList.append(Subfield('c', sf.value))

		if len(sfBValues) > 0:
			value = ''
			for i, item in enumerate(sfBValues):
				if i > 0:
					value += ' : ' 
				value += hacePrimeraLetraMinus(item)					 
			sfBList.append(Subfield('b', value))

		retorno.append(sfAList)
		retorno.append(sfBList)
		retorno.append(sfNList)
		retorno.append(sfPList)
		retorno.append(sfCList)
		return retorno

	@classmethod
	def hay(cls, list):
		return len(list) > 0 
			
	def set245(self):
		sfA = self.get245()[0]
		sfB = self.get245()[1]
		sfN = self.get245()[2]
		sfP = self.get245()[3]
		sfC = self.get245()[4]
		retorno = []
		#puntuación sfA
		if F2XXtitulos_maker.hay(sfA):
			value = sfA[0].value
			if F2XXtitulos_maker.hay(sfB):
				value += ' : '
			elif F2XXtitulos_maker.hay(sfN) or F2XXtitulos_maker.hay(sfP):
				value += '. '
			elif F2XXtitulos_maker.hay(sfC):
				value += ' / '
			retorno.append(Subfield('a', value))	
		#puntuación sfB
		if F2XXtitulos_maker.hay(sfB):
			for i, item in enumerate(sfB):
				value = item.value
				if i != len(sfB)-1:
					value +=  ' : '
				else:
					if F2XXtitulos_maker.hay(sfN) and F2XXtitulos_maker.hay(sfP):
						value +=  '. '
					elif F2XXtitulos_maker.hay(sfC):
						value +=  ' / '	
				retorno.append(Subfield('b', value))
		#puntuación sfN
		if F2XXtitulos_maker.hay(sfN):
			for i, item in enumerate(sfN):
				value = hacePrimeraLetraMayus(item.value)
				if i != len(sfN)-1:
					value +=  ', '
				else:
					if F2XXtitulos_maker.hay(sfP):
						value += ', '
					elif F2XXtitulos_maker.hay(sfC):
						value +=  ' / '	
				retorno.append(Subfield('n', value))
		#puntuación sfP
		if F2XXtitulos_maker.hay(sfP):
			for i, item in enumerate(sfP):
				value = hacePrimeraLetraMinus(item.value) if F2XXtitulos_maker.hay(sfN) else hacePrimeraLetraMayus(item.value)
				if i != len(sfP)-1:
					value += ', '
				else:
					if F2XXtitulos_maker.hay(sfC):
						value += ' / '
				retorno.append(Subfield('p', value))
		if F2XXtitulos_maker.hay(sfC):
			for i, item in enumerate(sfC):
				value = hacePrimeraLetraMayus(item.value)
				if i > 0:
					value += ', '
				retorno.append(Subfield('c', value))


		subfieldsMARC =  retorno
		fieldMARC = Field('245', ['0', ' '], subfieldsMARC)
		self.recordMARC.add_field(fieldMARC)

	def set246(self):
		F038BIBUNList = getListaDeCamposEnRegistro(self.recordBIBUN, '038')
		if len(F038BIBUNList) > 0:
			for item in F038BIBUNList:
				subfieldsMARC = []
				for sf in item.subfields:
					if sf.code == 'a':
						subfieldsMARC.append(Subfield('a', sf.value))
				fieldMARC = Field('246', ['2', ' '], subfieldsMARC)
				self.recordMARC.add_field(fieldMARC)

	def addF2XXtitulos(self):
		self.set210()
		self.set222()
		self.set245()
		self.set246()
