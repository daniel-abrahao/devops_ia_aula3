import pytest # type: ignore
from src_alta.app import somar, dividir
 
def test_somar():
    assert somar(2, 3) == 5
 
def test_dividir():
    assert dividir(10, 2) == 5
 
def test_dividir_por_zero():
    with pytest.raises(ValueError):
        dividir(10, 0)
 
dentro da pasta tests_alta_ia_autorizado
 
import pytest # type: ignore
from src_baixa.app import somar, dividir
 
def test_somar():
    assert somar(2, 3) == 5
 
dentro da pasta tests_baixa
 