def pertence_fibonacci(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    if b == numero or numero == 0:
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} NÃO pertence à sequência de Fibonacci."

numero = int(input("Digite um número: "))
print(pertence_fibonacci(numero))