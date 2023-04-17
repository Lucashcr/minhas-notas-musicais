from minhas_notas_musicais.progressoes import Progressao

import pytest


@pytest.mark.parametrize(
    'progressao, intervalo, semitonado',
    [
        ('C G Am F', -12, 'C G Am F'),
        ('C G Am F', -11, 'C# G# A#m F#'),
        ('C G Am F', -10, 'D A Bm G'),
        ('C G Am F', -9, 'D# A# Cm G#'),
        ('C G Am F', -8, 'E B C#m A'),
        ('C G Am F', -7, 'F C Dm A#'),
        ('C G Am F', -6, 'F# C# D#m B'),
        ('C G Am F', -5, 'G D Em C'),
        ('C G Am F', -4, 'G# D# Fm C#'),
        ('C G Am F', -3, 'A E F#m D'),
        ('C G Am F', -2, 'A# F Gm D#'),
        ('C G Am F', -1, 'B F# G#m E'),
        ('C G Am F', 0, 'C G Am F'),
        ('C G Am F', 1, 'C# G# A#m F#'),
        ('C G Am F', 2, 'D A Bm G'),
        ('C G Am F', 3, 'D# A# Cm G#'),
        ('C G Am F', 4, 'E B C#m A'),
        ('C G Am F', 5, 'F C Dm A#'),
        ('C G Am F', 6, 'F# C# D#m B'),
        ('C G Am F', 7, 'G D Em C'),
        ('C G Am F', 8, 'G# D# Fm C#'),
        ('C G Am F', 9, 'A E F#m D'),
        ('C G Am F', 10, 'A# F Gm D#'),
        ('C G Am F', 11, 'B F# G#m E'),
        ('C G Am F', 12, 'C G Am F'),
    ]
)
def test_semitom_retorna_corretamente_com_sustenidos(progressao, intervalo, semitonado):
    assert Progressao.parse(progressao).semitom(
        intervalo, '#') == Progressao.parse(semitonado)


@pytest.mark.parametrize(
    'progressao, intervalo, semitonado',
    [
        ('C G Am F', -12, 'C G Am F'),
        ('C G Am F', -11, 'Db Ab Bbm Gb'),
        ('C G Am F', -10, 'D A Bm G'),
        ('C G Am F', -9, 'Eb Bb Cm Ab'),
        ('C G Am F', -8, 'E B Dbm A'),
        ('C G Am F', -7, 'F C Dm Bb'),
        ('C G Am F', -6, 'Gb Db Ebm B'),
        ('C G Am F', -5, 'G D Em C'),
        ('C G Am F', -4, 'Ab Eb Fm Db'),
        ('C G Am F', -3, 'A E Gbm D'),
        ('C G Am F', -2, 'Bb F Gm Eb'),
        ('C G Am F', -1, 'B Gb Abm E'),
        ('C G Am F', 0, 'C G Am F'),
        ('C G Am F', 1, 'Db Ab Bbm Gb'),
        ('C G Am F', 2, 'D A Bm G'),
        ('C G Am F', 3, 'Eb Bb Cm Ab'),
        ('C G Am F', 4, 'E B Dbm A'),
        ('C G Am F', 5, 'F C Dm Bb'),
        ('C G Am F', 6, 'Gb Db Ebm B'),
        ('C G Am F', 7, 'G D Em C'),
        ('C G Am F', 8, 'Ab Eb Fm Db'),
        ('C G Am F', 9, 'A E Gbm D'),
        ('C G Am F', 10, 'Bb F Gm Eb'),
        ('C G Am F', 11, 'B Gb Abm E'),
        ('C G Am F', 12, 'C G Am F'),
    ]
)
def test_semitom_retorna_corretamente_com_bemois(progressao, intervalo, semitonado):
    assert Progressao.parse(progressao).semitom(
        intervalo, 'b') == Progressao.parse(semitonado)
