# -*- coding: utf-8 -*-
from pymarc import MARCReader, Field

def setCampoSubcampoValor(campo, subcampo, valor):
    """
        Se aniade un subcampo a un campo y se le asigna un valor.

        Args:
            campo (Field): campo al cual se le quiere aniadir el subcampo y el valor.
            subcampo (str): subcampo que se quiere aniadir al campo.
            valor (str): valor que se le quiere asignar al subcampo
    """
    campo.add_subfield(subcampo, valor)

def setCF(record, CF, valores):
    if len(record.get_fields(CF)) > 0:
        record.remove_field(record.get_fields(CF)[0])
    record.add_field(Field(tag=CF, data=valores))

def setCF001(record, valores):
    setCF(record, '001', valores)

def setCF003(record, valores):
    setCF(record, '003', valores)

def setCF005(record, valores):
    setCF(record, '005', valores)

def setCF008(record, valores):
    setCF(record, '008', valores)


    

