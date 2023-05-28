def caminho_maior_peso(grafo_copia, origem, destino, caminho):
    visitados[origem] = True

    if origem == destino:
        return caminho

    for vizinho, capacidade in enumerate(grafo_copia[origem]):
        if not visitados[vizinho] and capacidade > 0:
            proximo_caminho = caminho_maior_peso(
                grafo_copia, vizinho, destino, caminho + [(origem, vizinho)]
            )
            if proximo_caminho is not None:
                return proximo_caminho

    return None

def fluxo_maximo(grafo, origem, destino):
    grafo_copia = [list(row) for row in grafo]

    fluxo = 0

    while True:
        global visitados
        visitados = [False] * len(grafo)

        caminho = caminho_maior_peso(grafo_copia, origem, destino, [])

        if caminho is None:
            break

        capacidade_minima = min(grafo_copia[u][v] for u, v in caminho)

        for u, v in caminho:
            grafo_copia[u][v] -= capacidade_minima
            grafo_copia[v][u] += capacidade_minima

        fluxo += capacidade_minima

    return fluxo

