
#!/usr/bin/env python3
import os
import sys
from datetime import datetime
from entidades.campo     import Campo
from entidades.subcampo  import Subcampo
from BIBUNtoMARC_maker.BIBUNtoMARC import BIBUNtoMARC
from enlazador import Enlazador
from pymarc    import MARCReader
from pymarc    import Record
from escribirMarc import EscribirMARC
from informes  import initCSV, writeCSVCounter

bibliosBIBUN = 'archivos/mrcFiles/BIB_TODOS2.mrc'
# bibliosBIBUN = 'archivos/mrcFiles/BIB_10REG.mrc'
# bibliosBIBUN = 'archivos/mrcFiles/BIB_1REG.mrc'
# bibliosBIBUN = 'archivos/mrcFiles/BIB_TITULOS.mrc'
# bibliosBIBUN = 'archivos/mrcFiles/BIB_065.mrc'
# bibliosBIBUN = 'archivos/mrcFiles/BIB_057.mrc'

campo100 = Campo('100', [Subcampo('a', ''), Subcampo('d', '')])
campo110 = Campo('110', [Subcampo('a', ''), Subcampo('b', '')])
campo650 = Campo('650', [Subcampo('a', '')])
campo700 = Campo('700', [Subcampo('a', ''), Subcampo('d', '')])
campo710 = Campo('710', [Subcampo('a', ''), Subcampo('b', '')])
fechaAhora = datetime.now().strftime("%Y%m%d%H%M%S")
bibliosMARC = 'archivos/mrcTransformed/'+fechaAhora+'_BIB_EXPORT.mrc'

listaDeCampos = [campo100, campo110, campo650, campo710, campo700]

e = EscribirMARC(bibliosMARC)
enlazador = Enlazador()

# initCSV()
# print(sys.version)

if(len(listaDeCampos) > 0):
    if os.path.exists(bibliosBIBUN):
        with open(bibliosBIBUN, 'rb') as fh:
            reader = MARCReader(fh)
            for recordBIBUN in reader:
                record = Record()
                BIBUNtoMARC(record, recordBIBUN).MARCmaker()
                print(record)
                # enlazador.record = record
                # enlazador.link_auth(listaDeCampos)
                e.escribir(record)
            # print(writeCSVCounter(enlazador.recordCounter, enlazador.unlinkedAuth, enlazador.matchingAuth))
            # print("Trasnformacion exitosa:\n"
            #       "->Puede ver su archivo mrc modificado en archivos/mrcTransformed.\n"
            #       "->Puede ver los informes completos en archivos/reports.")
    else:
           print("No se puede encontrar el archivo .mrc que se quiere modificar. \nRecuerde declararlo correctamente en la variable 'biblios' en el archivo main.py")  
else:
   print("No ha declarado campos para enlazar. \nRecuerde declaralos correctamente en la variable 'listaDeCampos' en el archivo main.py ")
   



   
