import pytest

from minhas_notas_musicais.escalas import Escala


@pytest.mark.parametrize(
    'tonalidade, resultado, intervalos',
    [
        ('maior', 'A B C# D E F# G#', "I IIM IIIM IV V VIM VIIM"),
        ('menor', 'A B C D E F G', "I IIM IIIm IV V VIm VIIm"),
        ('menor-harmonica', 'A B C D E F G#', "I IIM IIIm IV V VIm VIIM"),
        ('menor-melodica', 'A B C D E F# G#', "I IIM IIIm IV V VIM VIIM"),
    ]
)
def test_escalas(tonalidade, resultado, intervalos):
    assert str(Escala('A', tonalidade)) == resultado
    assert ' '.join(Escala('A', tonalidade).intervalos()) == intervalos
