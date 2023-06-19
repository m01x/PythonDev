import random

def normalAttack():
    ataque = random.randint(1,100)
    if ataque <= 60:
        return True
    else:
        return False
    
def warriorSkill():
    dice=random.randint(1,100)
    if dice>=1 and dice<=10:
        skill = [" ha desencadenado su  GOLPE RADIANTE†††, cortando la dimensión, inflingiendo ",500]
    elif dice>=11 and dice<=50:
        skill = [" rapidamente ha girado en espiral, acertando una Estocada en reversa, inflingiendo ",150]
    elif dice>=51 and dice<=80:
        skill = [" en un segundo, realizo un Desenvaine de sangre, lanzando por los aires a su rival, inflingiendo ",300]
    else:
        skill = [" perdio el equilibrio y comenzó a vomitar sangre... afectado/a por un Colapso cardíaco, inflinge ", 2]
    return skill

def mageSkill():
    dice=random.randint(1,100)
    if dice>=1 and dice<=10:
        skill = [" ha concentrado su mana en el vacío, canalizando materia oscura...LANZASTE UN RAYO LA CONCHALALORA!! inflingiendo ",800]
    elif dice>=11 and dice<=50:
        skill = [" Invocó dos Vermis de Mana: Han atacado DOS VECES💥💥( 80 + 80 ) ",160]
    elif dice>=51 and dice<=80:
        skill = [" apunto su baculo y lanzo truenos radiantes *SHINGG*!!, infliengiendo (trueno) ",200]
    else:
        skill = [" súbitamente perdió la luz, un mareo intenso imposibilita liberar todo su poder... inflinge ", 0]
    return skill

def thiefSkill():
    dice=random.randint(1,100)
    if dice>=1 and dice<=10:
        skill = ["  ",400]
    elif dice>=11 and dice<=50:
        skill = [" ",150]
    elif dice>=51 and dice<=80:
        skill = [" ",300]
    else:
        skill = [" ", 2]
    return skill


