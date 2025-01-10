import json

faturamento_mensal = '''
[{"dia": 1, "valor": 22174.1664}, {"dia": 2, "valor": 24537.6698}, {"dia": 3, "valor": 26139.6134}, 
{"dia": 4, "valor": 0.0}, {"dia": 5, "valor": 0.0}, {"dia": 6, "valor": 26742.6612}, 
{"dia": 7, "valor": 0.0}, {"dia": 8, "valor": 42889.2258}, {"dia": 9, "valor": 46251.174}, 
{"dia": 10, "valor": 11191.4722}]
'''

faturamento = json.loads(faturamento_mensal)

dias_validos = [dia["valor"] for dia in faturamento if dia["valor"] > 0]

menor = min(dias_validos)
maior = max(dias_validos)
media = sum(dias_validos) / len(dias_validos)
dias_acima_da_media = sum(1 for valor in dias_validos if valor > media)

print(f"Menor valor: R${menor:.2f}")
print(f"Maior valor: R${maior:.2f}")
print(f"Dias acima da média: {dias_acima_da_media}")
