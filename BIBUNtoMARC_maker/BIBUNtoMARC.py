from BIBUNtoMARC_maker.controlField_maker.LDRtoCF005_maker import LDRtoCF005_maker
from BIBUNtoMARC_maker.controlField_maker.CF008_maker import CF008_maker
from BIBUNtoMARC_maker.F0XX_maker import F0XX_maker
from BIBUNtoMARC_maker.F2XXtitulos_maker import F2XXtitulos_maker
from BIBUNtoMARC_maker.F2XXpublic_maker import F2XXpublic_maker
from BIBUNtoMARC_maker.F3XXdescFis_maker import F3XXdescFis_maker
from BIBUNtoMARC_maker.F5XXnotas_maker import F5XXnotas_maker
from BIBUNtoMARC_maker.F6XX7XXencSec_maker import F6XX7XXencSec_maker
from BIBUNtoMARC_maker.F78Xrelaciones_maker import F78Xrelaciones_maker
from BIBUNtoMARC_maker.F86Xexistencias_maker import F86Xexistencias_maker
from BIBUNtoMARC_maker.F9XXcamposPropios_maker import F9XXcamposPropios_maker
from BIBUNtoMARC_maker.F952ejemplares_maker import F952ejemplares_maker


class BIBUNtoMARC:

	def __init__(self, recordMARC, recordBIBUN):
		self.recordMARC = recordMARC
		self.recordBIBUN= recordBIBUN

	def MARCmaker(self):
		LDRtoCF005_maker(self.recordMARC).addLDRtoCF005()
		CF008_maker(self.recordBIBUN, self.recordMARC).addCF008()
		F0XX_maker(self.recordBIBUN, self.recordMARC).addF0XX()
		F2XXtitulos_maker(self.recordBIBUN, self.recordMARC).addF2XXtitulos()
		F2XXpublic_maker(self.recordBIBUN, self.recordMARC).addF2XXpublic()
		F3XXdescFis_maker(self.recordBIBUN, self.recordMARC).addF3XXdescDis()
		F5XXnotas_maker(self.recordBIBUN, self.recordMARC).addF5XXnotas()
		F6XX7XXencSec_maker(self.recordBIBUN, self.recordMARC).addF6XX7XXencSec()
		F78Xrelaciones_maker(self.recordBIBUN, self.recordMARC).addF78Xrelaciones()
		F86Xexistencias_maker(self.recordBIBUN, self.recordMARC).addF86Xexistencias()		
		F9XXcamposPropios_maker(self.recordBIBUN, self.recordMARC).addF9XXcamposPropios()
		F952ejemplares_maker(self.recordBIBUN, self.recordMARC).addF952ejemplares()




		


