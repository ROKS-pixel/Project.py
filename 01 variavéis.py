faturamento = 1100  #numero inteiro
custo = 600


print("Faturamento", faturamento)
novas_vendas = 1000

faturamento = faturamento + novas_vendas

imposto = 0.15 * faturamento #float
print("Imposto", imposto)
lucro = faturamento - custo - imposto
print("Faturamento", faturamento)
print("Custo", custo)
print("Lucro", lucro)


mensagem = "O lucro foi de 2100 " #string
teve_lucro = True #boolean

margen_lucro = lucro / faturamento
print("Margem de lucro", margen_lucro)

# int = numeros inteiros
# float = numeros de casa decimal
# atrings = textos 
# boolean = verdadeiro ou falso

#operadores especiais

#mod -> %
#resto da divisão de um numero pelo  outro
#10 % 3 

anos = int(310 / 12)
print("Anos", anos)

meses = 310 % 12
print(meses, "meses")


# floor division -> //
