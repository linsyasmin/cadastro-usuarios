# PARTE 1: Adicionar usuários

import ast

with open ("teste.txt", "a") as arquivo:
    cont = "sim"

    while (cont == "sim"):
        nome = input("Nome: ").lower()
        idade = int(input("Idade: "))
        email = input("E-mail: ").lower()
        
        dados = [nome, idade, email]
        arquivo.write(f"{dados}\n")

        cont = input("Continuar? ").lower()

#PARTE 2: Menu de decisão

decisao = int(input("Digite 1 para adicionar usuário, 2 para exibir o nome dos usuários ou 3  para checar algum dado: "))

# adicionar usuário
if (decisao == 1): 
    with open ("teste.txt", "a") as arquivo:
        nome = input("Nome: ").lower()
        idade = int(input("Idade: "))
        email = input("E-mail: ").lower()
        dados = [nome, idade, email]
        arquivo.write(f"{dados}\n") 

# exibir o nome de todos os usuários
elif (decisao == 2):
    with open ("teste.txt", "r") as arquivo:
        usuarios = []
        for linha in arquivo:
            dados = ast.literal_eval(linha)
            usuarios.append(dados[0])
        print(f"Usuários cadastrados:\n{usuarios}") 

# para checar dado específico
elif (decisao == 3):
    with open ("teste.txt", "r") as arquivo:
        linhas = arquivo.readlines() #lê linha por linha
        checar = input("O que você deseja checar? ")

        # exibe a quantidade de usuários com x nome
        if (checar.lower() == "nome"):
            nome = input("Nome para checar: ")
            nomes = 0
            for nome in dados:
                nomes += 1
            print(f"Quantidade de usuários chamados {nome}:\n{nomes}")
        
        # exibe os usuários com x idade
        elif (checar.lower() == "idade"):
            idade = int(input("Idade que deseja checar: "))
            usuarios = []
            cont = 0

            # transformando cada linha do arquivo em lista:
            for linha in linhas: # acessa linha por linha
                dados = ast.literal_eval(linha) # dados se torna uma lista
                
                if idade in dados:
                    usuarios.append(dados[0])
                    cont += 1
            if cont > 0:
                print(f"Usuários com {idade} anos:\n{usuarios}")
            else:
                print(f"Não há usuários cadastrados com essa idade.")

else:
    print("Erro: não encontrado!") 