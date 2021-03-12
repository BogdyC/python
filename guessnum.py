import random
tryguess = 0
minnum = 1
maxnum = 15
print("Hola! ¿Cuál es tu nombre?")
uname = input()
randnum = random.randint(minnum, maxnum)
print("Hola, " + uname + "! Estoy pensando en un número entre el " + str(minnum) + " y el " + str(maxnum))
while tryguess < 6:
    print("Dime un numero")
    guess = input()
    guess = int(guess)
    tryguess = tryguess + 1
    if guess < randnum:
        print("Tu número es demasiado bajo")
    if guess > randnum:
        print("Tu número es muy alto")
    if guess == randnum:
        break
if guess == randnum:
    print("Buen trabajo," + uname + ", adivinaste mi número en " + str(tryguess) + " Intentos")
if guess != randnum:
    print("En realidad, mi numero era el " + str(randnum))
