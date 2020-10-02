#crear ciclo for que permita ingresar n numeros ingresados x teclado
#calcular y mostrar: cantidad de numeros pares y canrtidad de numeros imparres


veces=int(input("Cuantos números ingresa?: "))
par=0
impar=0
for x in range(veces):
    nume=int(input("Ingrese un número: "))
    if (nume%2==0):
        par=par+1
    elif(nume%2!=0):
        impar=impar+1

print("La cantidad de números pares es: " + str(par))
print("La cantidad de números impares es: " + str(impar))5
