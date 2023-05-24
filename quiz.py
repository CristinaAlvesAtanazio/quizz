print("Quiz Supernatural")
answer_user= input("Podemos começar? (s/n) ")

if answer_user != "s":
    quit()

score = 0

print("Começando...")

print("1/10 - Qual é o nome dos dois irmãos protagonistas em Supernatural?\n (1) Sam e Dean \n (2) John e Bobby \n (3) Michael e Lucifer \n (4) Adam e Castiel ")
answer_1 = input("Resposta: ")


if answer_1 == "1":
    print("Você acertou!")
    score+=1
else:
    print("Não foi dessa vez")  
    

print("2/10 - Qual é o nome do carro clássico que os irmãos Winchester dirigem?\n (1) Impala \n (2) Mustang \n (3) Camaro \n (4) Charger ")
answer_2 = input("Resposta: ")


if answer_2 == "1":
    print("Você acertou!")
    score+=1
else:
    print("Não foi dessa vez")  


print("3/10 - Qual é o nome do anjo aliado dos irmãos Winchester?\n (1) Gabriel \n (2) Uriel \n (3) Metatron \n (4) Castiel ")
answer_3 = input("Resposta: ")


if answer_3 == "4":
    print("Você acertou!")
    score+=1
else:
    print("Não foi dessa vez")  


print("4/10 - Quem é o principal vilão na primeira temporada de Supernatural?\n (1) Azazel \n (2) Lilith \n (3) Crowley \n (4) Abaddon ")
answer_4 = input("Resposta: ")


if answer_4 == "1":
    print("Você acertou!")
    score+=1
else:
    print("Não foi dessa vez")


print("5/10 - Qual é o nome do local onde os irmãos Winchester vivem e planejam suas caçadas?\n (1) Mansão \n (2) Bunker \n (3) Apartamento \n (4) Cabana ")
answer_5 = input("Resposta: ")


if answer_5 == "2":
    print("Você acertou!")
    score+=1
else:
    print("Não foi dessa vez")


print("6/10 - Qual é o nome do demônio que possui uma relação complexa com os irmãos Winchester?\n (1)Alistair \n (2) Ruby \n (3) Crowley \n (4) Meg ")
answer_6 = input("Resposta: ")


if answer_6 == "3":
    print("Você acertou!")
    score+=1
else:
    print("Não foi dessa vez") 
    

print("7/10 - Quem é conhecido como o rei do inferno em Supernatural?\n (1) Crowley \n (2) Lucifer \n (3) Azazel \n (4) Rowena ")
answer_7 = input("Resposta: ")


if answer_7 == "1":
    print("Você acertou!")
    score+=1
else:
    print("Não foi dessa vez") 


print("8/10 - Qual é o nome do grupo secreto que governa o mundo das bruxas em Supernatural?\n (1) A Irmandade das Sombras \n (2) O Conselho das Trevas \n (3) A Ordem dos Feiticeiros \n (4) A Sociedade dos Magos ")
answer_8 = input("Resposta: ")


if answer_8 == "2":
    print("Você acertou!")
    score+=1
else:
    print("Não foi dessa vez") 


print("9/10 - Qual é o nome do apocalipse que os irmãos Winchester tentam impedir?\n (1) O Apocalipse Celestial \n (2) O Armageddon \n (3) O Fim dos Tempos \n (4) A Grande Catástrofe ")
answer_9 = input("Resposta: ")


if answer_9 == "3":
    print("Você acertou!")
    score+=1
else:
    print("Não foi dessa vez")


print("10/10 - Quem é o pai dos irmãos Winchester?\n (1) John Winchester \n (2) Bobby Singer \n (3) Samuel Campbell \n (4) Dean Winchester Sr. ")
answer_10 = input("Resposta: ")


if answer_10 == "1":
    print("Você acertou!")
    score+=1
else:
    print("Não foi dessa vez")

print("Você fez {} acertos e {} falhas.".format(score, 10 - score))
