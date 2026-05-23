def somar(a, b):
	return a + b


def dividir(a, b):
	if b == 0:
		raise ValueError("b nao pode ser zero")
	return a / b


def verificar_numero(numero):
	if numero > 0:
		return "positivo"
	if numero < 0:
		return "negativo"
	return "zero"


def eh_par(numero):
	return numero % 2 == 0
