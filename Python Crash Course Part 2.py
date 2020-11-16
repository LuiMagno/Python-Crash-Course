# Dictionaries 

d = {'key1': 'value', 'key2': 123}
print('1. ', d['key1'])
print('2. ', d['key2'])

# A chave do dicionário pode guardar diferentes tipos de dados, desde strings e números até listas e outros dicionários

d1 = {'k1': [1,2,'TARGET']}
print('3. ', d1['k1'][2]) # Aqui estamos acessando a informação da 'k1' e obtendo o número dentro da lista

# Podemos fazer o mesmo que fizemos com as listas encadeadas e criar dicionários encadeados

dic = {'k1': {'innerkey': [1,'TARGET',2]}} # Aqui temos um dicionário dentro de outro dicionário
print('4. ', dic['k1']['innerkey'][1])

# Tuples 

t = (1,2,3)
print('5. ', t[0]) # Temos uma diferença crucial entre listas e tuplas -> tuplas não aceitam atribuições depois que são feitas. 
# Se eu fizer isso -> t[0] = 'new' irei receber um erro de "'tuple' object does not support item assignment"

# Sets

sets = {1,2,3,4,5,1,1,1,1,1,2,2,2,2,3,3,3} # Set não aceita elementos repetidos, só elementos únicos
print('6. ', sets)
lista = [1,2,3,1,1,1,1,1] 

print('7. ', set(lista)) # Set também é um método utilizado para transformar listas em sets

# Comparison Operators

print('8. ', 1 > 2)

print('9. ', 1 < 2)

print('10.', 1 >= 2)

print('11.', 1 <= 2)

print('12.', 1 == 1)

print('13.', 1 == 2)

print('14.', 1 != 2)

print('15.', 1 != 1)

print('16.', 'hi' == 'bye')

print('17.', 1 < 2 and 2 < 3 )

print('18.', (1<2) and (2>3))

print('18.', (1<2) or (2>3))

# If, else and elif -> também são operadores de comparação

# Aqui neste exemplo temos uma noção de como esses 3 funcionam

if 1 == 2:
    print('First')
elif 4 == 4:  # Por mais que '3 == 3' seja verdadeiro, a sequência de de elif só passa para o próximo se a condição não for aceita
    print('19. second')
elif 3 == 3:
    print('Third')
else:
    print('last')