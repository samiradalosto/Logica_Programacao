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
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Arredondar casas decimais 
s1 = n1 + n2 + n3 /3
round(s1),2
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Exemplo 3
def boas_vindas(nome, cargo,):
    print (f"olá, {nome}! Você é o novo {cargo}")

    boas_vindas("samira", "desenvolvedor")
    boas_vindas("carlos", "Gerente")

#Exemplo 4
def configurar_conxão(servidor, porta = 8080):
    print(f"Conectando a (servidor) na porta (porta)...")

    configurar_conxão("192.168.1.1") #Use a porta 800
    configurar_conxão("10.0.01", 3000) #use a porta 300



