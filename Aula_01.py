a = int(input('Entre com o primeiro valor:'))
b = int(input('Entre com o segundo valor:'))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
resultado = print('soma: {soma}. \nsubtracao: {subtracao}. '
      '\nmultiplicacao: {multiplicacao}'
      '\ndivisao: {divisao}'
      '\nresto: {resto}' .format(soma=soma,
subtracao=subtracao,
resto=resto,
multiplicacao=multiplicacao,
divisao=divisao))

print(resultado)

