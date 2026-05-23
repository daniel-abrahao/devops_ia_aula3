def somar(a, b):
	return a + b


def dividir(a, b):
	if b == 0:
		raise ValueError("b nao pode ser zero")
	return a / b