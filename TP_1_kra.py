print("Hola profe lo que me acuerdo de python es esto:")
while True:
    num1=int(input("Ingrese un numero: "))
    num2=int(input("Ingrese un numero: "))
    opcion=input("Que funcion desea usar?: 1) Suma 2) Resta 3) Multiplicacion 4) Division (Ingrese 0 para terminar)")
    if opcion=="1":
        print("sus numeros son: ",num1,"y",num2)
        print("La suma es: ",num1+num2)
    elif opcion=="2":
        print("sus numeros son: ",num1,"y",num2)
        print("la resta de sus numeros es:",num1-num2)
    elif opcion=="3":
        print("sus numeros son: ",num1,"y",num2)
        print("la multiplicacion de sus numeros es: ",num1*num2)
    elif opcion=="4":
        print("sus numeros son: ",num1,"y",num2)
        print("la division de sus numeros es: ",num1/num2)
    if opcion=="0":
        break