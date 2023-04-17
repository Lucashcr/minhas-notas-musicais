import re

from .notas import Nota


TONALIDADES = ['maior', 'menor']
TENSOES = [
    '2', 'sus2',
    '4', 'sus4', '11', '11+',
    '5+', '5-',
    '6', '6-', '13', '13-',
    '7', '7+',
    '9', '9+', '9-',
]


class Acorde:
    ...


class Acorde:
    ACORDE_REGEX = re.compile(r"^(\w[#b]?)(m)?((?:sus)?\d[+-]?)?")
    TENSOES_REGEX = re.compile(r"\((\d?\d[+-]?)\)")

    def __init__(self, tonica: Nota | str, tonalidade: str = 'maior', tensoes: list[str] = []):
        if tonalidade not in TONALIDADES:
            raise ValueError(
                f"Tonalidade inválida! Permitidas: {TONALIDADES}")
        elif not all(tensao in TENSOES for tensao in tensoes):
            raise ValueError(
                f"Tensão inválida! Permitidas: {TENSOES}")
        elif isinstance(tonica, str):
            tonica = Nota(tonica)

        self.tonica = tonica
        self.tonalidade = tonalidade
        self.tensoes = tensoes

    def __str__(self):
        cifra = str(self.tonica) + ('' if self.tonalidade == 'maior' else 'm')

        self.__ordena_tensoes()
        for tensao in self.tensoes:
            if self.tensoes.index(tensao) == 0:
                cifra += f'{tensao}'
            else:
                cifra += f'({tensao})'

        return cifra

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, __o: Acorde) -> bool:
        return (
            self.tonica == __o.tonica and
            self.tonalidade == __o.tonalidade and
            self.tensoes == __o.tensoes
        )

    @classmethod
    def parse(cls, acorde: str) -> Acorde:
        m = cls.ACORDE_REGEX.match(acorde)
        nota = m.group(1)
        tonalidade = 'menor' if m.group(2) == 'm' else 'maior'
        _tensoes = [m.group(3)] + cls.TENSOES_REGEX.findall(acorde)
        tensoes = [tensao for tensao in _tensoes if tensao is not None]
        return Acorde(Nota(nota), tonalidade, tensoes)

    def semitom(self, intervalo: int = +1, acidente: str | None = None) -> Acorde:
        return Acorde(self.tonica.semitom(intervalo, acidente), self.tonalidade, self.tensoes)

    def tom(self, intervalo: float = +1, acidente: str | None = None) -> Acorde:
        return Acorde(self.tonica.tom(intervalo, acidente), self.tonalidade, self.tensoes)

    @staticmethod
    def __sort_key(tensao):
        if 'sus' in tensao:
            tensao = tensao[3]
        if '+' in tensao or '-' in tensao:
            tensao = tensao[:-1]

        return int(tensao)

    def __ordena_tensoes(self):
        self.tensoes.sort(key=self.__sort_key)
