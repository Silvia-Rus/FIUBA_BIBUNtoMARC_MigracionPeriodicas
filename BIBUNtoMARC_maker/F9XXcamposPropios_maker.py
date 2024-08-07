from pymarc import Record
from pymarc import Field
from pymarc import Subfield
from datetime import datetime
from gettersSetters.getters import getListaDeCamposEnRegistro
from .diccionarios.ocurrencias import F952p


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

	def set952(self):
		subfieldsMARC = []
		subfieldsMARC.append(Subfield('0', '0'))
		subfieldsMARC.append(Subfield('1', '0'))
		subfieldsMARC.append(Subfield('3', '0'))
		subfieldsMARC.append(Subfield('7', '0'))
		subfieldsMARC.append(Subfield('7', '0'))
		subfieldsMARC.append(Subfield('a', 'BC'))
		subfieldsMARC.append(Subfield('b', 'BC'))
		subfieldsMARC.append(Subfield('o', '[SIGNATURA?]'))
		# barcode
		subfieldsMARC.append(Subfield('p', F952p[0]))
		# fecha actual en formato MMMM-DD-AA
		subfieldsMARC.append(Subfield('r', datetime.now().strftime('%Y-%m-%d')))
		subfieldsMARC.append(Subfield('y', 'CR'))
		fieldMARC = Field('952', ['#', '#'], subfieldsMARC)
		self.recordMARC.add_field(fieldMARC)
		F952p[0] += 1

	def set985(self):
		list096BIBUN = getListaDeCamposEnRegistro(self.recordBIBUN, '096')
		for item in list096BIBUN:
			subfieldsMARC = []
			for sf in item.subfields:
				subfieldsMARC.append(Subfield('a', sf.value))
				fieldMARC = Field('985', ['0', '0'], subfieldsMARC)
				self.recordMARC.add_field(fieldMARC)

	def set997(self):
		list098BIBUN = getListaDeCamposEnRegistro(self.recordBIBUN, '098')
		for item in list098BIBUN:
			subfieldsMARC = []
			for sf in item.subfields:
				subfieldsMARC.append(Subfield('a', sf.value))
				fieldMARC = Field('997', ['0', '0'], subfieldsMARC)
				self.recordMARC.add_field(fieldMARC)

	def addF9XXcamposPropios(self):
		self.recordMARC.add_field(self.F964)
		self.set942()
		self.set985()
		self.set997()
		self.set952()
		