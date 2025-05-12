def analisar_numeros(lista):
    media = sum(lista) / len(lista)
    maior = max(lista)
    menor = min(lista)
    pares = sum(1 for n in lista if n % 2 == 0)

    return {
        "media": round(media, 2),
        "maior": maior,
        "menor": menor,
        "pares": pares
    }
