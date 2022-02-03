
#Ejercicios de Tipos de Datos Simples

#Ejercicio 1
#Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable
# y luego muestre por pantalla el contenido de la variable.

n = 'Hola Mundo'
print(n)

#Ejercicio 2
#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario
# lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario
# haya introducido.

print('Introduzca su nombre')
name = input()
print('¡Hola' + name + '!')

#Ejercicio 3
#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora.
#Después debe mostrar por pantalla la paga que le corresponde.

print('¿Cuantas horas ha trabajado?')
horas = float(input())

print('¿Y cual es su precio por hora?')
precio = float(input())

print("Usted ha ganado " , precio * horas, " €" )


#Ejercicio 4
#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%.
#Escribir un programa que comience leyendo el número de barras vendidas que no son del día.
#Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser
# fresca y el coste final total.

print('¿Cuantas barras de pan va a comprar?')
barras = float(input())

precio_habitual = 3.49

descuento = 0.6

total = precio_habitual * barras * descuento

print('Precio habitual de una barra: ', precio_habitual,' € \nDescuento del día: ', descuento, '\nTotal: ', round(total, 2), ' € ')



#Ejercicio 5
#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal
# y lo almacene en una variable, e imprima por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es
# el índice de masa corporal calculado redondeado con dos decimales.

print("Digame su estatura: ")
altura = float(input())

print("Digame su peso: ")
peso = float(input())

imc = round(float(peso)/float(altura)**2.2)

print("Tu imc es de: ", imc)


##Ejercicios de Cadenas

#Ejercicio 1
#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por
#pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

nombre = input('¿Como te llamas? ')
numero = input('Introduzca un número entero ')
print((nombre + '\n')*int(numero))