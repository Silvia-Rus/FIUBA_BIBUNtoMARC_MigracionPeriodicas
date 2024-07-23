from pymarc import Record
from pymarc import Field
from pymarc import Subfield
from gettersSetters.getters import getListaDeCamposEnRegistro
from .diccionarios.BIBUN046n_MARC310a import BIBUN046n_MARC310a


class F3XXdescFis_maker:

	def __init__(self, recordBIBUN, recordMARC):
		self.recordBIBUN = recordBIBUN
		self.recordMARC = recordMARC
		self.F0300 = Field('300', ['#', '#'], [Subfield('a','v.')])

	def set300(self):
		self.recordMARC.add_field(self.F0300)

	def set310_222(self):
		F046BIBUNList = getListaDeCamposEnRegistro(self.recordBIBUN, '046')
		subfieldsMARC = []
		fieldMARC = ''
		for i, item in enumerate(F046BIBUNList):
			field = '310' if i == 0 else '322'
			for sf in item.subfields:
				if sf.code == 'c':
					value = BIBUN046n_MARC310a[sf.value]
					subfieldsMARC.append(Subfield('a', value))
			fieldMARC = Field(field, ['#', '#'], subfieldsMARC)
			self.recordMARC.add_field(fieldMARC)


	def addF3XXdescDis(self):
		self.set300()
		self.set310_222()
