# map()
seq = [1,2,3,4,5]
print('hello')

def times2(var):
    return var*2

lista = list(map(times2, seq))
print('1.',lista)

# Lambda Expression

# Nós podemos transformar a função times2() em só uma linha:
t2 = lambda var: var*2
print('2.',t2(10))

# Assim eu posso transformar a linha 8 com o uso da função times2() e map() em apenas lambda e map(), olha só:
lista = list(map(lambda num: num*2, seq)) # E teremos o mesmo resultado
print('3.',lista)

# Basicamente transformar funções simples em expressões lambda mais simples e rápidas

# filter() Vamos filtar elementos de uma sequência

lista = list(filter(lambda num: num%2 == 0, seq))
print('4.', lista)

# methods
s = 'Hello my name is Lui'
print('5.',s.lower())
print('6.',s.upper())
print('7.',s.split())

# No método split() eu posso simplesmente separar a string por critérios dentro da string

print('8.',s.split('a'))
print('9.',s.split('a')[1])

d = {'k1': 1, 'k2': 2}
print('10.',d.keys())
print('11.',d.items())
print('12.',d.values())

lst = [1,2,3,4,5]
print('13.', lst.pop())
print('14.', lst.pop(0))
print('15.', lst)

# in

print('16.', 'x' in [1,2,3])

# tuple unpacking
x = [(1,2), (3,4), (5,6)] # lista de tuplas
print('17.')
for (a,b) in x: # Tirar itens individuais de listas de tuplas
    print(a)


'asdasdasd'