import time
nombre=input("Como te llamas? ")
print("Hola, "+nombre," es hora de jugar")
print(" ")
time.sleep(1)
print("Comienza a adivinar")
time.sleep(0.5)
palabra="ahorcado"
tupalabra=" "
vidas=5

while vidas > 0:
    fallas=0
    for letra in palabra:
        if letra in tupalabra:
            print(letra,end="")
        else:
            print("_",end="")
            fallas+=1
    if fallas==0:
        input()
        print(" ")
        print("Felicidades, ganaste")
        input(" ")
        break

    tuletra=input("introduce una letra: ")
    tupalabra+=tuletra

    if tuletra not in palabra:
        vidas-=1
        print("Ups, te equivocaste")
        print("Te quedan",+vidas," vidas")
    if vidas== 0:
        print("Perdiste!")
else:
    input()
    print("Gracias por participar")
    input()
