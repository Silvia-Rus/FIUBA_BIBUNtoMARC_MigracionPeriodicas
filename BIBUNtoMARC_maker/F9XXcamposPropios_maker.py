from pymarc import Record
from pymarc import Field
from pymarc import Subfield
from gettersSetters.getters import getListaDeCamposEnRegistro

class F9XXcamposPropios_maker:

	def __init__(self, recordBIBUN, recordMARC):
		self.recordBIBUN = recordBIBUN
		self.recordMARC = recordMARC
		self.F964 = Field('964', ['#', '#'], [Subfield('b','PUBENSERIE')])


	def set942(self):
		subfieldsMARC = []
		subfieldsMARC.append(Subfield('n', '0'))
		subfieldsMARC.append(Subfield('c', 'CR'))
		subfieldsMARC.append(Subfield('2', 'udc'))
		fieldMARC = Field('942', ['#', '#'], subfieldsMARC)
		self.recordMARC.add_field(fieldMARC)

	def set985(self):
		list096BIBUN = getListaDeCamposEnRegistro(self.recordBIBUN, '096')
		for item in list04XBIBUN:
			subfieldsMARC = []
			for sf in item.subfields:
				subfieldsMARC.append(Subfield('a', sf.value))
				fieldMARC = Field('985', ['0', '0'], subfieldsMARC)
				self.recordMARC.add_field(fieldMARC)

	def set997(self):
		list096BIBUN = getListaDeCamposEnRegistro(self.recordBIBUN, '098')
		for item in list04XBIBUN:
			subfieldsMARC = []
			for sf in item.subfields:
				subfieldsMARC.append(Subfield('a', sf.value))
				fieldMARC = Field('997', ['0', '0'], subfieldsMARC)
				self.recordMARC.add_field(fieldMARC)

	def F9XXcamposPropios(self):
		self.recordMARC.add_field(self.F964)
		self.set942()
		self.set985()
		self.set997()
		