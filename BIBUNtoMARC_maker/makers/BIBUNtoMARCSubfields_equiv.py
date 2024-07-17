from pymarc import Record
from pymarc import Field
from pymarc import Subfield


class BIBUNtoMARCSubfields_equiv:

	def __init__(self, sfBIBUNCode, sfMARCCode):
		self.sfBIBUNCode = sfBIBUNCode
		self.sfMARCCode = sfMARCCode

	@classmethod
	def buscarMARCCodeDesdeBIBUNcode(cls, listBIBUNtoMARCSubfields, terminoABuscar):
		retorno = False
		if len(listBIBUNtoMARCSubfields) > 0:
			for item in listBIBUNtoMARCSubfields:
				if item.sfBIBUNCode == terminoABuscar:
					retorno = item.sfMARCCode
		return retorno






