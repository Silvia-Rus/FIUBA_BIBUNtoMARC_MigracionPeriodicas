from pymarc import Record
from pymarc import Field
from pymarc import Subfield
from datetime import datetime
from gettersSetters.getters import getListaDeCamposEnRegistro

class F9XXcamposPropios_maker:

	def __init__(self, recordBIBUN, recordMARC):
		self.recordBIBUN = recordBIBUN
		self.recordMARC = recordMARC
		self.F997 = Field('997', [' ', ' '], [Subfield('b','PUBENSERIE')])


	def set942(self):
		subfieldsMARC = []
		subfieldsMARC.append(Subfield('n', '0'))
		subfieldsMARC.append(Subfield('c', 'CR'))
		subfieldsMARC.append(Subfield('2', 'udc'))
		fieldMARC = Field('942', [' ', ' '], subfieldsMARC)
		self.recordMARC.add_field(fieldMARC)

	def set985(self, field):
		listBIBUN = getListaDeCamposEnRegistro(self.recordBIBUN, field)
		for item in listBIBUN:
			subfieldsMARC = []
			for sf in item.subfields:
				subfieldsMARC.append(Subfield('2', 'BIBUN '+field+'$a'))
				subfieldsMARC.append(Subfield('a', sf.value))
				fieldMARC = Field('985', ['0', '0'], subfieldsMARC)
				self.recordMARC.add_field(fieldMARC)

	#FALTA EL 986

	def set985from085(self):
		self.set985('085')

	def set985from096(self):
		self.set985('096')

	def set964(self):
		list098BIBUN = getListaDeCamposEnRegistro(self.recordBIBUN, '964')
		for item in list098BIBUN:
			subfieldsMARC = []
			for sf in item.subfields:
				subfieldsMARC.append(Subfield('b', sf.value))
				fieldMARC = Field('964', ['0', '0'], subfieldsMARC)
				self.recordMARC.add_field(fieldMARC)

	def addF9XXcamposPropios(self):
		self.recordMARC.add_field(self.F997)
		self.set942()
		self.set985from085()
		self.set985from096()
		self.set964()
		