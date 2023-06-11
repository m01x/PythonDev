import random

player = input("Bienvenido al simulador de combates, Como te llamas: ")
print("\n")
print("Vas a enfrentar a Ogron el terrible!!... escoge tu arma\n")
print("=== ID: 1 Katana: Pega 30, 1 golpe===\n")
print("=== ID: 2 Dagas Dobles: Pega 10, probabilidad de doble golpe ==\n")
weapon = int(input("Escoge tu arma, Ingresa el ID: "))
rounds = int(input("Cuantas rondas vas a pelear: "))

confirm=input("Vamos a comenzar el combate, estas seguro de Iniciarlo? S/N\n")
if confirm=="s":
    print("---------------------------> iniciando el combate pactado a "+str(rounds)+" Entre Ogron el Peligroso vs "+player+" !!")
    print("******************************************************************")
    print("\n")
    print(" O H H H !!! NO0O0O0O0!!!!! Ogron esta transformandose en "+player+"...!!! Pelearas contra tu reflejo!!! mucha suerte!!!")
    print("\n")
    print("++++++++++++++++++===============E M P I E Z A   E L   C O M B A T E ================++++++++++++++++++\n")
    asalto=1
    dmgPlayer_total=0
    dmgPlayer_daga1=0
    dmgPlayer_daga2=0
    dmgOgron_daga1=0
    dmgOgron_daga2=0
    dmgOgron_total=0
    while asalto <= rounds:
        if weapon == 1:
            #TODO pasar a funcion el calculo de damagess.
            #Katana, atk 30 1 hit
            dmgPlayer = random.randint(1,30)
            dmgOgron = random.randint(1,30)
            anunciador="Le has inflingido "+str(dmgPlayer)+" a Ogron... y Ogron te ha inflingido "+str(dmgOgron)+"."
        else:
            #Dual Dagas, atk 10 , 50% chande double hit
            chance=int(random.randint(1,100))
            if chance>=50:
                dmgPlayer_daga1 = random.randint(1,10)
                dmgPlayer_daga2 = random.randint(1,10)
                dmgOgron_daga1 = random.randint(1,10)
                dmgOgron_daga2 = random.randint(1,10)
                dmgOgron = dmgOgron_daga1 + dmgOgron_daga2
                dmgPlayer = dmgPlayer_daga1 + dmgPlayer_daga2
                anunciador="GUAU!! HAN LANZADO DOBLES GOLPES!! Ogron Te ha golpeado con "+str(dmgOgron_daga1)+"+"+str(dmgOgron_daga2)+"("+str(dmgOgron)+") puntos de daño, mientras que "+str(player)+" ha inflingido "+str(dmgPlayer_daga1)+"+"+str(dmgPlayer_daga2)+"("+str(dmgPlayer)+") de daño."
            else:
                dmgPlayer = random.randint(1,10)
                dmgOgron = random.randint(1,10)
                anunciador="Le has inflingido "+str(dmgPlayer)+" a Ogron... y Ogron te ha inflingido "+str(dmgOgron)+"."
        dmgPlayer_total = dmgPlayer_total + dmgPlayer
        dmgOgron_total = dmgOgron_total + dmgOgron
        print("RONDA: "+str(asalto)+" "+str(anunciador)+".")
        asalto=asalto+1
    print(">>>>>>>>>>>>> FIN DEL ENCUENTRO <<<<<<<<<<<<<<<")
    if dmgPlayer_total > dmgOgron_total:
        print("El ganador es :"+player+"!!!! FELICIDADES\n")
    elif dmgPlayer_total < dmgOgron_total:
        print("HAS MUERTO: Ogron te ha derrotado.... No te preocupes, intentalo nuevamente\n")
    else:
        print("Tenemos un EMPATE!!!\n")
    print("\n**************************\n")
    print("Ogron inflingio: "+str(dmgOgron_total)+" de daño.")
    print(str(player)+" Inflingio: "+str(dmgPlayer_total)+" de daño.")
else:
    print("Gallina...")


