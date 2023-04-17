import pytest

from minhas_notas_musicais.acordes import Acorde, Nota


@pytest.mark.parametrize(
    'acorde',
    [
        'A',
        'A#',
        'Am',
        'A#m',
        'Abm',
        'Am7',
        'A7+',
        'Asus4',
        'Amsus4',
        'Asus4(9)',
        'A7(9+)',
        'Asus4(7)(9)(11)',
    ]
)
def test_fazer_parse_de_acordes(acorde):
    assert str(Acorde.parse(acorde)) == acorde


@pytest.mark.parametrize(
    'acorde, intervalo, semitonado',
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
def test_semitom_retorna_corretamente(acorde, intervalo, semitonado):
    assert Acorde.parse(acorde).semitom(intervalo) == Acorde.parse(semitonado)


@pytest.mark.parametrize(
    'acorde, intervalo, semitonado',
    [
        ('C9', 0, 'C9'),
        ('C7', 0.5, 'C#7'),
        ('Cm7+', 1, 'Dm7+'),
        ('Csus4(9)', 1.5, 'D#sus4(9)'),
        ('Cmsus4(9)(11)', 2, 'Emsus4(9)(11)'),
    ]
)
def test_tom_retorna_corretamente(acorde, intervalo, semitonado):
    assert Acorde.parse(acorde).tom(intervalo) == Acorde.parse(semitonado)


@pytest.mark.parametrize(
    'intervalo', (0.1, 0.2, 0.3, 0.4, 0.6, 0.7, 0.8, 0.9)
)
def test_tom_deve_lancar_ValueError(intervalo):
    with pytest.raises(ValueError) as error_info:
        Acorde(Nota('C')).tom(intervalo)


def test_muda_tonalidade_do_acorde():
    assert -Acorde('C') == Acorde('C', 'menor')
    assert -Acorde('C', 'menor') == Acorde('C', 'maior')
