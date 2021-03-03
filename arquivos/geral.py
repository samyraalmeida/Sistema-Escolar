import unicodedata

def tirar_acentos(nome):
    # Tiro os acentos de nome
	nome_sem_acentos = unicodedata.normalize('NFKD', nome).encode('ascii', 'ignore').decode('utf8')
	return nome_sem_acentos

def formata_nome(nome):
	# Tiro os acentos de nome 
	nome = tirar_acentos(nome)

	# Retorno nome como uma string, sem acentos e minúscula.
	return nome.lower()

def valida_nome(nome):

    separar_nome = nome.split(' ')
    
    # Checo se o nome so é composto por letras do alfabeto
    for nome in separar_nome: 
        if not nome.isalpha(): # Caso não seja, ok recebe falso
            raise ValueError
    
    # Se o código chegou até aqui, significa que o nome é valido
    return True

def valida_resposta(resposta):

    # Se a resposta não esta no formato
	if not resposta in ['s', 'n']:
        # Retorno um erro de valor
		raise ValueError
    
    # Se está no formato, retorno verdadeiro
	return True

def perguntar(pergunta):

    while True:
        # A pergunta, sempre so vai ter sim ou não como resposta, então iremos realizar a pergunta enquanto o
        # usuário não digitar uma resposta válida.
        
        try:
            # Exibo a pergunta
            print(pergunta)

            # Leio a resposta
            resposta = input('> ')
            # Formo o nome (tiro os possiveis acentos e coloco tudo em minusculo)
            resposta = formata_nome(resposta)

            if valida_resposta(resposta):
                
                if resposta == 's':
                    return True
                else:
                    return False
        except ValueError:
            print('Por favor, digite s ou n.')
            print('Você digitou:', resposta)

def valida_opcao_menu(menu, pergunta_menu):
    
    # Exibo a pergunta do menu
    print(pergunta_menu)
    print('Escolha uma das opções a seguir:')

    # Exibo o menu
    for opcao in menu:
        print(opcao)       

    # Seleciono a ocao do menu
    while True:
        try:
            opcao = input('> ')
            opcao = int(opcao)

            if 1 < opcao > len(menu):
                raise ValueError
            
            return opcao
        except ValueError:
            
            print(f"\nEscolha uma das opções e digite o número, entre {1} e {len(menu)}, associado a ela.")
            print('Você digitou:', opcao)
