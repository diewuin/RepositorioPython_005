#ingresar 2 numeros, mostrar la suma y multiplicacion de ambos
a=int(input("Digite un numero: "))
b=int(input("Digite un numero: "))
suma=a+b
multi=a*b
print("La suma de "+ str(a)+"y de "+ str(b)+ "Es igual a: "+ str(suma))
print("La multiplicacion de "+ str(a)+" y de "+ str(b)+ "Es igual a: "+ str(multi))
#estructura if
if(a>b):
    print("El numero "+str(a)+ "es mayor que el numero : "+str(b))
elif(a<b):
    print("El numero "+str(a)+ "es menor que el numero: "+str(b))
else:
    print("Los numeros son iguales.")