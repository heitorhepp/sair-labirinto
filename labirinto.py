labirinto = [
    "I...#.......",
    ".####.#.#.#.",
    "......#.##..",
    ".##.#.#....#",
    ".#.##......#",
    "....##......",
    "##.#........",
    "............",
    "............",
    "............",
    "............",
    "...........F",
]

# caminho2 = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (1, 3), (1,4),
#             (1,5), (0,5), (0,6), (0,7), (0,8)]

def achar(lab, simbolo):
    for i, linha in enumerate(lab):
        if simbolo in linha:
            return (i, linha.index(simbolo))
inicio = achar(labirinto, 'I')   # (0, 0)
saida  = achar(labirinto, 'F')   # (11, 11)


DIRECOES = [(-1, 0), (0, 1), (1, 0), (0, -1)]   # ↑ → ↓ ←
def livre(lab, i, j):
    dentro = 0 <= i < len(lab) and 0 <= j < len(lab[0])
    return dentro and lab[i][j] != '#'
def montar_grafo(lab):
    grafo = {}
    for i in range(len(lab)):
        for j in range(len(lab[0])):
            if not livre(lab, i, j):
                continue
            grafo[(i, j)] = []
            for di, dj in DIRECOES:
                if livre(lab, i + di, j + dj):
                    grafo[(i, j)].append((i + di, j + dj))
    return grafo
grafo = montar_grafo(labirinto)


def desenhar(lab, caminho):
    grade = [list(linha) for linha in lab]
    for i, j in caminho:
        if grade[i][j] == '.':
            grade[i][j] = '*'
    for linha in grade:
        print(''.join(linha))
# caminho escrito à mão, só para testar
caminho = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (1, 3), (1,4),
            (1,5), (0,5), (0,6), (0,7), (0,8), (0,9), (0,10), (1,10), (2,10), (3,10)]

caminho2 = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (1, 3), (1,4),
            (1,5), (2,5), (2,6), (3,6), (4,)]


desenhar(labirinto, caminho)
print()
desenhar(labirinto, caminho2)


# labirinto = [...]   # o seu, mínimo 10 × 10
# grafo = montar_grafo(labirinto)
# def dfs(grafo, inicio, saida): ...
# def bfs(grafo, inicio, saida): ...
# def gulosa(grafo, inicio, saida): ...
# cada uma devolve (caminho, casas_visitadas)
# desenhar(labirinto, caminho)   # para cada uma