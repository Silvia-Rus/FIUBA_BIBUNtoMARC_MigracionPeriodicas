from pymarc import Record
from pymarc import Field
from pymarc import Subfield
from gettersSetters.getters import getSubfieldsFromField
# from gettersSetters.setters import setField

class F2XXtitulos_maker:
	def __init__(self, recordBIBUN, recordMARC):
		self.recordBIBUN = recordBIBUN
		self.recordMARC = recordMARC

