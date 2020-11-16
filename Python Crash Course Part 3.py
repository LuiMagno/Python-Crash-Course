# Iteradores
# FOR
lista = [1,2,3,4,5]
# O for serve para iterar sobre um iterável e executar um certo bloco de código para cada item presente na lista
print('1. ')
for item in lista: # 'item' aqui pode ser qualquer palavra
    print(item)

# WHILE
i = 1
print('2. ')
while i < 5:
    print('i is: {}'.format(i))
    i = i+1

# RANGE É UM GERADOR
# Ou seja, ele sempre gera um objeto iterável com começo e fim, tipo:

lista = range(0,10)
print('3. ', lista)

for item in lista:
    print('hi!')
# Ou, podemos fazer essa mesma coisa dessa forma
print('4. ')
for x in range(0,5):
    print('Eu vim ver o macaco')


# List compreenshion 

x = [1,2,3,4]
out = []
for num in x:
    out.append(num**2)
print('5.', out)

# Podemos economizar todo esse código utilizando compreensão em listas:
out = [num**2 for num in x] 
#      Me dê o quadrado do num em x - Para cada num in x me dê num**2 (fácil)
print('6.', out)

# Revisando funções!

def my_func(name = 'Default Name'): # Se eu escrever o parametro 'name' dessa forma, toda vida que a função for chamada e os parâmetros estiverem vazios, o 'Default Name' vai entrar
    print('7. Hello '+name)
# Como nesse exemplo
my_func()
my_func('Lui')