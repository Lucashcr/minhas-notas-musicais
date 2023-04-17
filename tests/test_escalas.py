import pytest

from minhas_notas_musicais.escalas import Escala


@pytest.mark.parametrize(
    'tonalidade',
    ['maior', 'menor', 'menor-harmonica', 'menor-melodica']
)
def test_escalas(tonalidade):
    assert Escala('C')
