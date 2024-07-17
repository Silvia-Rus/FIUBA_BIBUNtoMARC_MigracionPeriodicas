from pymarc import Record
from pymarc import Field
from pymarc import Subfield
from .makers.BIBUNtoMARCField import BIBUNtoMARCField
from .makers.BIBUNtoMARCSubfields_equiv import BIBUNtoMARCSubfields_equiv
from gettersSetters.getters import getSubfieldsFromField


class F0XX_maker:
	def __init__(self, recordBIBUN, recordMARC):
		self.recordBIBUN = recordBIBUN
		self.recordMARC = recordMARC
		self.F040a = Field('040', ['#', '#'], [Subfield('a','AR-BaUFI'), Subfield('b', 'spa')])

	def setF022a(self):
		# F015aBIBUNList = getSubfieldsFromField(self.recordBIBUN, '015', 'a')
		# retorno = False
		# if len(F015aBIBUNList) > 0:
		# 	retorno = Field('022', ['#', '#'], [Subfield('a', F015aBIBUNList[0])])
		# return retorno
		BIBUNtoMARCSubfields = [BIBUNtoMARCSubfields_equiv('a','a')]
		BIBUNtoMARC = BIBUNtoMARCField(
			self.recordBIBUN,
			'015', '022', '#', '#', 
			BIBUNtoMARCSubfields
		)
		MARCFieldsList = BIBUNtoMARC.maker()
		BIBUNtoMARCField.writer(self.recordMARC, MARCFieldsList)

	def setF080a(self):
		F060aBIBUNList = getSubfieldsFromField(self.recordBIBUN, '060', 'a')
		F061aBIBUNList = getSubfieldsFromField(self.recordBIBUN, '061', 'a')
		F060a061aBIBUNList = F060aBIBUNList + F061aBIBUNList
		retorno = False
		if len(F060a061aBIBUNList) > 0:
			retorno = Field('080',[ '#', '#'], [Subfield('a', F060a061aBIBUNList[0])])
		return retorno

	def addF0XX(self):
		self.recordMARC.add_field(self.F040a)
		self.setF022a()
		F080a = self.setF080a()
		# if F022a: 
		# 	self.recordMARC.add_field(F022a)
		if F080a: 
			self.recordMARC.add_field(F080a)









