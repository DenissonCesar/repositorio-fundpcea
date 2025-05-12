from main import analisar_numeros

numeros = [7, 22, 9, 10, 87, 12]

resultado = analisar_numeros(numeros)

print(f"Média: {resultado['media']}")
print(f"Maior número: {resultado['maior']}")
print(f"Menor número: {resultado['menor']}")
print(f"Quantidade de números pares: {resultado['pares']}")
