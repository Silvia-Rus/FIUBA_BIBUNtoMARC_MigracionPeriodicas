from pymarc import Record
from pymarc import Field
from pymarc import Subfield
from .BIBUNtoMARCSubfields_equiv import BIBUNtoMARCSubfields_equiv
from gettersSetters.getters import getSubfieldsFromField, getListaDeCamposEnRegistro


class BIBUNtoMARCField:

	def __init__(self, recordBIBUN, fBIBUNtag, fMARCtag, ind1, ind2, listBIBUNtoMARCSubfields):
		self.recordBIBUN = recordBIBUN
		self.fBIBUNtag = fBIBUNtag
		self.fMARCtag = fMARCtag
		self.ind1 = ind1
		self.ind2 = ind2
		self.listBIBUNtoMARCSubfields = listBIBUNtoMARCSubfields

	def maker(self): 
		fields = []
		# Savamos del reg. BIBUN el listado de subcampos
		listaCamposBIBUN = getListaDeCamposEnRegistro(self.recordBIBUN, self.fBIBUNtag)
		if len(listaCamposBIBUN) > 0:
			subfields = []
			for campoBIBUN in listaCamposBIBUN: # miramos cada uno de los campos BIBUN
				for sfBIBUN in campoBIBUN.subfields: # miramos cada uno de los subcampos BIBUN
					# encontramos el code para el subcampo MARC
					SFequiv =  BIBUNtoMARCSubfields_equiv.buscarMARCCodeDesdeBIBUNcode(self.listBIBUNtoMARCSubfields,sfBIBUN.code)
					if SFequiv:
						subfields.append(Subfield(SFequiv, sfBIBUN.value))
				fields.append(Field(self.fMARCtag, [self.ind1, self.ind2], subfields))
		return fields

	@classmethod
	def writer(cls, recordMARC, MARCFieldList):
		if len(MARCFieldList) > 0:
			for MARCField in MARCFieldList:
				recordMARC.add_field(MARCField)








