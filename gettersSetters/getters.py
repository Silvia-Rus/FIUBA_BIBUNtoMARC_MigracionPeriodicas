# -*- coding: utf-8 -*-
from pymarc import MARCReader
from pymarc import Field

def getListaDeCamposEnRegistro(record, fieldTag):
   """
      Devuelve las ocurrencias de un campo en concreto que se encuentran dentro de un registro.

      Args:
         record (Record): el registro en el que se va a buscar el campo.
         fieldTag (str) : el campo a buscar.
      
      Return:
         List: un listado de items en tipo Field con las ocurrencias.
   """
   return record.get_fields(fieldTag)

def getSubfields(field, subfield):
    """
      De un campo en concreto se devuelve un listado de subcampos cuya letra se especifica en el argumento.

      Args:
         field (Field): un campo de tipo Field del cual se quieren extraer los subcampos.
         subfield (str): una letra que representa el subcampo del que queremos tomar la informacion.
      
      Return:
         List: un listado de subcampos.
    """
    return field.get_subfields(subfield) #devuelve una lista

def getListDollar9(campo):
   """
      Encuentra el listado de ocurrencias de subcampo 9 del campo que entra como argumento.

      Args:
         campo (Field): el campo del que se quieren extraer los subcampos 9.
      
      Return: 
         List: el listado de subcampos 9 encontrados. 
   """
   return getSubfields(campo, '9') 

def getListDollarA(campo):
   """
      Encuentra el listado de ocurrencias de subcampo a del campo que entra como argumento.

      Args:
         campo (Field): el campo del que se quieren extraer los subcampos a.
      
      Return:
         List: el listado de subcampos a encontrados. 
   """
   return getSubfields(campo, 'a') 

def getSubfieldsFromField(record, fieldTag, subfieldTag):
    listFields = getListaDeCamposEnRegistro(record, fieldTag)
    listSubfields = []
    for field in listFields:
        listSubfields += getSubfields(field, subfieldTag)
    return listSubfields
        
def getList045d(record):
    return getSubfieldsFromField(record, '045', 'd')

def getList045h(record):
    return getSubfieldsFromField(record, '045', 'h')

def getList046c(record):
    return getSubfieldsFromField(record, '046', 'c')

def getList048a(record):
    return getSubfieldsFromField(record, '048', 'a')

def getIl300(record):
    list300a = getSubfieldsFromField(record, '300', 'a')
    list300b = getSubfieldsFromField(record, '300', 'b')
    return list300a + list300b

# def getAnio0452(record):
#     list260c = getList260c(record)
#     list264c = getList264c(record)
#     return list260c + list264c   

def getHasUnlinkedAuth(campo):
   """
      Detecta si el campo tiene un subcampo 9. Utilizado para saber si
      un campo de encabezamiento de un registro bibliografico generado con Koha esta 
      enlazado a un registro de autoridad o no. 

      Args:
         Campo (Field): campo del cual se quiere saber si contiene un subcampo 9.

      Return: 
         Bool: verdadero si no tiene subcampo 9. Falso si lo tiene.
   """
   return len(getListDollar9(campo)) == 0 and len(getListDollarA(campo)) > 0

def getSubfields(campo, subcampo):
   """
      Devuelve un listado de subcampos con las ocurrencias de un subcampo concreto 
      que aparecen un un campo que entra por parametro.

      Args:
         Campo (Field): campo del cual se quieren recuperar las ocurrencias de un subcampo.
         Subcampo (str): subcampo del cual queremos las ocurrencias en el campo que entra por parametro.
      
      Return:
         List: lista de ocurrencias del subcampo.
   """                                  
   return campo.get_subfields(subcampo)

def getValorSubfield(subcampo):
      return subcampo.encode('utf-8')

def getBiblioNumber(record):
   """
      Devuelve el Biblionumber de un registro descargado de Koha del cual se asume contiene 
      esa informacion en el 999$c.

      Args:
         Record (Record): registro del cual se quiere saber el biblionumber.
      
      Return:
         String: el Biblionumber del registro o None si no contiene campo 990$c.
   """
   listaCampos999 = record.get_fields('999')
   if len(listaCampos999) > 0:
      listaSubcampos999c = listaCampos999[0].get_subfields('c')
      if len(listaSubcampos999c) > 0:
         return listaSubcampos999c[0]
   return None

def getCF008(record):
    return record['008']

def getCF001(record):
    # return record.get_fields('008')[0].encode('utf-8')
    return record['001']




   
   
   


