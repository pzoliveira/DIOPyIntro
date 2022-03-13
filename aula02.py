a = int(input('Entre o primieiro valor: '))
b = int(input('Entre o segundo valor: '))
soma = a + b
diferenca = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
print('Soma: {v1}\nSubtração: {v2}\nMultiplicação: {v3}\nDivisão: {v4}\nResto: {v5}'.format(v5=resto, v4=int(divisao), v3=multiplicacao, v2=diferenca,
                                                                                             v1=soma))
