import pytest

from minhas_notas_musicais.escalas import Escala


@pytest.mark.parametrize(
    'tonalidade, resultado',
    [
        ('maior', 'A B C# D E F# G#'),
        ('menor', 'A B C D E F G'),
        ('menor-harmonica', 'A B C D E F G#'),
        ('menor-melodica', 'A B C D E F# G#'),
    ]
)
def test_escalas(tonalidade, resultado):
    assert str(Escala('A', tonalidade)) == resultado
