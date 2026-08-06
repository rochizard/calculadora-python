seguir = "si"

while seguir == "si":
    print("="*25)
    print("🧮 CALCULADORA 🧮")
    print("=" * 25)
    
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    
    operación= input("Con cuál opción quieres operar?\n1.sumar\n2.restar\n3.multiplicar\n4.dividir").strip()
    if operación =="1":
        sumar1= int(input("Cuál es el primer número que querés sumar?"))
        sumar2=int(input("Cuál es el segundo número que querés sumar?"))
        print ("El resultado es:",sumar1+sumar2)
    elif operación == "2":
        restar1= int(input("Cuál es el primer número que querés restar?"))
        restar2=int(input("Cuál es el segundo número que querés restar?"))
        print ("El resultado es:",restar1-restar2)
    elif operación == "3":
       multiplicar1= int(input("Cuál es el primer número que querés multiplicar?"))
       multiplicar2=int(input("Cuál es el segundo número que querés multiplicar?"))
       print ("El resultado es:",multiplicar1*multiplicar2)
    elif operación=="4":
        dividir1= int(input("Cuál es el primer número que querés dividir?"))
        dividir2= int(input("Cuál es el segundo número que querés dividir?"))
        print("El resultado es:",dividir1/dividir2)
    else:
        print("Esa opción no existe.")
    seguir=input("Querés hacer otra cuenta? si/no").strip().lower()
print("Chau!")
        
