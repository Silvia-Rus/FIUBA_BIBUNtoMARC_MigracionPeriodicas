from BIBUNtoMARC_maker.controlField_maker.LDRtoCF005_maker import LDRtoCF005_maker
from BIBUNtoMARC_maker.controlField_maker.CF008_maker import CF008_maker
from BIBUNtoMARC_maker.F0XX_maker import F0XX_maker
from BIBUNtoMARC_maker.F2XXtitulos_maker import F2XXtitulos_maker



class BIBUNtoMARC:

	def __init__(self, recordMARC, recordBIBUN):
		self.recordMARC = recordMARC
		self.recordBIBUN= recordBIBUN

	def MARCmaker(self):
		LDRtoCF005_maker(self.recordMARC).addLDRtoCF005()
		CF008_maker(self.recordBIBUN, self.recordMARC).addCF008()
		F0XX_maker(self.recordBIBUN, self.recordMARC).addF0XX()
		

		#008
		#0XX
		#2XX
		#...


		


