from pymarc import Record
from pymarc import Field
from pymarc import Subfield
from gettersSetters.getters import getListaDeCamposEnRegistro
from regex import borrarString, detectarString


class F86Xexistencias_maker:

	def __init__(self, recordBIBUN, recordMARC):
		self.recordBIBUN = recordBIBUN
		self.recordMARC = recordMARC

	def setSFa(self, field):
		fieldBIBUN = self.getFieldBIBUN(field)
		FBIBUNList = getListaDeCamposEnRegistro(self.recordBIBUN, fieldBIBUN)
		retorno = []
		for index, item in enumerate(FBIBUNList):
			value = ''
			for i, sf in enumerate(item.subfields):
				if i == len(item.subfields) - 1 and index != len(FBIBUNList) -1:
					value += sf.value+'; '
				else:
					value += sf.value+' '
			retorno.append(Subfield('a', value))
		return retorno


	def getFieldBIBUN(self, fieldMARC):
		if fieldMARC == '866':
			return '080'
		elif fieldMARC == '867':
			return '082'
		elif fieldMARC == '868':
			return '081'

	def getSfZ(self, fieldBIBUN):
		FBIBUNList = getListaDeCamposEnRegistro(self.recordBIBUN, fieldBIBUN)
		retorno = []
		for item in FBIBUNList:
			for sf in item:
				value = borrarString(sf.value, '[Err3]')
				retorno.append(Subfield('z', value))
		return retorno

	def set866(self):
		sf2MARC = [(Subfield('2', 'FOCAD'))]
		sfAMARC = self.setSFa('866')
		sfZMARCfrom099 = self.getSfZ('099')
		sfZMARCfrom191 = self.getSfZ('199')
		sfZMARC = sfZMARCfrom099 + sfZMARCfrom191
		subfieldsMARC = sf2MARC + sfAMARC + sfZMARC
		fieldMARC = Field('866', ['#', '7'], subfieldsMARC)
		self.recordMARC.add_field(fieldMARC)


	def set867_868(self, field):
		subfieldsMARC = self.setSFa(field)
		if len(subfieldsMARC) > 0:
			fieldMARC = Field(field, ['#', '0'], subfieldsMARC)
			self.recordMARC.add_field(fieldMARC)


	def addF86Xexistencias(self):
		self.set866()
		self.set867_868('867')
		self.set867_868('868')



