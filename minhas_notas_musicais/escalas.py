from .notas import Nota


ESCALAS = {
    'maior': (0, 2, 4, 5, 7, 9, 11),
    'menor': (0, 2, 3, 5, 7, 8, 10),
    'menor-harmonica': (0, 2, 3, 5, 7, 8, 11),
    'menor-melodica': (0, 2, 3, 5, 7, 9, 11),
}

INTERVALOS = "I IIm IIM IIIm IIIM IV IV# V VIm VIM VIIm VIIM".split()


class Escala:
    def __init__(self, tonica: Nota | str, tonalidade: str = 'maior'):
        if isinstance(tonica, str):
            tonica = Nota(tonica)

        if tonalidade not in ESCALAS.keys():
            raise ValueError(
                f"Tonalidade inválida! Permitidas: {ESCALAS.keys()}"
            )

        self.tonica = tonica
        self.tonalidade = tonalidade

    def __str__(self) -> str:
        return ' '.join(str(self.tonica.semitom(i)) for i in ESCALAS[self.tonalidade])
        # esc = ''
        # for i in ESCALAS[self.tonalidade]:
        #     esc += f'| {self.tonica.semitom(i):<2} '
        # esc += '|'
        # return '-'*len(esc) + '\n' + esc + '\n' + '-'*len(esc)

    @classmethod
    def intervalos(cls, tonalidade: str = 'maior'):
        return [INTERVALOS[i] for i in ESCALAS[tonalidade]]
