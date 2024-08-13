#Ejercicios Pair Programming
#--------------------------------------------------------------------------------------------------
#Problema 1
horas_de_trabajo = int (input("Por favor, ingrese sus horas de trabajo. \n"))
tarifa_por_hora = int (input("Por favor, ingrese su tarifa por hora de trabajo. \n"))
print ("Su Salario es de =" , horas_de_trabajo * tarifa_por_hora )
#--------------------------------------------------------------------------------------------------
#Problema 2
nombre = input ("Ingrese su nombre: ")
apellido = input ("Ingrese su nombre: ")
empresa = input ("Ingrese su nombre: ")
print (f"{nombre}.{apellido}@{empresa}.com")


#------------------------------------------------------------------------------------------------------

# Cree un programa que le pida al usuario su nombre, apellido, y edad, y muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.
print("Digite su nombre: ")
nombre = input()
print("Digite su apellido: ")
apellido = input()
print("Digite su edad: ")
edad = int(input())

if edad < 3:
    print(f"{nombre} {apellido} es bebé")
elif 3 <= edad < 13:
    print(f"{nombre} {apellido} es niño")
elif 13 <= edad < 18:
    print(f"{nombre} {apellido} es joven")
elif 18 <= edad < 30:
    print(f"{nombre} {apellido} es adulto")
else:
    print(f"{nombre} {apellido} es adulto mayor")

#----------------------------------------------------------------------
#Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero.

secret_number = 5

print ("Digite un número: ")
user_number = int(input())

while user_number != secret_number :

    print ("Digite un número: ")
    user_number = int(input())

print ("Numero correcto")
#-------------------------------------------------------------------------------------
#Cree un programa que le pida tres números al usuario y muestre el mayor.
numero_mayor = 0
contador = 0
while contador != 3:
    contador = contador + 1
    print(f"Ingrese numero {contador}")
    numero_ingresado = int(input())
    if numero_ingresado > numero_mayor :
        numero_mayor = numero_ingresado
    
print(f"El número mayor es {numero_mayor}")
#-------------------------------------------------------------------------
"""5. Dada `n` cantidad de notas de un estudiante, calcular:
   1. Cuantas notas tiene aprobadas (mayor a 70).
   2. Cuantas notas tiene desaprobadas (menor a 70).   
   3. El promedio de todas.
   4. El promedio de las aprobadas.
   5. El promedio de las desaprobadas."""
   
   
print("Ingrese la cantidad de notas que desea revisar:")
cantidad_de_notas = int(input())
cantidad_de_notas_aprobadas = 0
cantidad_de_notas_reprobadas = 0


lista_de_notas_aprobadas = []
lista_de_notas_reprobadas = []

ciclo = 0
while ciclo != cantidad_de_notas:
    ciclo = ciclo + 1

    print(f"Ingrese numero {ciclo}")
    numero_ingresado = int(input())
    if numero_ingresado >= 70 :
        cantidad_de_notas_aprobadas = cantidad_de_notas_aprobadas + 1
        lista_de_notas_aprobadas.append(numero_ingresado)
        
    elif numero_ingresado < 70:
        cantidad_de_notas_reprobadas = cantidad_de_notas_reprobadas + 1
        lista_de_notas_reprobadas.append(numero_ingresado)

promedio_total =  (sum(lista_de_notas_aprobadas)+ sum(lista_de_notas_reprobadas)) / cantidad_de_notas
promedio_de_aprobadas = (sum(lista_de_notas_aprobadas)) / cantidad_de_notas_aprobadas if cantidad_de_notas_aprobadas > 0 else 0
promedio_de_reprobadas = (sum(lista_de_notas_reprobadas)) / cantidad_de_notas_reprobadas if cantidad_de_notas_reprobadas > 0 else 0



print(f"El número de notas aprobadas es de: {cantidad_de_notas_aprobadas}")
print(f"El número de notas aprobadas es de: {cantidad_de_notas_reprobadas}")
print(f"El promedio total de notas es de: {promedio_total}")
print(f"El promedio  de notas aprobadas es de: {promedio_de_aprobadas}")
print(f"El promedio  de notas reprobadas es de: {promedio_de_reprobadas}")