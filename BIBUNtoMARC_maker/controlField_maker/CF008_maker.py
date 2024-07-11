
# -*- coding: utf-8 -*-
from gettersSetters.getters   import getList045d, getList045h, getList046c, getList048a, getList050l_0509
from gettersSetters.setters   import setCF008
from regex import getCuatroPrimerasCifras, tieneFotos, tieneGraficas, tieneIlustraciones, borrarStringEnItemsDeLista
from datetime import datetime
from ..diccionarios.BIBUN_048a_008_15_17 import BIBUN_048a_008_15_17
from ..diccionarios.BIBUN_046a_008_18 import BIBUN_046a_008_18
from ..diccionarios.BIBUN_050_008_35_37 import BIBUN_050_008_35_37


class CF008_maker:
    def __init__(self, recordBIBUN, recordMARC):
        self.recordBIBUN = recordBIBUN
        self.recordMARC = recordMARC
        self.CF008 = '--------------------|||r#||||0|||#0---#d'
    
    def __str__(self):
        return self.CF008

    def setPosiciones008(self, valores, posicionDesde, posicionHasta = None):
      retorno = False
      if posicionHasta == None or posicionHasta < 40:
        # print("entra a posicion hasta mayor a 39")
        # print(posicionDesde > -1)
        # print(posicionHasta > -1)
        # print(posicionDesde < posicionHasta)
        # print((posicionHasta-posicionDesde+1) == len(valores))
        lista008 = list(self.CF008)
        if posicionHasta == None and len(valores) == 1:
            lista008[posicionDesde] = valores
            retorno = True
        elif posicionDesde > -1 and posicionHasta > -1 and posicionDesde < posicionHasta and (posicionHasta-posicionDesde+1) == len(valores):
            i = posicionDesde
            for valor in valores:
                lista008[i] = valor
                i+=1
            retorno = True
        self.CF008 = ''.join(lista008)
      return retorno
        
    def setControlField008_00_05(self): # fecha de catalogación
       fechaAhora = datetime.now().strftime('%y%m%d')
       return self.setPosiciones008(fechaAhora, 0, 5)
    
    def setControlField008_06_10(self): # primera fecha de publicacion
      primerAnioCifras = self.getPrimerAnioCifras()
      str06_10 = 'm'+primerAnioCifras if primerAnioCifras else 'm||||'
      return self.setPosiciones008(str06_10, 6, 10)

    def setControlField008_11_14(self): # segunda fecha de publicacion
      segundoAnioCifras = self.getSegundoAnioCifras()
      str11_14 = segundoAnioCifras if segundoAnioCifras else '||||'
      return self.setPosiciones008(str11_14, 11, 14)

    def setControlField008_15_17(self): # lugar de edición
      lugarEdicion = getList048a(self.recordBIBUN)[0]
      str15_17 = BIBUN_048a_008_15_17[lugarEdicion]
      while len(str15_17) < 3:
        str15_17 += '#'
      return self.setPosiciones008(str15_17, 15, 17)

    def setControlField008_18(self): # periodicidad
      str18 = '|' 
      periodicidadLista = getList046c(self.recordBIBUN)
      if len(periodicidadLista) > 0 and BIBUN_046a_008_18[periodicidadLista[0]] != None:
          str18 = BIBUN_046a_008_18[periodicidadLista[0]]
      return self.setPosiciones008(str18, 18)

    def setControlField008_35_37(self):
      str35_37 = '|||'
      idiomasLista = self.getListaConStringSinErr3()
      if len(idiomasLista) > 0 and BIBUN_050_008_35_37[idiomasLista[0]] != None:
        str35_37 = BIBUN_050_008_35_37[idiomasLista[0]]
      return self.setPosiciones008(str35_37, 35, 37)

    def getPrimerAnioCifras(self):
      lista045d = getList045d(self.recordBIBUN)
      if len(lista045d) > 0:
        primeraFecha = lista045d[0]
        return getCuatroPrimerasCifras(primeraFecha)
      else:
        return False

    def getSegundoAnioCifras(self):
      lista045h = getList045h(self.recordBIBUN)
      if len(lista045h) > 0:
        segundaFecha = lista045h[0]
        return getCuatroPrimerasCifras(segundaFecha)
      else:
        return False

    def getListaConStringSinErr3(self):
      lista050 = getList050l_0509(self.recordBIBUN)
      if len(lista050) > 0:
        return borrarStringEnItemsDeLista(lista050, '[err3]')
      else:
        return False
    
    def addCF008(self):
       self.setControlField008_00_05()
       self.setControlField008_06_10()
       self.setControlField008_11_14()
       self.setControlField008_15_17()
       self.setControlField008_18()
       self.setControlField008_35_37()
       setCF008(self.recordMARC, self.CF008)


              
                  
        



        



    



