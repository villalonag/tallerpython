'''
Autor: Gabriel Villalona
Descripcion: Programa que solicita los datos personales
fecha: 15- Mayo -2021
'''
#Taller de Programacion con Python
import os
os.system("cls")

print('****Bienvenidos a su primer programa de python****')

nombre = input('Por favor colocar sus nombres: \n')

apellidos = input('Por favor colocar sus apellidos: \n')

nombreCompleto =  nombre  + ' '+  apellidos

edad = input('inidique su edad: \n')

edad = int(edad) #Esta linea convierte el dato edad de string a int o entero

peso = input('inidique su peso: \n')

peso = float(peso)#Esta linea convierte el dato edad de string a flotante o tipo de dato con punto decimal

enSalud = input('Esta en salud salud actualmente ? Escribir  True para SI y False para NO \n')

enSalud = bool(enSalud) 

print('Su nombre es: ',nombreCompleto)

print('Su edad es: ', edad)

print('Su peso es: ',peso)

print('Su estaod de Salud es: ', enSalud)



