#Se o seu jogo aparecer um erro como: "import emoji ModuleNotFoundError: No module named 'emoji'"
#Execute esse comando: "./run.sh"

import random
import time
import emoji
from termcolor import colored

#Criando tabuleiros
tabuleiro_vazio1 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

tabuleiro_vazio2 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

tabuleiro_computador = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

tabuleiro_player = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

#criando variável de embarcações do player
embarcacoes_player1 = 0
embarcacoes_computador = 0

#Criando as Def's

# verificação para saber se a LINHA onde o jogador quer inserir uma embarcação é válida
def linha_invalida():
    while True:
        entrada = input(colored("\nIndique a LINHA onde você deseja inserir uma embarcação: ", "cyan"))
        if entrada.isdigit():
            linha = int(entrada)
            if linha in [1, 2, 3, 4, 5]:
                return linha
        print(colored("❌ Opção inválida", "red", attrs=['bold']))
        
# verificação para saber se a COLUNA onde o jogador quer inserir uma embarcação é válida
def coluna_invalida():
    while True:
        entrada = input(colored("Indique a COLUNA onde você deseja inserir uma embarcação: ", "blue"))
        if entrada.isdigit():
            coluna = int(entrada)
            if 1 <= coluna <= 10:
                return coluna
        print(colored("❌ Opção inválida", "red", attrs=['bold']))
        
# verificacao da LINHA que o jogador que atirar é válida  
def jogador_quer_acertar_linha():
    while True:
        entrada = input(colored("🧑 Player 1 - Escreva a LINHA de cordenada onde você quer atirar: ", "grey"))
        if entrada.isdigit():
            linha = int(entrada)
            if linha in [1, 2, 3, 4, 5]:
                return linha
        print(colored("❌ Opção inválida", "red", attrs=['bold']))


# verificação da COLUNA que o jogador quer acertar é válida
def jogador_quer_acertar_coluna():
    while True:
        entrada = input(colored("🧑 Player 1 - Escreva a  COLUNA de cordenada onde você quer atirar: ", "grey"))
        if entrada.isdigit():
            coluna = int(entrada)
            if 1 <= coluna <= 10:
                return coluna
        print(colored("❌ Opção inválida", "red", attrs=['bold']))


#Verifica o número em cada posição e PRINTA, NÃO DEFINE, um simbolo correspondente       
def exibe_matriz(matriz_desejada):
    print('   ', end='')
    for i in range(1, 11):
        print(f'{i:2}', end=' ')
    print()

    for i, linha in enumerate(matriz_desejada):
        print(f'{i + 1:2} ', end=' ')
        for celula in linha:
            if celula == 0:
                simbolo = emoji.emojize('🟦')
                simbolo_colorido = colored(simbolo, 'cyan')
            elif celula == 1:
                simbolo = emoji.emojize('🚢')
                simbolo_colorido = colored(simbolo, 'green')
            elif celula == 'x':
                simbolo = emoji.emojize('💦')
                simbolo_colorido = colored(simbolo, 'blue')
            elif celula == 2:
                simbolo = emoji.emojize('💥')
                simbolo_colorido = colored(simbolo, 'red')
            print(simbolo_colorido, end=' ')
        print()
                
                
#iniciando o jogo
print(colored("\n******************************************", "yellow"))
print(colored("* Bem vindo ao jogo de Batalha Naval!!!! *", "yellow"))
print(colored("******************************************\n", "yellow"))
print(colored("JOGADORES, ORGANIZEM SUAS FROTAS!!!!!     \n", "green" , attrs=["dark", "bold"]))
print()
print(colored("🧑 PLAYER 1:", "blue"))

#Fazendo o player adicionar 5 embarcacoes
while embarcacoes_player1 < 5:
    
    #pedindo a linha que será adicionada uma embarcação
    linha = linha_invalida()
    
    #pedindo a coluna que será adicionada uma embarcação
    coluna = coluna_invalida()
    
    #Enquanto ele adicionar uma embarcação em um lugar que já possui embarcação ele vai pedir para tentar de novo
    while True:
        if tabuleiro_player[linha - 1][coluna - 1] == 1:
            print(colored("VOCÊ JÁ POSSUI UMA EMBARCAÇAO NESSA POSIÇÃO. DIGITE NOVAMENTE", "red", attrs=["bold"]))
            linha = linha_invalida()
            coluna = coluna_invalida()
            
        #Se não, ele vai definir o número de embarcações e o tabuleiro atual
        else:
            embarcacoes_player1 += 1
            tabuleiro_player[linha - 1][coluna - 1] = 1
            print()
            break 
        
    #apenas fazendo uma verificação para exibir o tabuleiro do player e escrever o plural ou o singular dependendo da quantidade de embarcações 
    if embarcacoes_player1 == 1:
        print(colored("Você possui {} embarcação e seu tabuleiro atual é: ".format(embarcacoes_player1), "cyan", attrs=["dark"]))
        exibe_matriz(tabuleiro_player)
        enter = input(colored("Pressione ENTER", "yellow"))
        
    else:
        print(colored("Você possui {} embarcações e seu tabuleiro atual é: ".format(embarcacoes_player1), "cyan", attrs=["dark"]))
        exibe_matriz(tabuleiro_player)
        enter = input(colored("Pressione ENTER", "yellow"))


print()


#Definindo o tabuleiro do computador
for embarcacao_computador in range(0,5):
    
    #Definindo a linha e coluna onde serão adicionadas as embarcações do computador
    linha_computador = random.randint(0,4)
    coluna_computador = random.randint(0,9)
    
    #Enquanto a cordenada já possuir uma embarcação ele vai sortear de novo
    while tabuleiro_computador[linha_computador][coluna_computador] == 1:
        linha_computador = random.randint(0,4)
        coluna_computador = random.randint(0,9)
        
    #Depois de já conferir ele define onde a embarcação vai ficar e soma +1 ao número de embarcações
    tabuleiro_computador[linha_computador][coluna_computador] = 1
    embarcacoes_computador += 1

    #printando a quantidade de embarcações do computador
    if embarcacoes_computador == 1:
        print(colored("🤖 O COMPUTADOR possui {} embarcação.".format(embarcacoes_computador), "magenta"))
    else:
        print(colored("🤖 O COMPUTADOR possui {} embarcações.".format(embarcacoes_computador), "magenta"))
    time.sleep(1.5)
    
enter = input(colored("Pressione ENTER", "yellow"))
#comecando a guerra
#Player atirando
print(colored("\nA GUERRA COMEÇOU!!!!!!!!!!!!!!!!!!!!!", "green", attrs=["dark","bold"]))
print()

while embarcacoes_player1 != 0 and embarcacoes_computador != 0:
    print(colored("\n🧑 Player 1 - Esse é o seu tabuleiro:" , "blue"))
    exibe_matriz(tabuleiro_vazio1)
    print(colored("Você possui {} embarcações.".format(embarcacoes_player1), "magenta"))
    enter = input(colored("Pressione ENTER", "yellow"))
    print(colored("\nTabuleiro do 🤖 computador: ", "red"))
    exibe_matriz(tabuleiro_vazio2)
    print(colored("O 🤖 computador possui {} embarcações.".format(embarcacoes_computador), "magenta"))
    enter = input(colored("Pressione ENTER", "yellow"))
    
    print(colored("\n🧑 PLAYER 1 ATIREEEEE!!!!", "blue"))
    jogador_acertou_linha = jogador_quer_acertar_linha() - 1
    jogador_acertou_coluna = jogador_quer_acertar_coluna() - 1
    
    while tabuleiro_vazio2[jogador_acertou_linha][jogador_acertou_coluna] == "x" or tabuleiro_vazio2[jogador_acertou_linha][jogador_acertou_coluna] == 2:
        print(colored("\nVOCÊ JÁ ATIROU NESSA POSIÇÃO. DIGITE NOVAMENTE", "red", attrs=["bold"]))
        jogador_acertou_linha = jogador_quer_acertar_linha() - 1
        jogador_acertou_coluna = jogador_quer_acertar_coluna() - 1  
    
    #Se não derrubou nenhuma embarcação do computador ele faz isso
    if tabuleiro_computador [jogador_acertou_linha][jogador_acertou_coluna] == 0:
        print(colored("\nVocê não derrubou nenhuma embarcação! 😞", "red"))
        print(colored("O 🤖 computador possui {} embarcações".format(embarcacoes_computador), "magenta"))
        tabuleiro_vazio2[jogador_acertou_linha][jogador_acertou_coluna] = "x"
        enter = input(colored("Pressione ENTER", "yellow"))
        print()
    
    #se derrubou ele faz isso  
    elif tabuleiro_computador[jogador_acertou_linha][jogador_acertou_coluna] == 1:
        embarcacoes_computador -= 1
        print(colored("\nVocê derrubou uma embarcação do computador!!! 😎​", "green"))
        print(colored("O computador possui {} embarcações".format(embarcacoes_computador), "magenta"))
        tabuleiro_vazio2[jogador_acertou_linha][jogador_acertou_coluna] = 2
        enter = input(colored("Pressione ENTER", "yellow"))
        print()
        
        
    #Computador atirando
    linha_atira = random.randint(0,4)
    coluna_atira = random.randint(0,9)
    
    while tabuleiro_vazio1[linha_atira][coluna_atira] == "x" or tabuleiro_vazio1[linha_atira][coluna_atira] == 2:
        linha_atira = random.randint(0,4)
        coluna_atira = random.randint(0,9)
        

    print(colored("O 🤖 COMPUTADOR ESTÁ ATIRANDOOOOO!!!!!", "red"))
    print(colored(f"O 🤖 computador vai atirar na LINHA: {linha_atira + 1}", "grey"))

    print(colored(f"O 🤖 computador vai atirar na COLUNA: {coluna_atira + 1}", "grey"))
    enter = input(colored("Pressione ENTER", "yellow"))

    #Se o computador não derrubou nenhuma embarcação sua o bloco executado é:
    if tabuleiro_player[linha_atira][coluna_atira] == 0:
        print(colored("\nO 🤖 computador NÃO acertou sua embarcação!", "red"))
        print(colored("Você possui {} embarcações!".format(embarcacoes_player1), "blue"))
        tabuleiro_vazio1[linha_atira][coluna_atira] = "x"
        enter = input(colored("Pressione ENTER", "yellow"))
        
    #Se ele derrubou o bloco executado é:   
    elif tabuleiro_player[linha_atira][coluna_atira] == 1:
        embarcacoes_player1 -= 1
        print(colored("\nO 🤖 computador derrubou uma embarcação sua!", "green"))
        print(colored("Você possui {} embarcações!".format(embarcacoes_player1), "blue"))
        tabuleiro_vazio1[linha_atira][coluna_atira] = 2
        enter = input(colored("Pressione ENTER", "yellow"))
        
    if embarcacoes_computador == 0:
        print(colored("\nO 🧑 JOGADOR AFUNDOU A FROTA DO 🤖 COMPUTADOR!!!!!!", "green", attrs=["bold"]))
        print(colored("TEMOS UM NOVO CAPITÃO DOS MARES 🌊", "blue", attrs=["bold"]))
        print(colored("O 🧑 JOGADOR VENCEUUUUU ​🏆​​", "red", attrs=["bold"]))
        print(colored("\nPLACAR FINAL: ", "yellow", attrs=["bold"]))
        print(colored("Embarcações do 🧑 Player: {}. Embarcações do 🤖 Computador {}.".format(embarcacoes_player1, embarcacoes_computador), "cyan", attrs=["bold"]))
        
    elif embarcacoes_player1 == 0:
        print(colored("\nO 🤖 COMPUTADOR AFUNDOU A FROTA DO 🧑 JOGADOR!!!!!!", "green", attrs=["bold"]))
        print(colored("TEMOS UM NOVO CAPITÃO DOS MARES 🌊", "blue", attrs=["dark", "bold"]))
        print(colored("O 🤖 COMPUTADOR VENCEUUUUU 🏆", "blue", attrs=["bold"]))
        print(colored("\nPLACAR FINAL: ", "yellow", attrs=["bold"]))
        print(colored("Embarcações do 🧑 Player: {}. Embarcações do 🤖 Computador {}.".format(embarcacoes_player1, embarcacoes_computador), "cyan", attrs=["bold"]))
        
    elif embarcacoes_player1 == 0 and embarcacoes_computador == 0:
        print(colored("\nESSA GUERRA FOI SANGRENTA, NINGUÉM SOBREVIVEU!", "grey", attrs=["bold"]))
    
print(colored("************************************************************************", "green", attrs=["bold"]))
print(colored("* Obrigado por participar do nosso jogo 😁                             *", "green", attrs=["bold"]))
print(colored("* Alunos: Felipe Bresciani, Pedro Henrique Junqueira e Rafael Eliezer. *", "green", attrs=["bold"]))
print(colored("************************************************************************\n", "green", attrs=["bold"]))