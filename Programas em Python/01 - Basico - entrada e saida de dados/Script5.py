# Faça um algoritmo que pergunte quanto você 
# ganha por hora e o numero de horas trabalhadas 
# no mes. Calcule e mostre o total do seu salário 
# no referido mes.

#entradas
valor_por_hora = float(input("Qual valor você ganha por hora? "))
horas_trabalhadas = int(input("Quantas horas você trabalhou neste mês? "))
#processamento
salario = horas_trabalhadas * valor_por_hora
#saída
print("Neste mês você vai receber R$ {0:.2f}".format(salario))