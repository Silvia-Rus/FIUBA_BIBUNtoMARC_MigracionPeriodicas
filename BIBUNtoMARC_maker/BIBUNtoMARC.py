from BIBUNtoMARC_maker.controlField_maker.LDRtoCF005_maker import LDRtoCF005_maker
from BIBUNtoMARC_maker.controlField_maker.CF008_maker import CF008_maker
from BIBUNtoMARC_maker.F0XX_maker import F0XX_maker
from BIBUNtoMARC_maker.F2XXtitulos_maker import F2XXtitulos_maker
from BIBUNtoMARC_maker.F2XXpublic_maker import F2XXpublic_maker
from BIBUNtoMARC_maker.F3XXdescFis_maker import F3XXdescFis_maker





class BIBUNtoMARC:

	def __init__(self, recordMARC, recordBIBUN):
		self.recordMARC = recordMARC
		self.recordBIBUN= recordBIBUN

	def MARCmaker(self):
		LDRtoCF005_maker(self.recordMARC).addLDRtoCF005()
		# CF008_maker(self.recordBIBUN, self.recordMARC).addCF008()
		F0XX_maker(self.recordBIBUN, self.recordMARC).addF0XX()
		F2XXtitulos_maker(self.recordBIBUN, self.recordMARC).addF2XXtitulos()
		F2XXpublic_maker(self.recordBIBUN, self.recordMARC).addF2XXpublic()
		F3XXdescFis_maker(self.recordBIBUN, self.recordMARC).addF3XXdescDis()

		#008
		#0XX
		#2XX
		#...


		


