
import os
import platform



msg_logo = """
▒█▀▀▄ ▀█▀ ▒█▀▀▀█ ▒█▀▀█ ░█▀▀█ ▒█▄░▒█ ▒█░▄▀ 
▒█░▒█ ▒█░ ▒█░░▒█ ▒█▀▀▄ ▒█▄▄█ ▒█▒█▒█ ▒█▀▄░ 
▒█▄▄▀ ▄█▄ ▒█▄▄▄█ ▒█▄▄█ ▒█░▒█ ▒█░░▀█ ▒█░▒█
"""

menu = """ 
    Bem vindo!
    
    Escolha uma opção:
    [D] Depositar
    [S] Sacar
    [E] Extrato
    [X] Sair
"""

msg = "Opção escolhida é invalida"




def limpar_terminal():
    # Verifica o sistema operacional e limpa terminal
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
    
print(msg_logo)

saldo = 0
limite = 500
valor = 0
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    print(menu)
    menu_op = str(input("Escolha uma opção:"))
 
    
    if(menu_op in "Dd"):
        limpar_terminal()
        print(" DEPOSITO ".center(40, '='))
        valor = float(input("Digite o valor do deposíto: "))
        if(valor > 0):
            saldo += valor
            extrato.append(f"Deposito R${valor:.2f}")
            print(extrato[-1])
        else:
            print("Operação falhou! valor invalido")
        
    elif(menu_op in "sS"):
        limpar_terminal()
        print(" SAQUE ".center(40, '='))
        valor = float(input("Digite o valor do saque: "))   
        if(numero_saques == LIMITE_SAQUES):
            print("Operação falhou! Número máximo de saques excedido.") 
        elif(valor >= 500):
            print("Operação falhou! O valor do saque excede o limite.")
        elif(valor > 0):
            if(saldo >= valor):
                saldo -= valor
                extrato.append(f"SAQUE R$-{valor:.2f}")
                numero_saques +=1
                print(extrato[-1])
            else:
                print("Saldo insuficiente")
        else:
             print("Operação falhou! valor invalido")
    elif(menu_op in "Ee"):
        limpar_terminal()
        print(" EXTRATO ".center(40, '='))
        for registro in extrato:
            print(registro)
        print("=" * 40)
        print("Saldo Total R$ ", saldo)
        
        
    elif(menu_op in "Xx"):
       
        
        break
    else:
        limpar_terminal()
        print("Opção escolhida é invalida!, tente novamente")
        continue
    
