from pymarc import Record
from pymarc import Field
from pymarc import Subfield

from gettersSetters.getters import getSubfieldsFromField


class F0XX_maker:
	def __init__(self, recordBIBUN, recordMARC):
		self.recordBIBUN = recordBIBUN
		self.recordMARC = recordMARC
		self.F040a = Field('040', ['#', '#'], [Subfield('a','AR-BaUFI'), Subfield('b', 'spa')])

	def set022a(self):
		F015aBIBUNList = getSubfieldsFromField(self.recordBIBUN, '015', 'a')
		retorno = False
		if len(F015aBIBUNList) > 0:
			retorno = Field('022', ['#', '#'], [Subfield('a', F015aBIBUNList[0])])
		return retorno

	def set080a(self):
		F060aBIBUNList = getSubfieldsFromField(self.recordBIBUN, '060', 'a')
		F061aBIBUNList = getSubfieldsFromField(self.recordBIBUN, '061', 'a')
		F060a061aBIBUNList = F060aBIBUNList + F061aBIBUNList
		retorno = False
		if len(F060a061aBIBUNList) > 0:
			retorno = Field('080',[ '#', '#'], [Subfield('a', F060a061aBIBUNList[0])])
		return retorno

	def addF0XX(self):
		self.recordMARC.add_field(self.F040a)
		F022a = self.set022a()
		F080a = self.set080a()
		if F022a: 
			self.recordMARC.add_field(F022a)
		if F080a: 
			self.recordMARC.add_field(F080a)









