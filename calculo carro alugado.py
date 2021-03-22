print("Olá, somos a TraSantos aluguéis de carros, seja bem-vindo(a) ao nosso sistema de cálculo sobre seus gastos")
nome = str(input("Digite o seu nome:"))
inicioano = int(input("Digite o ano do aluguel, no formato AAAA:"))
iniciomes = int(input("Digite o mês do aluguel, no formato MM:"))
iniciodia = int(input("Digite o dia do aluguel, no formado DD:"))
finalano = int(input("Digite o ano de entrega, no formato AAAA:"))
finalmes = int(input("Digite o mês de entrega, no formato MM:"))
finaldia = int(input("Digite o dia de entrega, no formato DD:"))

ano = finalano - inicioano
mes = finalmes - iniciomes
dia = finaldia - iniciodia

valor_ano = ano * 365
valor_mes = mes * 30
qnt_dias = valor_ano + valor_mes + dia
valor_dias = qnt_dias * 60

iniciokm = float(input("Digite a quilometragem inicial:"))
finalkm = float(input("Digite a quilometragem final:"))

totalkm = finalkm - iniciokm
valorkm = totalkm * 0.15
Valortotal = valorkm + valor_dias

print("Você utilizou o carro por", qnt_dias, "Dias")
print("Você rodou", totalkm, "quilometros")
print("O aluguel diário do carro custa 60 R$, seu custo total do aluguel foi: R$", valor_dias)
print("O valor cobrado por quilometro rodado é 0.15, seu custo total foi: R$", valorkm)
print(" O valor total a ser pago é: R$", Valortotal)
print(nome, ",Agradecemos sua preferência ")
