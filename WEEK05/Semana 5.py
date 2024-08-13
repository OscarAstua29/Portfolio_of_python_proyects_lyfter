#cree un programa que itere e imprima un string letra por letra de derecha a izquierda.

my_string = "Pizza con piña"


for index in range (len(my_string) -1,-1,-1):
    print(my_string[index])

#Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.

my_list = [4, 3, 6, 1, 7,]


##for index in range (len(my_list)):(preguntar en el 1:1)

last_item = my_list.pop(-1)#(index)
my_list.insert(0,last_item )
fist_item = my_list.pop(1)
my_list.append(fist_item)

print(my_list)

#Cree un programa que elimine todos los números impares de una lista.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

i= 0 

while i < len(my_list):
    if my_list[i] % 2 != 0: 
        del my_list[i]

    else:
        i=i+1
print(my_list)


#Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.
ciclo_numero=1
numero_mayor = 0
lista_de_numeros = []
while ciclo_numero < 11:
    
    numero_ingresado = int(input(f"Ingrese numero {ciclo_numero}: ")) 

    lista_de_numeros.append(numero_ingresado)

    if numero_ingresado > numero_mayor:
        numero_mayor = numero_ingresado
    ciclo_numero = ciclo_numero + 1

print(lista_de_numeros)
print(f"El número mayor es {numero_mayor}")  