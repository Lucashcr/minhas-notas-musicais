# Minhas notas musicais

Esta é uma biblioteca em Python para fazer operações sobre notas, acordes, progressões e escalas musicais.

## Instalação
Para instalar a biblioteca, basta clonar o repositório:

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

### Acordes

O módulo acordes permite trabalhar com acordes musicais. É possível criar um acorde a partir de uma string que representa o seu nome ou utilizando-se o método de classe `parse`:

```python
# Criando um acorde maior
a = acordes.Acorde("C")

# Criando um acorde menor
a = acordes.Acorde("Am")
```

Vale salientar também que esta biblioteca também suporta a utilização de acordes com tensões:

```python
# Criando um acorde maior
a = acordes.Acorde("C9")

# Criando um acorde menor
a = acordes.Acorde("Am7(13)")
```

### Progressões

O módulo progressoes permite trabalhar com progressões de acordes. É possível criar uma progressão a partir de uma sequência de acordes ou utilizando-se o método de classe `parse`:

Criando uma progressão simples

```python
p = progressoes.Progressao(
    acordes.Acorde('C'),
    acordes.Acorde('G'),
    acordes.Acorde('Am'),
    acordes.Acorde('F'),
)
print(p)  # C G Am F

p = progressoes.Progressao.parse('C G Am F')
print(p)  # C G Am F
```

### Escalas

O módulo escalas permite trabalhar com escalas musicais. É possível criar uma escala a partir de uma string que representa o seu nome:

```python
# Criando uma escala maior
e = escalas.Escala("C", "maior")
print(e)  # C D E F G A B

# Criando uma escala menor
e = escalas.Escala("Am", "menor")
print(e)  # A B C D E F G

# Criando uma escala menor harmônica
e = escalas.Escala("Am", "menor-harmonica")
print(e)  # A B C D E F G#

# Criando uma escala menor melódica
e = escalas.Escala("Am", "menor-melodica")
print(e)  # A B C D E F# G#
```

## Contribuindo

Se você quiser contribuir para esta biblioteca, por favor, crie um pull request com as suas alterações ou abra uma nova issue para discutir ideias.

## Licença

Esta biblioteca está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.