# Vamos "não" mexer com tuplas, ou seja, tuplas são imutáveis, ou seja, não podem ser alteradas depois de criadas. Elas são usadas para armazenar dados que não devem ser modificados, como coordenadas geográficas, datas, etc.

tupla = (1, 2, 3, 4, 5)  # Criando uma tupla com 5 elementos

print(tupla[0])  # Acessando o primeiro elemento da tupla (1)
print(tupla[1])  # Acessando o segundo elemento da tupla (2)

#  tupla só é usada em coisas que não devem mudar tipo dia da semana, meses do ano, etc. Se precisar de uma estrutura de dados mutável, use uma lista.
