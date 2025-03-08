import Conjunto

#Conjunto do Numeros Naturais
N = Conjunto.Conjunto()

N.inserir(0)
N.inserir(1)
N.inserir(2)
N.inserir(3)
N.inserir(4)
N.inserir(5)
N.inserir("...")
print("Numeros Naturais\nN" + N.__str__())
print("N -> 1 |",N.contem(1))
print("N -> -20 |",N.contem(-20))
print("---------------------------")

#Conjunto dos Numeros Inteiros
Z = Conjunto.Conjunto()

Z.inserir("...")
Z.inserir(-3)
Z.inserir(-2)
Z.inserir(-1)
Z.inserir(0)
Z.inserir(1)
Z.inserir(2)
Z.inserir(3)
Z.inserir("...")
print("Numeros Inteiros\nZ" + Z.__str__())
print("Z -> -3 |",Z.contem(-3))
print("Z -> 5.9 |",Z.contem(5.9))
print("---------------------------")

#Conjunto dos Numeros Racionais
Q = Conjunto.Conjunto()

Q.inserir("...")
Q.inserir(-3/2)
Q.inserir(-1)
Q.inserir(0)
Q.inserir(1/2)
Q.inserir(2)
Q.inserir(3.5)
Q.inserir("...")
print("Numeros Racionais\nQ" + Q.__str__())
print("Q -> 0 |",Q.contem(0))
print("Q -> 1.4142 |",Q.contem(1.4142))
print("---------------------------")
