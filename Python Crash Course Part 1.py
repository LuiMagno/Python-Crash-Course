# Data Types

# Numbers

result = 1 + 1
print('1. ', result)

result = 1 * 3
print('2. ', result)

result = 1 / 2
print('3. ', result)

result = 2 ** 4
print('4. ', result)

result = 4 % 2 # Aqui nós temos o %, que apresenta o resto da divisão de x por y
print('5. ', result)

result = 5 % 2
print('6. ', result)

result = (2+3) * (5+5)
print('7. ', result)
print('-'*100)

# Variable Assignment

# Nós não podemos iniciar uma variável com números ou caracteres especiais!
x = 2
y = 3
z = x + y
name_of_var = 12
print('8. ', z)
x = x + x # Aqui temos uma nova instância da variável X, que agora tem outro valor.
print('9. ', x)

# Strings

str1 = 'single quote'
str2 = "double quotes"
str3 = "Eu preciso 'daquela' coisa." # Utilizamos aspas simples e duplas quando ocorre algo como no exemplo (ou escrevendo em inglês).
str4 = "Please, I'm very busy today, ask me tomorrow." # Aqui um exemplo onde usamos os dois tipos de aspas.

x = 'hello'
print('10.', x)

num = 12
name = 'Lui'
print('11.', 'My number is {}, and my name is {}'.format(num, name))

print("12.", "My number is {one}, and my name is {two}. Let's prove here that use that type of format is great! Name - {two}, Number - {one}!".format(one=num, two=name))

s = 'hello'

print('13.', s[0])
print('14.', s[4])

s = 'abcdefghjk'
print('15.', s[0:]) # A partir do 0, pegue tudo além dele (incluindo ele)
print('16.', s[:3]) # Pegar tudo até o 3 (Não incluindo ele)
print('17.', s[3:]) # Pegar tudo depois do 3 (Incluindo ele)
print('18.', s[3:6]) # Aqui vamos pegar tudo a partir do 3 (incluindo ele) até o 6 (não incluindo ele), conseguindo um 'def'

# Lists

my_list = ['a','b', 'c']
my_list.append('d')
print('19.',my_list)

print('20.', my_list[1:]) # Usando a mesma noção de indexação para listas (como foi usado em strings)
my_list[0] = 'NEW'
print('21.', my_list) # Também posso reassimilar itens da lista utilizando os index

nested_list = [1,2,[1,2,3]] # Também podemos criar listas encadeadas, uma dentro da outra, tipo Inception
print('22.',nested_list[2][2]) # Essa é a maneira de acessar itens da lista encadeada 
print('23.', nested_list[2]) # ou somente a lista que desejamos dentro da lista encadeada

nested_inception = [1,2,3,[4,5,[1,2,[1,2,'target']]]] # Listas encadeadas podem se tornar complicadas, mas nada muito assustador. Vamos acertar o 'target'
print('24.', nested_inception[3][2][2][2])