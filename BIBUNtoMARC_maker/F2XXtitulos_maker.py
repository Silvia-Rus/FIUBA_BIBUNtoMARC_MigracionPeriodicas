from pymarc import Record
from pymarc import Field
from pymarc import Subfield
from gettersSetters.getters import getSubfieldsFromField, getListaDeCamposEnRegistro
from .makers.BIBUNtoMARCField import BIBUNtoMARCField
from .makers.BIBUNtoMARCSubfields_equiv import BIBUNtoMARCSubfields_equiv

class F2XXtitulos_maker:
	def __init__(self, recordBIBUN, recordMARC):
		self.recordBIBUN = recordBIBUN
		self.recordMARC = recordMARC









