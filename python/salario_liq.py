valor_hora = float(input())
horas_trabalhadas = float(input())
salario_bruto = valor_hora * horas_trabalhadas 
inss = (salario_bruto * 0.08)
imposto_renda = (salario_bruto * 0.11)
sindicato = (salario_bruto * 0.05)
salario_liq = salario_bruto - inss - imposto_renda - sindicato

print (f'{salario_bruto:.2f}')
print (f'{inss:.2f}')
print (f'{imposto_renda:.2f}')
print (f'{sindicato:.2f}')
print (f'{salario_liq:.2f}')