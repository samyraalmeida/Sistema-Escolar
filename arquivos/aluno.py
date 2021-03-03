import geral
import datetime
import disciplina

'''
Aluno contém:

    * Número de Matrícula que deve ser gerado automaticamente.
    * Nome.
    * Email.
    * Data de Nascimento.
'''

class entidade_aluno():
    
    def __init__(self):
        self.ultima_matricula = 0
        self.lista = {}
        self.nomes = {}
        self.emails = {}

    def checar_matricula(self, matricula_aluno):
        
        # Checo se a matricula do aluno existe
        if matricula_aluno in self.lista:
            # Se sim, retorno verdadeiro
            return True
        else:
            # Se não, retorno falso
            return False

    def adicionar_nome(self, matricula_aluno, nome_aluno):
        # Adiciono o nome do aluno a lista de nomes
        nome_aluno = geral.formata_nome(nome_aluno)

        if not nome_aluno in self.nomes:
            self.nomes[nome_aluno] = []
        
        self.nomes[nome_aluno].append(matricula_aluno)

    def deletar_nome(self, matricula_aluno, nome_aluno):
        # Deleto o nome do aluno da lista de nomes
        nome_aluno = geral.formata_nome(nome_aluno)

        self.nomes[nome_aluno].remove(matricula_aluno)

        if not self.nomes[nome_aluno]:
            self.nomes.pop(nome_aluno)
    
    def adicionar_email(self, matricula_aluno, email):
        # Adiciono o email do aluno à lista de emails
        if not email in self.emails:
            self.emails[email] = []
        
        self.emails[email].append(matricula_aluno)
    
    def deletar_email(self, matricula_aluno, email):
        # Deleto o email do aluno da lista de emails
        self.emails[email].remove(matricula_aluno)

        if not self.emails[email]:
            self.emails.pop(email)
    
    def adicionar(self, dados_aluno):
        # Adiciono o aluno a estrutura
        matricula_aluno, nome_aluno, email, data_nasc = dados_aluno
        
        self.adicionar_nome(matricula_aluno, nome_aluno)
        self.adicionar_email(matricula_aluno, email)

        self.ultima_matricula = matricula_aluno
        self.lista[matricula_aluno] = [nome_aluno, email, data_nasc]

    def deletar(self, matricula_aluno):
        # Deleto o aluno da estrutura
        nome_aluno, email, data_nasc = self.lista[matricula_aluno]

        self.deletar_nome(matricula_aluno, nome_aluno)
        self.deletar_email(matricula_aluno, email)

        self.lista.pop(matricula_aluno)

    def alterar(self, novos_dados):
        matricula_aluno, nv_nome_aluno, nv_email, nv_data_nasc = novos_dados
        # Altero os dados do aluno 

        # Pego os antigos dados e os deleto da estrutura
        ant_nome_aluno, ant_email, ant_data_nasc = self.lista[matricula_aluno]
        
        self.deletar_nome(matricula_aluno, ant_nome_aluno)
        self.deletar_email(matricula_aluno, ant_email)
        
        # Adiciono os novos dados à estrutura

        self.adicionar_nome(matricula_aluno, nv_nome_aluno)
        self.adicionar_email(matricula_aluno, nv_email)

        self.lista[matricula_aluno] = [nv_nome_aluno, nv_email, nv_data_nasc]

def exibir(dados_aluno, disciplinas_assistidas = [], exibir_disc = False):
    
    matricula_aluno, nome_aluno, email, data_nasc = dados_aluno

    # Exibo os dados do aluno
    print(f"Matrícula:                         {matricula_aluno}")
    print(f"Nome:                              {nome_aluno}")
    print(f"email:                             {email}")
    print(f"data de nascimento:                {data_nasc}")
    
    # Checo se é para exibir as disciplinas que o aluno assite
    if exibir_disc:
        
        # Se sim, 
        # Transformo a lista de disciplinas em uma string que contem os códigos das disciplinas

        disciplinas_assistidas = list(map(str, disciplinas_assistidas))
        disciplinas_assistidas = ' '.join(disciplinas_assistidas)
        
        # Se o aluno não assiste nenhuma disciplina
        if not disciplinas_assistidas:
            disciplinas_assistidas = 'Esse(a) aluno(a) não assiste nenhuma matéria.'

        # Exibo os codigos das disciplinas, se ele está matriculado em alguma, caso contrário 
        # exibo uma mensagem informando que o aluno não assiste nenhuma disciplina
        print(f"Código das disciplinas assistidas: {disciplinas_assistidas}")

def recebe_nome():

    while True:
        try:
            # Leio o nome do aluno
            print('\nDigite o nome do(a) aluno(a):')
            nome_aluno = input('> ')

            # Checo se o formato do nome esta ok

            if geral.valida_nome(nome_aluno):

                # Se sim, retorno o nome
                return nome_aluno
        except ValueError:

            # Se deu erro, exibo uma mensagem que deu erro
            print('O nome do(a) aluno(a) só deve conter letras do alfabeto.')
            print('Você digitou:', nome_aluno)

def valida_email(email):

    # Se o email não tem @ ele é inválido
    if not '@' in email:
        raise ValueError

    username, domain = email.split('@')

    # Se não existir nenhum caractere antes ou depois do @, o email é invalido
    if not username or not domain:
        raise ValueError

    # Crio uma lista com os caracteres (diferentes de letras e números) que são permitidos
    lista_caracteres = ['.', '_']

    for i in range(0, len(username) - 1, 1):
        caractere_atual = username[i]
        caractere_prox = username[i + 1]

        # Se algum dos dois caracteres é inválido, ou seja, se algum dos dois é diferente de '.', '_' 
        # e não é letra nem número.
        if (not caractere_atual in lista_caracteres and not caractere_atual.isalnum()) or (not caractere_prox in lista_caracteres and not caractere_prox.isalnum()):
            raise ValueError
        
        # Se existir '..', '__', '._' ou '_.' o email é inválido
        if caractere_atual in lista_caracteres and caractere_prox in lista_caracteres:
            raise ValueError

    # Se o primeiro ou o ultimo caractere do username não são alfanuméricos, o email é inválido
    if not username[0].isalnum() or not username[len(username) - 1].isalnum():
        raise ValueError

    # Se não tem '.' no dominio, o email é invalido
    if not '.' in domain:
        raise ValueError
    
    for i in range(0, len(domain) - 1, 1):
        caractere_atual = domain[i]
        caractere_prox = domain[i + 1]

        # Se o dominio não é composto somente por '.', letras e números ou se existir algum '..',
        # o email é inválido

        if caractere_atual == '.':
            if not caractere_prox.isalnum():
                raise ValueError
        elif not caractere_atual.isalnum():
            raise ValueError

    # Se o primeiro ou o ultimo caractere do domain não são alfanuméricos, o email é inválido
    if not domain[0].isalnum() or not domain[len(domain) - 1].isalnum():
        raise ValueError

    # Se o chegamos até aqui, o email é válido
    return True

def recebe_email():
    
    while True:
        try:
            # Leio o email do aluno
            print('\nDigite o email:')
            email = input('> ')

            # Checo se o email esta na formatação correta
            if valida_email(email):
                return email
        except ValueError:

            # Se deu erro, exibo uma mensagem de erro
            print('O email esta fora da formatação, por favor digite um email válido!')
            print('Você digitou:', email)

def valida_data(data):
    
    # Checo de a data é válida
    ano, mes, dia = [int(i) for i in data.split('-')]

    # Se for, ira retornar a data, se não irá retornar o erro 'ValueError'
    return datetime.date(ano, mes, dia)
    
def recebe_data():

    while True:
        try:
            # Leio a data de nascimento do aluno
            print('\nDigite a data de nascimento (AAAA-MM-DD):')
            data_nasc = input('> ')

            # Checo se a data de nascimento é válida
            # Se ela for, retornamos ela, se não ela irá retornar uma mensagem de erro
            return valida_data(data_nasc)
        except ValueError:

            # Se a data ão for valida, exibimos uma mensagem de erro
            print('Essa data de nascimento não existe. Por favor, digite uma data válida.')
            print('Você digitou:', data_nasc)

def cadastrar(Alunos):
    while True:
        # Coloco a matricula do aluno
        matricula_aluno = Alunos.ultima_matricula + 1

        # Leio o nome do aluno
        nome_aluno = recebe_nome()

        # Leio o email do aluno
        email = recebe_email()

        # Leio a data de nascimento do aluno
        data_nasc = recebe_data()

        # Crio uma lista com os dados do aluno, afim de facilitar nossa vida
        dados_aluno = [matricula_aluno, nome_aluno, email, data_nasc]

        # Exibo os dados do aluno
        print('\nVocê está criando o(a) seguinte aluno(a):')
        exibir(dados_aluno)

        # Checo se é para confirmar o cadastro
        if geral.perguntar('\nConfirmar cadastro? (s/n)'):
            
            # Se sim, cadastro o aluno
            Alunos.adicionar(dados_aluno)
            print('Cadastrando aluno(a)...')

            # Paro o loop
            break
        
        # Caso contrário,
        # Checo se não é para cadastrar um aluno

        if not geral.perguntar('\nDeseja cadastrar um(a) aluno(a)? (s/n)'):
            
            # Se sim, paro o loop
            break
        
        # Caso contrario, repetimos o loop

    return Alunos

def recebe_matricula():
    while True:
        try:
            # Leio a matrícula do aluno
            print('\nDigite a matrícula do(a) aluno(a):')
            matricula_aluno = input('> ')
            matricula_aluno = int(matricula_aluno) 
            
            # Se a matricula digitada for um número inteiro
            return matricula_aluno
        except ValueError:

            # Caso não seja, exibo uma mensagem de erro
            print('A matrícula do(a) aluno(a) é númerica.')
            print('Você digitou:', matricula_aluno)

def pesquisa_matricula(pesq_matricula, Alunos):

    # Irei buscar todas as matriculas dos alunos que contem 'pesq_matricula'
    # Essa lista vai conter todas as matriculas que se encaixam da condição anterior
    lista_alunos = []

    # Transformo pesq_matricula em uma string, a fim de facilitar as proximas checagens
    pesq_matricula_str = str(pesq_matricula)

    # Passo por todas as matriculas dos alunos
    for matricula_aluno in Alunos.lista.keys():

        matricula_aluno_str = str(matricula_aluno)

        # checo se pesq_matricula esta contida em  matricula_aluno

        if pesq_matricula_str in matricula_aluno_str:
            # Se sim, adiciono matricula_aluno a lista dos alunos
            lista_alunos.append(matricula_aluno)

    # Se algum aluno satisfaz a busca
    if lista_alunos:

        # Retorno a lista de alunos
        return lista_alunos

    # Caso contrário, retorno um erro de chave
    raise KeyError

def pesquisa_nome(pesq_nome, Alunos):
    # Irei buscar todas as matriculas dos alunos que contem nos quais seus nomes contem 'pesq_nome'

    # Essa lista vai conter todas as matriculas que se encaixam da condição anterior
    lista_alunos = []

    # Formato o nome digitado, ou seja, tiro os acentos e coloco todos os caracteres minusculos
    pesq_nome_formatado = geral.formata_nome(pesq_nome)

    # Passo por todas as matriculas dos alunos
    for nome_aluno in Alunos.nomes.keys():
        
        # Checo se pesq_nome_formatado está contido em nome_aluno
        if pesq_nome_formatado in nome_aluno:

            # Se sim, adiciono todos os alunos que tem esse nome na lista de alunos
            lista_alunos += Alunos.nomes[nome_aluno]

    # Se algum aluno satisfaz a busca
    if lista_alunos:
        
        # Retorno a lista de alunos
        return lista_alunos

    # Caso contrário, retorno um erro de chave
    raise KeyError

def pesquisa_email(pesq_email, Alunos):
    # Irei buscar todas as matriculas dos alunos que contem 'nos quais seus nomes contem 'pesq_nome'

    # Essa lista vai conter todas as matriculas que se encaixam da condição anterior
    lista_alunos = []

    # Passo por todas as matriculas dos alunos
    for email in Alunos.emails.keys():
        
        # Checo se pesq_email está contido em email
        if pesq_email in email:
            
            # Se sim, adiciono todos os alunos que tem esse email na lista de alunos
            lista_alunos += Alunos.emails[email]

    # Se algum aluno satisfaz a busca
    if lista_alunos:
        
        # Retorno a lista de alunos
        return lista_alunos

    # Caso contrário, retorno um erro de chave
    raise KeyError

def busca_exibindo_escolhendo_resultados(lista_alunos, Alunos, Disciplinas):

    print('\nOs(as) alunos(as) que satisfazem sua busca são:')

    # Exibo todos os alunos que satisfazem ao nome digitado
    for matricula_aluno in lista_alunos:
        nome_aluno, email, data_nasc = Alunos.lista[matricula_aluno]

        dados_aluno = [matricula_aluno, nome_aluno, email, data_nasc]

        disciplinas_assistidas = []

        if matricula_aluno in Disciplinas.alunos:
            disciplinas_assistidas = Disciplinas.alunos[matricula_aluno]
        
        print('\nExibindo aluno:')
        exibir(dados_aluno, disciplinas_assistidas, True)

    # Pego o código do aluno
    while True:
        print('\nEscolha um(a) dos(as) alunos(as) mostrados acima e digite sua matrícula.', end = '')
        
        matricula_aluno = recebe_matricula()
        
        if matricula_aluno in lista_alunos:
            return matricula_aluno
        else:
            print('Digite uma das matrículas dos alunos(as) mostrados(as) acima.')

def busca_matricula(Alunos, Disciplinas):

    try:
        # Leio a matricula que foi digitada
        pesq_matricula = recebe_matricula()

        # Monto uma lista com os codigos dos alunos que satisfazem a busca
        lista_alunos = pesquisa_matricula(pesq_matricula, Alunos)

        # Exibo todos na tela e escolho o aluno desejado
        return busca_exibindo_escolhendo_resultados(lista_alunos, Alunos, Disciplinas)
    except KeyError:
        # Caso o código não exista
        print(f"Nenhum resultado encontrado para a matrícula: {pesq_matricula}")

def busca_nome(Alunos, Disciplinas):
    try:
        # Leio o nome que foi digitado
        pesq_nome = recebe_nome()

        # Monto uma lista com os códigos dos alunos que satisfazem a busca
        lista_alunos = pesquisa_nome(pesq_nome, Alunos)

        # Exibo todos na tela e escolho o aluno desejado
        return busca_exibindo_escolhendo_resultados(lista_alunos, Alunos, Disciplinas)
    except KeyError:
        # Caso o nome não exista        
        print(f'Nenhum resultado encontrado para o nome "{pesq_nome}".')

def busca_email(Alunos, Disciplinas):
    try:
        # Leio o email que foi digitado
        pesq_email = recebe_email()

        # Monto uma lista com os códigos dos alunos que satisfazem a busca
        lista_alunos = pesquisa_email(pesq_email, Alunos)

        # Exibo todos na tela e escolho o aluno desejado
        return busca_exibindo_escolhendo_resultados(lista_alunos, Alunos, Disciplinas)
    except KeyError:
        # Caso o nome não exista
        print(f'Nenhum resultado encontrado para o email {pesq_email}.')

def busca(opcao, Alunos, Disciplinas):
    # Se opcao = 1, iremos realizar uma busca aluno por Matrícula.
    # Se opcao = 2, iremos realizar uma busca aluno por Nome.
    # Se opcao = 3, iremos realizar uma busca aluno por email.
    
    matricula_aluno = int()

    if opcao == 1: 
        # Busca por matrícula
        print('\nBusca por matrícula', end = '')
        matricula_aluno = busca_matricula(Alunos, Disciplinas)
    elif opcao == 2: 
        # Busca por nome
        print('\nBusca por nome', end = '')
        matricula_aluno = busca_nome(Alunos, Disciplinas)
    else:
        # Busca por email
        print('\nBusca por email', end = '')
        matricula_aluno = busca_email(Alunos, Disciplinas)

    if matricula_aluno:
        nome_aluno, email, data_nasc = Alunos.lista[matricula_aluno]
        
        dados_aluno = [matricula_aluno, nome_aluno, email, data_nasc]

        disciplinas_assistidas = []

        if matricula_aluno in Disciplinas.alunos:
            disciplinas_assistidas = Disciplinas.alunos[matricula_aluno]

        print('\nExibindo aluno:')
        exibir(dados_aluno, disciplinas_assistidas, True)

def recebe_busca(pergunta_menu, Alunos, Disciplinas):
    
    # Opções de busca pelo aluno
    menu_busca_aluno = [
        '1. Buscar Aluno por Matrícula.',
        '2. Buscar Aluno por Nome.',
        '3. Buscar Aluno por email.'
    ]

    opcao = geral.valida_opcao_menu(menu_busca_aluno, pergunta_menu)

    matricula_aluno = int()

    if opcao == 1: 
        # Busca por matrícula
        matricula_aluno = busca_matricula(Alunos, Disciplinas)
    elif opcao == 2: 
        # Busca por nome
        matricula_aluno = busca_nome(Alunos, Disciplinas)
    else:
        # Busca por email
        matricula_aluno = busca_email(Alunos, Disciplinas)

    return matricula_aluno

def recebe_modificacoes(opcao):
    
    # Checo qual alteração está sendo feita nesse momento
    if opcao == 0:
        # Modifico o nome do aluno
        return recebe_nome()
    elif opcao == 1:
        # Modifico o email do aluno
        return recebe_email()
    else:
        # Modifico a data de aniverário do aluno
        return recebe_data()

def modificar(Alunos, Disciplinas):
    while True:
        
        # Defino a pergunta que será exibida junto com o menu de busca
        pergunta_menu = '\nComo deseja achar o(a) aluno(a) que você irá modificar?'

        # Realizo a busca para saber qual aluno vai ser alterado
        matricula_aluno = recebe_busca(pergunta_menu, Alunos, Disciplinas)

        # Checo se o aluno existe de fato
        if Alunos.checar_matricula(matricula_aluno):

            # Crio uma lista com as possiveis modificações no aluno
            opcoes_modificacoes_aluno = [
                '\nDeseja modificar o Nome do Aluno?',
                '\nDeseja modificar o Email do Aluno?',
                '\nDeseja modificar a data de nascimento do Aluno?'
            ]

            # Crio um vetor que vai conter os novos dados do aluno
            novos_dados = [matricula_aluno]

            # Percorro a lista de possiveis modificações, checando se é ou não para alterar esse dado do aluno
            for opcao in range(3):
                
                # A pergunta a alteracao em questão
                pergunta_modificar = opcoes_modificacoes_aluno[opcao]

                # O valor do dado que será adicionado ao aluno ou o mesmo que antes se não alterarmos nada
                adicionar = Alunos.lista[matricula_aluno][opcao]

                # Checo se é para alterar o dado
                if geral.perguntar(pergunta_modificar):
                    # Se sim realizo a alteração
                    adicionar = recebe_modificacoes(opcao)
                
                # Adiciono o dado na lista atualizado no aluno
                novos_dados.append(adicionar)

            # Exibo o aluno com a alteração
            print('\nExibindo aluno(a) após as alterações:')
            exibir(novos_dados)

            # Checo se é para confirmar a modificação
            if geral.perguntar('\nConfirmar modificação? (s/n)'):
                
                # Se sim, altero o aluno
                Alunos.alterar(novos_dados)
                print('Modificando aluno(a)...')
                # Paro o loop
                break
            
        # Caso alguma das checagens anteriores não seja verdadeira,
        # Checo se não é para modificar um aluno
        if geral.perguntar('\nDeseja modificar um(a) aluno(a)? (s/n)'):
            
            # Se sim, paro o loop
            break
        
        # Caso contrario, repetimos o loop

    return Alunos

def remover(Alunos, Disciplinas):
    while True:
        # Defino a pergunta que será exibida junto com o menu de busca
        pergunta_menu = '\nComo deseja achar o(a) aluno(a) que você irá remover?'

        # Realizo a busca para saber qual aluno vai ser removido
        matricula_aluno = recebe_busca(pergunta_menu, Alunos, Disciplinas)

        # Checo se o aluno existe de fato
        if Alunos.checar_matricula(matricula_aluno):
        
            nome_aluno, email, data_nasc = Alunos.lista[matricula_aluno]

            dados_aluno = [matricula_aluno, nome_aluno, email, data_nasc]

            print('\nExibindo o(a) aluno(a):')
            exibir(dados_aluno)
            
            # Checo se é para confirmar a remoção
            if geral.perguntar('\nConfirmar remoção? (s/n)'):
                # Se sim, removo o aluno

                if matricula_aluno in Disciplinas.alunos:
                    
                    lista_disciplinas = []
                    
                    for codigo_disciplina in Disciplinas.alunos[matricula_aluno]:
                        lista_disciplinas.append(codigo_disciplina)
                    
                    for codigo in lista_disciplinas:
                        Disciplinas.deletar_aluno(codigo, matricula_aluno)

                Alunos.deletar(matricula_aluno)
                print('Removendo aluno(a)...')
                # Paro o loop
                break
        
        # Caso alguma das checagens anteriores não seja verdadeira,
        # Checo se não é para remover um professor

        if not geral.perguntar('\nDeseja remover um(a) aluno(a)? (s/n)'):
            
            # Se sim, paro o loop
            break
        # Caso contrario, repetimos o loop

    return [Alunos, Disciplinas]

def recebe_disciplina(lista_disciplinas, Disciplinas):
    while geral.perguntar('\nDeseja matricular esse aluno em alguma disciplina? (s/n)'):
        # Defino a pergunta que será exibida junto com o menu de busca
        pergunta_menu = '\nComo deseja achar a disciplina que que o(a?) aluno(a) irá assistir?'

        # Realizo a busca para saber qual disciplina será assistida
        codigo_disciplina = disciplina.recebe_busca(pergunta_menu, Disciplinas)

        # Checo se a disciplina existe de fato
        if not Disciplinas.checar_codigo(codigo_disciplina):
            print('Por favor, digite uma disciplina válida.')
            continue

        dias_horarios = Disciplinas.lista[codigo_disciplina][1]

        vagas_disponiveis = Disciplinas.lista[codigo_disciplina][4]

        if codigo_disciplina in Disciplinas.matriculas:
            alunos_matriculados = Disciplinas.matriculas[codigo_disciplina]
            
            tam = len(alunos_matriculados)

            vagas_disponiveis -= tam

        if not vagas_disponiveis:
            print('Essa disciplina já está lotada.')
            continue
        
        # Se os horarios da disciplina chocarem com os do aluno
        if not disciplina.checar_disponibilidade(lista_disciplinas, dias_horarios, Disciplinas):
            # Exibimos uma mensagem de erro e rodamos o loop de novo
            print('Os horários do(a) aluno(a) chocam com o da disciplina.')
            continue
        
        nome_disciplina, dias_horarios, matricula_prof, local, num_vagas = Disciplinas.lista[codigo_disciplina]
        
        alunos_matriculados = []
        
        if codigo_disciplina in Disciplinas.matriculas:
            alunos_matriculados = Disciplinas.matriculas[codigo_disciplina]

        dados_disciplina = [codigo_disciplina, nome_disciplina, dias_horarios, matricula_prof, local, num_vagas, alunos_matriculados]

        print('\nVocê esta matriculando o(a) aluno(a) a seguinte disciplina:')
        disciplina.exibir(dados_disciplina)

        # Se for para cadastrar
        if geral.perguntar('\nConfirma? (s/n)'):
            # Retorno o codigo da disciplina
            return codigo_disciplina
        
        # Caso contrário o loop ira se repetir

def matricular(Alunos, Disciplinas):

    while True:
        # Defino a pergunta que será exibida junto com o menu de busca
        pergunta_menu = '\nComo deseja achar o(a) aluno(a) que você irá matricular em uma disciplina?'

        matricula_aluno = recebe_busca(pergunta_menu, Alunos, Disciplinas)

        if Alunos.checar_matricula(matricula_aluno):
            # Exibo o aluno
            nome_aluno, email, data_nasc = Alunos.lista[matricula_aluno]

            dados_aluno = [matricula_aluno, nome_aluno, email, data_nasc]
        
            print('\nVocê esta selecionando o(a) seguinte aluno(a):')
            exibir(dados_aluno)

            # Se não for esse professor, rodo o loop de novo
            if not geral.perguntar('\nConfirma? (s/n)'):
                continue
            
            # Fazemos uma lista com as disciplinas que ele assiste
            lista_disciplinas = []

            if matricula_aluno in Disciplinas.alunos:
                
                lista_disciplinas = Disciplinas.alunos[matricula_aluno]
            
            # Defino a pergunta que será exibida junto com o menu de busca
            pergunta_menu = '\nComo deseja achar a disciplina que o(a) aluno(a) irá assistir?'

            codigo_disciplina = recebe_disciplina(lista_disciplinas, Disciplinas)

            if codigo_disciplina:
                
                Disciplinas.adicionar_aluno(codigo_disciplina, matricula_aluno)
                print('Matriculando aluno...')
                break
        
        # Caso alguma das checagens anteriores não seja verdadeira,
        # Checo se não é para matricular um aluno

        if not geral.perguntar('\nDeseja matricular um(a) aluno(a) em alguma disciplina? (s/n)'):
            
            # Se sim, paramos o loop
            break

        # Caso contrario, repetimos o loop

    return Disciplinas

def setup():

    Alunos = entidade_aluno()

    try:
        with open('alunos.csv', 'r', encoding='UTF-8') as arq:
            max_mat_aluno = 0

            for dados in arq:

                dados = dados.split(',')
                dados[0] = int(dados[0])
                dados[3] = dados[3].rstrip()
                
                dados[3] = valida_data(dados[3])
            
                if dados[0] > max_mat_aluno:
                    max_mat_aluno = dados[0]

                Alunos.adicionar(dados)
            
            Alunos.ultima_matricula = max_mat_aluno
    except FileNotFoundError:
        print('Não tem nenhum aluno(a) gravado em disco.')
    
    return Alunos

def converte_aluno_csv(dados_aluno):
    dados_aluno[0] = str(dados_aluno[0])
    aluno_csv = ','.join(dados_aluno)
    return str(aluno_csv + '\n')

def converte_csv(Alunos):
    with open('alunos.csv', 'w', encoding='UTF-8') as arq:
        
        if Alunos.lista:
            for matricula in Alunos.lista:
                nome_aluno, email, data_nasc = Alunos.lista[matricula]
                
                data_nasc = [data_nasc.year, data_nasc.month, data_nasc.day]
                data_nasc = list(map(str, data_nasc))
                data_nasc = '-'.join(data_nasc)

                dados_aluno = [matricula, nome_aluno, email, data_nasc]
                data_nasc 
                arq.write(converte_aluno_csv(dados_aluno))
