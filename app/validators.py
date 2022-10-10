#from curses.ascii import isalpha
from django.core.exceptions import ValidationError

def validar_letra(value):
    if value.isalpha():       
        raise  ValidationError(
            '%(value)s no puede contener una letra%',
            params={'value':value},
        )

def validar_numero(value):
    if value.isdigit():       
        raise  ValidationError("no puede contener un numero")

def validar_numeroMenorACero(value):
    if value<0:       
        raise  ValidationError("el precio no puede ser negativo")