import re

ACIDENTES = ["#", "b", ""]
NOTAS_SEM_ACIDENTES = "A B C D E F G".split()
NOTAS_COM_SUSTENIDO = "A A# B C C# D D# E F F# G G#".split()
NOTAS_COM_BEMOL = "A Bb B C Db D Eb E F Gb G Ab".split()
TODAS_AS_NOTAS = sorted(set(NOTAS_COM_BEMOL + NOTAS_COM_SUSTENIDO))


class Nota:
    ...


class Nota:
    NOTA_REGEX = re.compile(r'([ABCDEFG]{1})([#b]?)')

    def __init__(self, nota: str, acidente: str = ''):
        if not isinstance(nota, str):
            raise TypeError("O primeiro argumento precisa ser uma string")
        if nota not in TODAS_AS_NOTAS:
            raise ValueError(f"Nota inválida! Permitidas: {TODAS_AS_NOTAS}")
        if acidente not in ACIDENTES:
            raise ValueError(f"Acidente inválido! Permitidos: {ACIDENTES}")

        m = self.NOTA_REGEX.match(nota)
        self.nota = m.group(1)

        if acidente == '':
            self.acidente = m.group(2)
        else:
            self.acidente = acidente

    def __str__(self) -> str:
        return self.nota + self.acidente

    def __eq__(self, __o: Nota) -> bool:
        return (
            self.nota == __o.nota and
            self.acidente == __o.acidente
        )

    def semitom(self, intervalo: int = +1, acidente: str | None = None):
        if acidente is None:
            if self.acidente in ('#', ''):
                notas = NOTAS_COM_SUSTENIDO
            else:
                notas = NOTAS_COM_BEMOL
        else:
            if acidente == '#':
                notas = NOTAS_COM_SUSTENIDO
            elif acidente == 'b':
                notas = NOTAS_COM_BEMOL
            else:
                raise ValueError(
                    "Acidente inválido! Utilize um destes: [#, b]"
                )

        try:
            index = (NOTAS_COM_SUSTENIDO.index(str(self)) + intervalo) % 12
        except ValueError:
            index = (NOTAS_COM_BEMOL.index(str(self)) + intervalo) % 12

        return Nota(notas[index])

    def tom(self, intervalo: float = +1, acidente: str | None = None):
        if intervalo * 2 == int(intervalo * 2):
            return self.semitom(int(2 * intervalo), acidente)
        else:
            raise ValueError("Intervalo precisa ser múltiplo de 0.5!")


A = Nota("A")
As = Nota("A#")
Ab = Nota("Ab")

B = Nota("B")
Bb = Nota("Bb")

C = Nota("C")
Cs = Nota("C#")

D = Nota("D")
Ds = Nota("D#")
Db = Nota("Db")

E = Nota("E")
Eb = Nota("Eb")

F = Nota("F")
Fs = Nota("F#")

G = Nota("G")
Gs = Nota("G#")
Gb = Nota("Gb")


# __all__ = [
#     'A', 'As', 'Ab',
#     'B', 'Bb',
#     'C', 'Cs',
#     'D', 'Ds', 'Db',
#     'E', 'Eb',
#     'F', 'Fs',
#     'G', 'Gs', 'Gb',
# ]

# if __name__ == '__main__':
#     print(Nota('A#'))
