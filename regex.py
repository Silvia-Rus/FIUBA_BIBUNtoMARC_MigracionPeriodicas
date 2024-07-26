# -*- coding: utf-8 -*-
import unicodedata
import sys
import re
from Casos.casos008 import a, d, o

def quitarTilde(string):
        return ''.join((c for c in unicodedata.normalize('NFD', string) if unicodedata.category(c) != 'Mn'))


def getCuatroPrimerasCifras(texto):
    retorno = False
    busqueda = re.search(r'\d{4}', str(texto))
    if busqueda:
        retorno = busqueda.group()
    return retorno

def apareceElStringEnLaLista(listaDeCasos, listaDeSubcampos):
    for caso in listaDeCasos:
        for sc in listaDeSubcampos:
            if caso in str(sc):
                return  True        
    return False

def separarParteEntreParentesis(texto):
    retorno = []
    partes = texto.split('(')
    retorno.append(partes[0])
    if len(partes) > 1:
        retorno.append(partes[1].split(')')[0])
    return retorno

def borrarStringEnItemsDeLista(listaDeCasos, string):
    retorno = []
    for caso in listaDeCasos:
        retorno.append(caso.replace(string, ""))
    return retorno

def esElPrimerCaracter(texto, caracter):
    retorno = False
    if texto[0] == caracter:
        retorno = True
    return retorno

def esElUltimoCaracter(texto, caracter):
    retorno = False
    if texto[-1] == caracter:
        retorno = True
    return retorno

def borrarElPrimerCaracter(texto):
    return texto[1:]

def borrarElUltimoCaracter(texto):
    return texto[:-1]

def separarParteEntreSimbolos(texto, simbolo):
    return texto.split(simbolo)
    # retorno = []
    # partes = texto.split(simbolo)
    # retorno.append(partes[0])
    # if len(partes) > 1:
    #     retorno.append(partes[1].split(')')[0])
    # return retorno

def tieneIlustraciones(listaDeStrings):
    return apareceElStringEnLaLista(a, listaDeStrings)

def tieneGraficas(listaDeStrings):
    return apareceElStringEnLaLista(d, listaDeStrings)

def tieneFotos(listaDeStrings):
    return apareceElStringEnLaLista(o, listaDeStrings)

def hacePrimeraLetraMinus(texto):
    return texto[0].lower() + texto[1:]

def hacePrimeraLetraMayus(texto):
    return texto[0].upper() + texto[1:]


    

    

