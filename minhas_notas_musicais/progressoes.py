from .acordes import Acorde
from .notas import Nota, NOTAS_COM_BEMOL, NOTAS_COM_SUSTENIDO, TODAS_AS_NOTAS
from .notas import *


class Progressao:
    ...


class Progressao:
    def __init__(self, *acordes: Acorde):
        self.acordes = acordes

    @classmethod
    def parse(cls, progressao: str):
        progressao = progressao.split(' ')
        while '' in progressao:
            progressao.remove('')

        return Progressao(*map(lambda item: Acorde.parse(item), progressao))

    def semitom(self, intervalo: int = +1, acidente: str | None = None):
        return Progressao(*(acorde.semitom(intervalo, acidente) for acorde in self.acordes))

    def tom(self, intervalo: int = +1, acidente: str | None = None):
        return self.semitom(2*intervalo, acidente)

    def transpor(self, destino: Acorde | str):
        if not isinstance(destino, Acorde):
            if isinstance(destino, str):
                destino = Acorde.parse(destino)
            else:
                raise TypeError("O parâmetro tom precisa ser um acorde")
        if str(destino) not in TODAS_AS_NOTAS:
            raise ValueError(
                f"Nota inválida! Tente umas destas: {TODAS_AS_NOTAS}"
            )

        if str(self.acordes[0].tonica) in NOTAS_COM_BEMOL:
            indice_origem = NOTAS_COM_BEMOL.index(str(self.acordes[0].tonica))
        else:
            indice_origem = NOTAS_COM_SUSTENIDO.index(
                str(self.acordes[0].tonica))

        if str(destino.tonica) in NOTAS_COM_BEMOL:
            indice_destino = NOTAS_COM_BEMOL.index(str(destino.tonica))
        else:
            indice_destino = NOTAS_COM_SUSTENIDO.index(str(destino.tonica))

        semitoms = indice_destino - indice_origem
        if destino.tonica.acidente:
            return self.semitom(semitoms, destino.tonica.acidente)
        else:
            return self.semitom(semitoms)

    def __str__(self) -> str:
        return ' '.join(str(acorde) for acorde in self.acordes)

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, other: Progressao) -> bool:
        if len(self.acordes) != len(other.acordes):
            return False

        return all(self.acordes[i] == other.acordes[i] for i in range(len(self.acordes)))
