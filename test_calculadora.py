import pytest 

from calculadora import sumar, restar, multiplicar, dividir,  calcular_total

def test_sumar_con_negativos():
 assert sumar(5, (-5)) == 0
 
def test_restar_resultado_negativo():
 assert restar(9, 9) == 0
 
def test_multiplicar_por_cero():
 assert multiplicar(-5, -2) == 10
 
def test_dividir_resultado_decimal():
 assert dividir(-4, 2) == -2.0

def test_calcular_total_con_descuento():
 assert calcular_total(100, 2, 10) == 180.0
 
