import random

def jogar():
    menu_principal_do_jogo()

    
def menu_principal_do_jogo():
    print("\n\n BEM VINDO AO JOGO DO BICHO\n\n")
    print("Escolha seu tipo de aposta:\n[1]Apostar no animal\n[2]Apostar na dezena")
    opcao_menu_principal = input("Qual opção? ")
    opcao_menu_principal = int(opcao_menu_principal)
    
    if(opcao_menu_principal == 1):
        apostar_no_animal()
    elif(opcao_menu_principal == 2):
        apostar_na_dezena()
    
def apostar_no_animal():
        print("\nAPOSTANDO NO ANIMAL\n")
        aposta = input("Qual animal deseja apostar? ")
        aposta = aposta.strip().lower()
        print ("Sua aposta foi: ", aposta)   
        
        acerca = input("Deseja apostar acerca ou em todos? ")
        acerca = acerca.strip().lower()
        if(acerca == "acerca"):
            acerca = True
        else:
            acerca = False 
        premio = define_animais(aposta, acerca)
        valor_premio(premio)  
            
def define_animais(aposta, acerca):
    animais = {
        'avestruz' : (1, 2, 3, 4),
        'aguia' : (5,6,7,8),
        'burro' : (9,10,11,12),
        'borboleta' : (13,14,15,16),
        'cachorro' : (17,18,19,20),
        'cabra' : (21,22,23,24),
        'carneiro' : (25,26,27,28),
        'camelo' : (29,30,31,32),
        'cobra' : (33,34,35,36),
        'coelho' : (37,38,39,40),
        'cavalo' : (41,42,43,44),
        'elefante' : (45,46,47,48),
        'galo' : (49,50,51,52),
        'gato' : (53,54,55,56),
        'jacare' : (57,58,59,60),
        'leao' : (61,62,63,64),
        'macaco' : (65,66,67,68),
        'porco' : (69,70,71,72),
        'pavao' : (73,74,75,76),
        'peru' : (77,78,79,80),
        'touro' : (81,82,83,84),
        'tigre' : (85,86,87,88),
        'urso' : (89,90,91,92),
        'veado' : (93,94,95,96),
        'vaca' : (97,98,99,00)
    }
        
    animal1 = None 
    animal2 = None
    animal3 = None
    animal4 = None
    animal5 = None
    
    primeira_dezena = random.randint(0, 99)
    segunda_dezena = random.randint(0, 99)
    terceira_dezena = random.randint(0, 99)
    quarta_dezena = random.randint(0, 99)
    quinta_dezena = random.randint(0, 99)    
    
    for x, y in animais.items():
        if primeira_dezena in y:
            animal1 = x
        if segunda_dezena in y:
            animal2 = x
        if terceira_dezena in y:
            animal3 = x
        if quarta_dezena in y:
            animal4 = x
        if quinta_dezena in y:
            animal5 = x
            
    valor_aposta = input("Quanto deseja apostar na {}? ".format(aposta)) 
    valor_aposta = float(valor_aposta)  
         
    print("\n\nSORTEANDO DEZENAS\n")        
    print('A 1 dezena sorteada foi {0}, deu {1}'.format(primeira_dezena, animal1))
    print('A 2 dezena sorteada foi {0}, deu {1}'.format(segunda_dezena, animal2))
    print('A 3 dezena sorteada foi {0}, deu {1}'.format(terceira_dezena, animal3))
    print('A 4 dezena sorteada foi {0}, deu {1}'.format(quarta_dezena, animal4))
    print('A 5 dezena sorteada foi {0}, deu {1}\n'.format(quinta_dezena, animal5))
    

    #definindo vencedor da aposta em animal
    if (aposta == animal1 or aposta == animal2 or aposta == animal3 or aposta == animal4 or aposta == animal5):
         print('Deu bicho! Você ganhou!')
         premio = valor_aposta * 3.6
         if (acerca == True):
             print("Você ganhou acerca!!")
             premio = valor_aposta * 18
    else:
        print("Vixi rapaz, não foi dessa vez")
        premio = 0
                       
    return (premio)
      
def define_dezenas(aposta, acerca):
    animais = {
        'avestruz' : (1, 2, 3, 4),
        'aguia' : (5,6,7,8),
        'burro' : (9,10,11,12),
        'borboleta' : (13,14,15,16),
        'cachorro' : (17,18,19,20),
        'cabra' : (21,22,23,24),
        'carneiro' : (25,26,27,28),
        'camelo' : (29,30,31,32),
        'cobra' : (33,34,35,36),
        'coelho' : (37,38,39,40),
        'cavalo' : (41,42,43,44),
        'elefante' : (45,46,47,48),
        'galo' : (49,50,51,52),
        'gato' : (53,54,55,56),
        'jacare' : (57,58,59,60),
        'leao' : (61,62,63,64),
        'macaco' : (65,66,67,68),
        'porco' : (69,70,71,72),
        'pavao' : (73,74,75,76),
        'peru' : (77,78,79,80),
        'touro' : (81,82,83,84),
        'tigre' : (85,86,87,88),
        'urso' : (89,90,91,92),
        'veado' : (93,94,95,96),
        'vaca' : (97,98,99,00)
    }
        
    animal1 = None 
    animal2 = None
    animal3 = None
    animal4 = None
    animal5 = None
    
    primeira_dezena = random.randint(0, 99)
    segunda_dezena = random.randint(0, 99)
    terceira_dezena = random.randint(0, 99)
    quarta_dezena = random.randint(0, 99)
    quinta_dezena = random.randint(0, 99)    
    
    for x, y in animais.items():
        if primeira_dezena in y:
            animal1 = x
        if segunda_dezena in y:
            animal2 = x
        if terceira_dezena in y:
            animal3 = x
        if quarta_dezena in y:
            animal4 = x
        if quinta_dezena in y:
            animal5 = x
            
    valor_aposta = input("Quanto deseja apostar na {}? ".format(aposta)) 
    valor_aposta = float(valor_aposta)  
         
    print("\n\nSORTEANDO DEZENAS\n")        
    print('A 1 dezena sorteada foi {0}, deu {1}'.format(primeira_dezena, animal1))
    print('A 2 dezena sorteada foi {0}, deu {1}'.format(segunda_dezena, animal2))
    print('A 3 dezena sorteada foi {0}, deu {1}'.format(terceira_dezena, animal3))
    print('A 4 dezena sorteada foi {0}, deu {1}'.format(quarta_dezena, animal4))
    print('A 5 dezena sorteada foi {0}, deu {1}\n'.format(quinta_dezena, animal5))   
    
    #definindo vencedor da aposta em dezena
    if (aposta == primeira_dezena or aposta == segunda_dezena or aposta == terceira_dezena or aposta == quarta_dezena or aposta == quinta_dezena):
        print("Deu a dezena! Você ganhou")
        premio = valor_aposta * 12
        if (acerca == True):
            print("Você ganhou acerca!!")
            premio = valor_aposta * 60 
    else:
        print("Vixi rapaz, não foi dessa vez")
        premio = 0
                       
    return (premio)

def valor_premio(premio):
    print("Você ganhou: {} reais imaginários".format(premio))
     
def apostar_na_dezena():
    print("\nApostando na dezena\n")
    aposta = input("Qual dezena deseja apostar?")
    aposta = int(aposta)
    print ("Sua aposta foi na dezena: ", aposta)     
    acerca = input("Deseja apostar acerca ou em todos? ")
    acerca = acerca.strip().lower()
    if(acerca == "acerca"):
            acerca = True
    else:
            acerca = False   
    premio = define_dezenas(aposta, acerca)
    valor_premio(premio)      
    

if(__name__ == "__main__"):
    jogar()