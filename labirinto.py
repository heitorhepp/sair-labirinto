labirinto = [
    "I......####",
    "##.#..#.#..",
    ".###...#...",
    "#....##....",
    "##.....###.",
    "....##...#.",
    "...#...#..#",
    "......##...",
    "....#..#..#",
    "....##...#.",
    ".......#..F",
]

DIRECOES = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def achar(lab, simbolo):
    for i, linha in enumerate(lab):
        if simbolo in linha:
            return i, linha.index(simbolo)


def livre(lab, i, j):
    dentro = 0 <= i < len(lab) and 0 <= j < len(lab[0])
    return dentro and lab[i][j] != "#"


def montar_grafo(lab):
    grafo = {}

    for i in range(len(lab)):
        for j in range(len(lab[0])):
            if not livre(lab, i, j):
                continue

            grafo[(i, j)] = []

            for di, dj in DIRECOES:
                vizinho = (i + di, j + dj)

                if livre(lab, vizinho[0], vizinho[1]):
                    grafo[(i, j)].append(vizinho)

    return grafo


def desenhar(lab, caminho):
    grade = [list(linha) for linha in lab]

    for i, j in caminho:
        if grade[i][j] == ".":
            grade[i][j] = "*"

    for linha in grade:
        print("".join(linha))


def dfs(grafo, inicio, saida):
    visitados = {inicio}
    pilha = [(inicio, [inicio])]

    while pilha:
        atual, caminho = pilha.pop()

        if atual == saida:
            return caminho, visitados

        for vizinho in grafo[atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                pilha.append((vizinho, caminho + [vizinho]))

    return None, visitados


def bfs(grafo, inicio, saida):
    visitados = {inicio}
    fila = [(inicio, [inicio])]

    while fila:
        atual, caminho = fila.pop(0)

        if atual == saida:
            return caminho, visitados

        for vizinho in grafo[atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append((vizinho, caminho + [vizinho]))

    return None, visitados


def gulosa(grafo, inicio, saida):
    visitados = {inicio}
    fila = [(inicio, [inicio])]

    while fila:
        melhor_indice = 0

        for i in range(1, len(fila)):
            casa = fila[i][0]
            melhor_casa = fila[melhor_indice][0]

            distancia = abs(casa[0] - saida[0]) + abs(casa[1] - saida[1])
            melhor_distancia = (
                abs(melhor_casa[0] - saida[0])
                + abs(melhor_casa[1] - saida[1])
            )

            if distancia < melhor_distancia:
                melhor_indice = i

        atual, caminho = fila.pop(melhor_indice)

        if atual == saida:
            return caminho, visitados

        for vizinho in grafo[atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append((vizinho, caminho + [vizinho]))

    return None, visitados


inicio = achar(labirinto, "I")
saida = achar(labirinto, "F")
grafo = montar_grafo(labirinto)

print("\n+----------+------------+-------------------+")
print("| Busca DFS                                 |")
print("+----------+------------+-------------------+\n")
caminho_dfs, visitados_dfs = dfs(grafo, inicio, saida)
desenhar(labirinto, caminho_dfs)

print("\n+----------+------------+-------------------+")
print("|Busca BFS                                  |")
print("+----------+------------+-------------------+\n")
caminho_bfs, visitados_bfs = bfs(grafo, inicio, saida)
desenhar(labirinto, caminho_bfs)

print("\n+----------+------------+-------------------+")
print("| Busca Gulosa                              |")
print("+----------+------------+-------------------+\n")
caminho_gulosa, visitados_gulosa = gulosa(grafo, inicio, saida)
desenhar(labirinto, caminho_gulosa)

print("\n+----------+------------+-------------------+")
print("| Busca    | Movimentos | Casas visitadas   |")
print("+----------+------------+-------------------+")
print(f"| DFS      | {len(caminho_dfs) - 1:^10} | {len(visitados_dfs):^17} |")
print(f"| BFS      | {len(caminho_bfs) - 1:^10} | {len(visitados_bfs):^17} |")
print(f"| Gulosa   | {len(caminho_gulosa) - 1:^10} | {len(visitados_gulosa):^17} |")
print("+----------+------------+-------------------+")