tamanho = float(input())
velocidade = float(input())

velocidade = velocidade / 8

tempo = (tamanho / velocidade) / 60
tempo = "{:.2f}".format(tempo)
print(tempo)