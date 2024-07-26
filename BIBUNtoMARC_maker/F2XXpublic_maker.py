from pymarc import Record
from pymarc import Field
from pymarc import Subfield
from gettersSetters.getters import getListaDeCamposEnRegistro
from regex import hacePrimeraLetraMinus, hacePrimeraLetraMayus


class F2XXpublic_maker:
	def __init__(self, recordBIBUN, recordMARC):
		self.recordBIBUN = recordBIBUN
		self.recordMARC = recordMARC

	def get260AyB(self):
		F047BIBUNList = getListaDeCamposEnRegistro(self.recordBIBUN, '047')
		sfA = []
		sfB = []
		retorno = []
		for item in F047BIBUNList:
				for sf in item.subfields:
					if sf.code == 'l':
						sfA.append(Subfield('a', sf.value))
					elif sf.code == 'e' or sf.code == '9':
						sfB.append(Subfield('b', sf.value))
		retorno.append(sfA)
		retorno.append(sfB)
		return retorno

	def set260a(self):
		sfAList = self.get260AyB()[0]
		retorno =[]
		if len(sfAList) == 0:
			retorno.append(Subfield('a', '? :'))
		else:
			for i, sf in enumerate(sfAList):
				value = hacePrimeraLetraMayus(sf.value)
				if i == len(sfAList) - 1:
					value += ' :'
				else:
					value += ' ; '
				retorno.append(Subfield('a', value))
		return retorno

	def set260b(self):
		sfBList = self.get260AyB()[1]
		retorno =[]
		if len(sfBList) == 0:
			retorno.append(Subfield('b', '? :'))
		else:
			for i, sf in enumerate(sfBList):
				value = hacePrimeraLetraMayus(sf.value)
				if i == len(sfBList) - 1:
					value += ' ,'
				else:
					value += ' ; '
				retorno.append(Subfield('b', value)) 
		return retorno

	def set260c(self):
		F045BIBUNList = getListaDeCamposEnRegistro(self.recordBIBUN, '045')
		retorno = []
		for item in F045BIBUNList:
			subfieldsMARC = []
			valuePrimerAnio = '? - '
			valueSegundoAnio = ''
			for sf in item.subfields:
				value = ''
				if sf.code == 'd':
					valuePrimerAnio = sf.value+'-'
				elif sf.code == 'h':
					valueSegundoAnio = sf.value
			value = valuePrimerAnio + valueSegundoAnio
			retorno.append(Subfield('c', value))
		return retorno

	def set260(self):
		sfA = self.set260a()
		sfB = self.set260b()
		sfC = self.set260c()
		subfieldsMARC = sfA + sfB + sfC
		fieldMARC = Field('260', ['#', '#'], subfieldsMARC)
		self.recordMARC.add_field(fieldMARC)

	def addF2XXpublic(self):
		self.set260()
	