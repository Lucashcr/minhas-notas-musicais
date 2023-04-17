from minhas_notas_musicais.notas import *
from minhas_notas_musicais.notas import Nota, NOTAS_SEM_ACIDENTES, TODAS_AS_NOTAS

import pytest


def test_criacao_de_notas_especificando_acidente():
    for n in NOTAS_SEM_ACIDENTES:
        for a in ['', '#', 'b']:
            assert str(Nota(n, a)) == n + a


def test_criacao_de_notas_sem_especificar_acidente():
    for n in TODAS_AS_NOTAS:
        assert str(Nota(n)) == n


@pytest.mark.parametrize(
    'nota, intervalo, semitonada',
    [
        ('C', -12, 'C'),
        ('C', -11, 'C#'),
        ('C', -10, 'D'),
        ('C', -9, 'D#'),
        ('C', -8, 'E'),
        ('C', -7, 'F'),
        ('C', -6, 'F#'),
        ('C', -5, 'G'),
        ('C', -4, 'G#'),
        ('C', -3, 'A'),
        ('C', -2, 'A#'),
        ('C', -1, 'B'),
        ('C', 0, 'C'),
        ('C', 1, 'C#'),
        ('C', 2, 'D'),
        ('C', 3, 'D#'),
        ('C', 4, 'E'),
        ('C', 5, 'F'),
        ('C', 6, 'F#'),
        ('C', 7, 'G'),
        ('C', 8, 'G#'),
        ('C', 9, 'A'),
        ('C', 10, 'A#'),
        ('C', 11, 'B'),
        ('C', 12, 'C'),
    ]
)
def test_semitom_retorna_corretamente(nota, intervalo, semitonada):
    assert Nota(nota).semitom(intervalo) == Nota(semitonada)


@pytest.mark.parametrize(
    'nota, intervalo, semitonada',
    [
        ('C', -6, 'C'),
        ('C', -5.5, 'C#'),
        ('C', -5, 'D'),
        ('C', -4.5, 'D#'),
        ('C', -4, 'E'),
        ('C', -3.5, 'F'),
        ('C', -3, 'F#'),
        ('C', -2.5, 'G'),
        ('C', -2, 'G#'),
        ('C', -1.5, 'A'),
        ('C', -1, 'A#'),
        ('C', -0.5, 'B'),
        ('C', 0, 'C'),
        ('C', 0.5, 'C#'),
        ('C', 1, 'D'),
        ('C', 1.5, 'D#'),
        ('C', 2, 'E'),
        ('C', 2.5, 'F'),
        ('C', 3, 'F#'),
        ('C', 3.5, 'G'),
        ('C', 4, 'G#'),
        ('C', 4.5, 'A'),
        ('C', 5, 'A#'),
        ('C', 5.5, 'B'),
        ('C', 6, 'C'),
    ]
)
def test_tom_retorna_corretamente(nota, intervalo, semitonada):
    assert Nota(nota).tom(intervalo) == Nota(semitonada)


@pytest.mark.parametrize(
    'intervalo', (0.1, 0.2, 0.3, 0.4, 0.6, 0.7, 0.8, 0.9)
)
def test_tom_deve_lancar_ValueError(intervalo):
    with pytest.raises(ValueError) as error_info:
        C.tom(intervalo)
