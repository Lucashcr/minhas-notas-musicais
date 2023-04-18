# Minhas notas musicais

Esta é uma biblioteca em Python para fazer operações sobre notas, acordes, progressões e escalas musicais. O projeto foi baseado no repositório [notas-musicais](https://github.com/dunossauro/notas-musicais) implementado pelo Dunossauro (Eduardo Mendes) para o projeto [#CodaComigo](https://www.youtube.com/watch?v=R3hCkU4EXgY&list=PLOQgLBuj2-3LiHhK1upnjpHiFzcJ472QS) do canal Live de Python.

O objetivo deste projeto é reescrevê-lo utilizando-se o paradigma de programação orientada a objetos, tomando-se algumas decisões um pouco diferentes do projeto original, além de implementar algumas funcionalidades a mais que foram julgadas pertinentes.

## Instalação
Para instalar a biblioteca, basta clonar o repositório.

<!-- 
```python
pip install minhas_notas_musicais
```
-->

## Uso
Para usar a biblioteca, primeiro importe o módulo correspondente:

```python
import minhas_notas_musicais.notas as notas
import minhas_notas_musicais.acordes as acordes
import minhas_notas_musicais.progressoes as progressoes
import minhas_notas_musicais.escalas as escalas
```

### Notas
O módulo notas permite trabalhar com notas musicais. É possível criar uma nota a partir de uma string ou utilizar uma das notas definidas pela lib:

```python
# Criando uma nota a partir de uma string
n = notas.Nota("C")
print(n)  # C

n = notas.Nota("C#")
print(n)  # C#

n = notas.Nota("Db")
print(n)  # Db
```

```python
# Notas definidas pela lib
print(notas.A)  # A
print(notas.As)  # A#
print(notas.Ab)  # Ab
```

Além disso, é possível, dada uma nota, capturar a nota que encontra-se a um intervalo solicitado de semitons ou tons. Por padrão, a biblioteca assume o valor de um semitom ou tom, mas o valor também pode ser informado na chamada do método, além de poder forçar também o acidente a ser utilizado (sustenido ou bemol). Por padrão, utiliza-se o sustemnido.

Veja no exemplo abaixo como isto pode ser feito:

```python
# Notas definidas pela lib
print(notas.C.semitom())  # C#
print(notas.C.tom())  # D
print(notas.C.semitom(intevalo=+3))  # D#
print(notas.C.tom(intevalo=+2))  # E
print(notas.C.semitom(acidente='b'))  # Db
```

### Acordes

O módulo acordes permite trabalhar com acordes musicais. É possível criar um acorde a partir de uma string que representa o seu nome ou utilizando-se o método de classe `parse`. Uma funcionalidade interessante implementada além do projeto original foi a possibilidade de se trabalhar com tensões. Aqui está como isto pode ser feito:

```python
# Criando um acorde de Dó maior
print(acordes.Acorde(notas.C, "maior"))  # C

# Criando um acorde de Lá menor
print(acordes.Acorde.parse("Am"))  # Am

# Criando um acorde com tensões
print(acorde.Acorde.parse("Em7(9)"))  # Em7(9)
```

Vale salientar que, tal como as notas, os acordes também possuem os métodos de `tom` e `semitom` para transpor o acorde conforme necessário.

### Escalas

O módulo escalas permite trabalhar com escalas musicais. É possível criar uma escala a partir de dois parâmetros: a tônica da escala e sua tonalidade. Até então, foram implementadas apenas as escalas:

- Maior natural
- Menor natural
- Menor harmônica
- Menor melódica

Além de obter a escala em si, é possivel também obter os intervalos que a formam.

```python
# Criando uma escala maior
print(escalas.Escala("C", "maior"))  # C D E F G A B
print(escalas.Escala("C", "maior").intervalos())  # I IIM IIIM IV V VIM VIIM

# Criando uma escala menor
print(escalas.Escala("Am", "menor"))  # A B C D E F G
print(escalas.Escala("Am", "menor").intervalos())  # I IIM IIIm IV V VIm VIIm

# Criando uma escala menor harmônica
print(escalas.Escala("Am", "menor-harmonica"))  # A B C D E F G#
print(escalas.Escala("Am", "menor-harmonica").intervalos())  # I IIM IIIm IV V VIm VIIM

# Criando uma escala menor melódica
print(escalas.Escala("Am", "menor-melodica"))  # A B C D E F# G#
print(escalas.Escala("Am", "menor-melodica").intervalos())  # I IIM IIIm IV V VIM VIIM
```

### Progressões

O módulo progressoes permite trabalhar com progressões de acordes. É possível criar uma progressão a partir de uma sequência de acordes, com ou sem tensões, ou utilizando-se o método de classe `parse` para obtê-la a partir de uma string única. Por exemplo:

```python
print(progressoes.Progressao(
    acordes.Acorde('C'),
    acordes.Acorde('G'),
    acordes.Acorde('Am'),
    acordes.Acorde('F'),
))  # C G Am F

print(progressoes.Progressao.parse('C G Am F'))  # C G Am F
```

Além da funcionalidade dos métodos `semitom` e `tom`, que funcionam de maneira semelhante para os acordes e notas, tem-se também o método `transpor`. Esta funcionalidade, como o próprio nome sugere, transpõe a progressão de acordes, porém, ao invés de tomar como base um intervalo, toma-se como referência a tônica de destino para o primeiro acorde da progressão. Veja um exemplo:

```python
print(progressoes.Progressao.parse('C G Am F').transpor('D'))  # D A Bm G
print(progressoes.Progressao.parse('C G Am F').transpor('Ab'))  # Ab Eb Fm Db
print(progressoes.Progressao.parse('C G Am F').transpor('F'))  # F C Dm A# 
print(progressoes.Progressao.parse('C G Am F').transpor('F', acidente='b'))  # F C Dm Bb 
```

## Contribuindo

Se você quiser contribuir para esta biblioteca, por favor, crie um pull request com as suas alterações ou abra uma nova issue para discutir ideias.

## Licença

Esta biblioteca está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.