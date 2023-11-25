import os
import random
from colorama import Fore, Back, Style

jogarNovamente="s"
jogadas=0
quemJoga=2 # 1=CPU - 2=Jogador
maxJogadas=9
vit="n"
velha=[
    [" "," "," "], #L0C0 L0C1 L0C2
    [" "," "," "], #L1C0 L1C1 L1C2
    [" "," "," "]  #L2C0 L2C1 L2C2
]

def tela():
    global velha
    global jogadas
    os.system("cls")
    print("    0   1   2")
    print("0:  " + velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2])
    print("  -----------")
    print("1:  " + velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2])
    print("  -----------")
    print("2:  " + velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2])
    print("Jogadas: " + Fore.GREEN + str(jogadas) + Fore.RESET)

def jogadorJoga():
    global jogadas
    global quemJoga
    global maxJogadas
    if quemJoga==2 and jogadas<maxJogadas:
        try:
            l=int(input("Linha..: "))
            c=int(input("Coluna.: "))
            while velha[l][c]!= " ":
                l=int(input("Linha..: "))
                c=int(input("Coluna.: "))                    
            velha[l][c]="X"
            quemJoga=1
            jogadas+=1
        except:
            print("Jogada invalida")
            os.system("pause")
            #vit="n"

def cpuJoga():
    global jogadas
    global quemJoga
    global maxJogadas
    if quemJoga==1 and jogadas<maxJogadas:
         l=random.randrange(0,3)
         c=random.randrange(0,3)
         while velha[l][c]!= " ":
             l=random.randrange(0,3)
             c=random.randrange(0,3)
             velha[l][c]="O"
    jogadas+=1
    quemJoga=2

def verificarVitoria():
    global velha
    vitoria="n"
    simbolos=["x","O"]
    for s in simbolos:
        vitoria="n"
        #Verificar Linhas
        il=ic=0
        while il<3:
            soma=0
            ic=0
            while ic<3:
                if(velha[il][ic]==s):
                    soma+=1
                    ic+=1                    
                    if(soma==3):
                        vitoria=s
                        break
                    il+=1
                    if(vitoria!="n"):
                        break
                    #Verificar Colunas                 
                    il=ic=0
                    while ic<3:
                         soma=0
                         il=0
                         while il<3:
                              if(velha[il][ic]==s):
                                   soma+=1
                                   il+=1                                                                     
                                   if(soma==3):
                                        vitoria=s
                                        break
                                   ic+=1
                                   if(vitoria!="n"):
                                         break
                                   #Verifica diagonal 1
                                   soma=0
                                   idiag=0
                                   while idiag<3:
                                       if(velha[idiag][idiag]==s):
                                           soma+=1
                                           idiag+=1
                                           if(soma==3):
                                               vitoria=s
                                               break
                                           #Verifica diagonal 1
                                   soma=0
                                   idiagl=0
                                   idiagc=2
                                   while idiagc>=0:
                                       if(velha[idiag][idiag]==s):
                                           soma+=1
                                           idiagl+=1
                                           idiagc-=1
                                           if(soma==3):
                                               vitoria=s
                                               break
                                           return vitoria
                                       def redefinir():
                                           global velha
                                           global jogadas
                                           global quemJoga
                                           global maxJogadas
                                           global vit                                         
                                           jogadas=0
                                           quemJoga=2 # 1=CPU - 2=Jogador
                                           maxJogadas=9
                                           vit="n"
                                           velha=[
                                                   [" "," "," "], #L0C0 L0C1 L0C2
                                                           [" "," "," "], #L1C0 L1C1 L1C2
                                                                   [" "," "," "]  #L2C0 L2C1 L2C2
                                                                   ]
                                           while(jogarNovamente=="s"):
                                                while True:
                                                      tela()
                                                      jogadorJoga()
                                                      cpuJoga()
                                                      tela()
                                                      vit=verificarVitoria()
                                                      if(vit!="n")or(jogadas>=maxJogadas):
                                                            break
                                                            print(Fore.RED + "FIM DE JOGO" + Fore.YELLOW)
                                                            if(vit=="X" or vit=="O"):
                                                                  print("Resultado: Jogador " + vit + " venceu")
                                                            else:
                                                                                                                                    print("Resultado: Empate")
                                                                                                                                    jogarNovamente=input(Fore.BLUE + "Jogar Novamente? [s/n]: " + Fore.RESET)
                                                                                                                                    redefinir()