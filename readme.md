# Busca em Labirinto: DFS, BFS e Busca Gulosa

Atividade de Inteligência Artificial: implementar três algoritmos de busca em um labirinto próprio e comparar os resultados.

## O labirinto

Labirinto de **11 × 11**, desenhado por mim. Legenda:

- `I` = início, em `(0, 0)`
- `F` = saída, em `(10, 10)`
- `.` = caminho livre
- `#` = parede

```
I......####
##.#..#.#..
.###...#...
#....##....
##.....###.
....##...#.
...#...#..#
......##...
....#..#..#
....##...#.
.......#..F
```

Ele tem várias rotas possíveis até a saída, de tamanhos diferentes, e vários becos sem saída que obrigam a busca a voltar. Os movimentos são só nas 4 direções (cima, direita, baixo, esquerda), sem diagonais.

## Como funciona

O labirinto é convertido em um **grafo**: cada casa livre é um nó, ligado às casas livres vizinhas. As paredes não entram no grafo.

Os três algoritmos têm a mesma estrutura: uma lista de casas a explorar, onde cada item guarda a casa e o caminho percorrido até ela, e um conjunto de casas já visitadas. A diferença é **qual item sai da lista a cada passo**:

| Algoritmo | Qual item sai da lista | Estrutura |
|---|---|---|
| **DFS** (busca em profundidade) | o último que entrou | pilha |
| **BFS** (busca em largura) | o primeiro que entrou | fila |
| **Busca Gulosa** | o mais perto da saída (distância de Manhattan) | lista com busca do menor |

Cada algoritmo retorna `(caminho, casas_visitadas)`. As "casas visitadas" são as casas descobertas, ou seja, as que entraram na lista durante a busca.

## Como executar

```bash
python main.py
```

Não precisa instalar nada, só o Python 3.

## Resultados

Os caminhos encontrados (`*` marca o caminho):

**DFS**
```
I****..####
##.#*.#.#..
.###*..#...
#.***##....
##*....###.
***.##...#.
*..#...#..#
*.....##...
*...#..#..#
*...##***#.
*******#**F
```

**BFS**
```
I****..####
##.#*.#.#..
.###*..#...
#...*##....
##..***###.
....##***#.
...#...#*.#
......##*..
....#..#*.#
....##..*#.
.......#**F
```

**Busca Gulosa**
```
I*****.####
##.#.*#.#..
.###**.#...
#...*##....
##..***###.
....##***#.
...#...#**#
......##.*.
....#..#**#
....##..*#.
.......#**F
```

Tabela comparativa:

| Busca  | Movimentos | Casas visitadas |
|--------|:----------:|:---------------:|
| DFS    | 30         | 48              |
| BFS    | 20         | 71              |
| Gulosa | 24         | 35              |

## Análise

**Por que a BFS encontrou o menor caminho e a DFS não.**
A BFS explora o labirinto por camadas: primeiro todas as casas a 1 passo do início, depois as a 2 passos, e assim por diante. Como todo passo custa o mesmo, a primeira vez que ela chega na saída é pelo menor número de passos possível. O resultado, 20, é o mínimo teórico, porque a distância em linha reta entre `I` e `F` já é 20 (10 linhas + 10 colunas). O preço é visitar mais casas (71).

A DFS escolhe uma direção e vai até o fim dela, voltando só quando trava, e devolve o primeiro caminho que chega na saída, sem comparar com outros. Aqui ela se separou da BFS em `(3, 4)`: em vez de descer para `(4, 4)`, foi para a esquerda, `(3, 3)`, desceu pela coluna 0 e atravessou todo o fundo do labirinto, chegando em 30 movimentos.

**Em que ponto a Busca Gulosa foi induzida ao erro por uma parede.**
A gulosa só olha a distância até a saída e ignora quanto já andou e o que existe entre ela e a saída. Isso a enganou duas vezes:

1. Em `(0, 4)`, as casas `(0, 5)` e `(1, 4)` estão empatadas (distância 15) e ela escolheu `(0, 5)`. Seguiu por `(1, 5)` e `(2, 5)`, chegando a distância 13, mas ali há uma parede em `(3, 5)` bloqueando a descida. Precisou recuar para `(2, 4)`, onde a distância subiu para 14.
2. Em `(6, 8)`, houve outro empate (distância 5) e ela foi para `(6, 9)`. Desceu até `(8, 9)`, onde a parede em `(9, 9)` fecha o caminho, e voltou para `(8, 8)`.

Cada desvio custou 2 movimentos a mais, o que explica os 24 contra os 20 da BFS. Por outro lado, ela visitou só 35 casas, bem menos que as outras.

## Arquivos

- `main.py`: o labirinto, a construção do grafo, os três algoritmos, o desenho dos caminhos e a tabela.
- `README.md`: este arquivo.