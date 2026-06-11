# Exercicios 1 
# Calculos de notas por semestre onde terá duas notas formativas e uam nota somativa para encerar o semestre.
# Os valores de notas são 0 a 100
n1 = float(input('digite sua primeira nota \n'))
n2 = float(input('Digite sua segunda  nota \n'))
n3 = float (input('digite sua terceira nota \n'))
s1 =(n1 + n2 + n3  )/3
print("O resultado do calculo é: \n", s1)

n1 = float(input('digite sua primeira nota \n'))
n2 = float(input('Digite sua segunda  nota \n'))
n3 = float (input('digite sua terceira nota \n'))
s2 =(n1 + n2 + n3  )/3
print("O resultado do calculo é: \n", s2)

print ("as notas do do primeiro semestre", s1)
print ("as notas do segundo semestre",s2)
#-------------------------------------------------------------#

#Arredondar casas decimais 
s1 = n1 + n2 + n3 /3
round(s1),2
#-------------------------------------------------------------#

#Exemplo 3
def boas_vindas(nome, cargo,):
    print (f"olá, {nome}! Você é o novo {cargo}")

    boas_vindas("samira", "desenvolvedor")
    boas_vindas("carlos", "Gerente")

#--------------------------------------------------------------#
#Exemplo 4
def configurar_conxão(servidor, porta = 8080):
    print(f"Conectando a (servidor) na porta (porta)...")

    configurar_conxão("192.168.1.1") #Use a porta 800
    configurar_conxão("10.0.01", 3000) #use a porta 300

#--------------------------------------------------------------#

#Exercicio 5 
#Fça uma tabuada 
print("vamos fazer a tabuada do 2 ")
s1  = float(input('digite o numéro \n'))
s2 = float(input('Digite os numéro \n'))
stotal = s1 * s2 
print('O seu resultado é: \n', stotal)

#--------------------------------------------------------------#

#Exercicio 6 
#Calculo de idade: Deve apresentar o nome, curso, data nascimento e aresentar a idade sua final 
nome = input("digite seu nome: \n")
# idade = input("digite sua idade: \n")
curso = input("digite seu curso: \n")
#data = int(input("digite sua data: \n"))
# print("Os resultados são: \n" + "Seu nome é: \n ", + "Seu curso é: \n" "E data \n" "sua idade", )

s1 =float(input('digite o ano \n'))
s2 =float(input('digite o ano atual \n'))
stotal = s2 - s1
print("qual é resutado: \n", stotal)

#--------------------------------------------------------------#

#Exercicio 7
#Calcular gorjetas receba o valor da gorjeta (considerando 10% do avlor da conta)
print("os 10% porcemto do garçon")
g1 = float(input('digite o primeiro valor \n'))
print("Essa gorgeta: \n", g1 * 10 / 100)
print("O valor total da conta: \n", g1 +(g1 * 10 / 100))

#--------------------------------------------------------------#

#Exercicio, 8
#Criar um sistema para calcular o sucessor e antecesor de um valor 
print("O sistema para calcular")
v1 = float(input('Digite um numéro: \n'))
print(v1 - 1)
print(v1 + 1)

#--------------------------------------------------------------#

#Exercicio 9
# criar um algoritimo para calcular a venda de livros e que toda venda aprente um desconto fixo de 5%
print("Algoritimo para calcular")
e1 = float(input('Digite o valor do livro: \n'))
print("esse e o desconto: \n", e1 * 5 / 100)
print("O valor total da conta: \n", e1 - (e1 * 5 / 100))

#--------------------------------------------------------------#

def saudacao (nome):
    return f"Olá, {nome}!"

mensagem = saudacao ("samira")
print(mensagem)
#..............................................................#
#Exemplo 2 
nome = input("seu nome:")
idade = int(input("sua idade:"))#Converte texto para inteiro
print(f"{nome} tem {idade} anos.")
#..............................................................#