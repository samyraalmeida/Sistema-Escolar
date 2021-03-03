import geral
import disciplina

'''
Professor contém:
    * Número de Matrícula
    * Nome.
'''

class entidade_professor():

    def __init__(self):# Estrutura dos professores 
        self.ultima_matricula = 0
        self.lista = {}
        self.nomes = {}

    def checar_matricula(self, matricula_prof):
        # Checo se a matricula do professor existe
        if matricula_prof in self.lista:
            # Se sim, retorno verdadeiro
            return True
        else:
            # Se não, retorno falso
            return False

    def adicionar_nome(self, matricula_prof, nome_prof):
        # Adiciono o nome do professor a lista de nomes
        nome_prof = geral.formata_nome(nome_prof)

        if not nome_prof in self.nomes:
            self.nomes[nome_prof] = []
        
        self.nomes[nome_prof].append(matricula_prof)

    def deletar_nome(self, matricula_prof, nome_prof):
        # Deleto o nome do professor da lista de nomes        
        nome_prof = geral.formata_nome(nome_prof)

        self.nomes[nome_prof].remove(matricula_prof)

        if not self.nomes[nome_prof]:
            self.nomes.pop(nome_prof)

    def adicionar(self, matricula_prof, nome_prof):
        # Crio o professor
        self.ultima_matricula = matricula_prof
        self.lista[matricula_prof] = nome_prof
        
        self.adicionar_nome(matricula_prof, nome_prof)

    def deletar(self, matricula_prof):
        nome_prof = self.lista[matricula_prof]

        self.deletar_nome(matricula_prof, nome_prof)
        self.lista.pop(matricula_prof)

    def alterar(self, matricula_prof, novo_nome_prof):
        antigo_nome_prof = self.lista[matricula_prof]

        self.deletar_nome(matricula_prof, antigo_nome_prof)
        self.adicionar_nome(matricula_prof, novo_nome_prof)

        self.lista[matricula_prof] = novo_nome_prof

def exibir(dados_prof, disciplinas_ministradas = [], exibir_disc = False):
    
    matricula_prof, nome_prof = dados_prof

    # Exibo a matricula e o nome do professor
    print(f"Matrícula:                          {matricula_prof}")
    print(f"Nome:                               {nome_prof}")
    
    # Checo se é para exibir as disciplinas que o professor ministra
    if exibir_disc:
        
        # Transformo a lista de disciplinas em uma string que contem os códigos das disciplinas

        disciplinas_ministradas = list(map(str, disciplinas_ministradas))
        disciplinas_ministradas = ' '.join(disciplinas_ministradas)
        
        # Se o professor não ministra nenhuma disciplina
        if not disciplinas_ministradas:
            disciplinas_ministradas = 'Esse(a) professor(a) não ministra nenhuma matéria.'

        # Exibo os codigos das disciplinas, se ele ministra alguma, caso contrário exibo 
        # uma mensagem informando que o professor não ministra nenhuma disciplina
        print(f"Código das disciplinas ministradas: {disciplinas_ministradas}")

def recebe_nome():
    while True:
        try: 
            # Leio o nome do professor
            print('\nDigite o nome do(a) professor(a):')
            nome_prof = input('> ')
            
            # Checo se o formato do nome esta ok
            if geral.valida_nome(nome_prof): 
                
                # Se sim, retorno o nome
                return nome_prof
        except ValueError:
            
            # Se deu erro, exibo uma mensagem que deu erro
            print('O nome do(a) professor(a) só deve conter letras do alfabeto.')
            print('Você digitou:', nome_prof)

def cadastrar(Professores):

    while True:
        matricula_prof = Professores.ultima_matricula + 1
        
        # Leio o nome do professor
        nome_prof = recebe_nome()

        dados_prof = [matricula_prof, nome_prof]

        # Exibo os dados do professor
        print('\nVocê está criando o(a) seguinte professor(a):')
        exibir(dados_prof)

        # Checo se é para confirmar o cadastro
        if geral.perguntar('\nConfirmar cadastro? (s/n)'):
            
            # Se sim, cadastro o professor
            Professores.adicionar(matricula_prof, nome_prof)
            print('Cadastrando professor(a)...')

            break
        
        # Caso contrário,
        # Checo se não é para cadastrar um professor
        if not geral.perguntar('\nDeseja cadastrar um(a) professor(a)? (s/n)'):
            
            # Se sim, paro o loop
            break

        # Caso contrario repetimos o loop

    return Professores

def recebe_matricula():
    while True:
        try:
            # Leio a matricula do professor
            print('\nDigite a matrícula do(a) professor(a):')
            matricula_prof = input('> ')
            matricula_prof = int(matricula_prof) 
            
            # Se a matricula digitada for um número inteiro
            return matricula_prof
        except ValueError:

            # Caso não seja, exibo uma mensagem de erro
            print('A matrícula do(a) professor(a) é númerica.')
            print('Você digitou:', matricula_prof)

def pesquisa_matricula(pesq_matricula, Professores):

    # Irei buscar todas as matriculas dos professores que contem 'pesq_matricula'

    # Essa lista vai conter todas as matriculas que se encaixam da condição anterior
    lista_professores = []

    # Transformo pesq_matricula em uma string, a fim de facilitar as proximas checagens
    pesq_matricula_str = str(pesq_matricula)

    # Passo por todas as matriculas dos professores
    for matricula_prof in Professores.lista.keys():

        matricula_prof_str = str(matricula_prof)
        # checo se pesq_matricula esta contida em  matricula_prof
        if pesq_matricula_str in matricula_prof_str:
            # Se sim, adiciono matricula_prof a lista dos professores
            lista_professores.append(matricula_prof)

    # Se algum professor satisfaz a busca
    if lista_professores:

        # Retorno a lista de professores
        return lista_professores

    # Caso contrário, retorno um erro de chave
    raise KeyError

def pesquisa_nome(pesq_nome, Professores):
    # Irei buscar todas as matriculas dos professores que contem 'nos quais seus nomes contem 'pesq_nome'

    # Essa lista vai conter todas as matriculas que se encaixam da condição anterior
    lista_professores = []

    # Formato o nome digitado, ou seja, tiro os acentos e coloco todos os caracteres minusculos
    pesq_nome_formatado = geral.formata_nome(pesq_nome)

    # Passo por todas as matriculas dos professores
    for nome_prof in Professores.nomes.keys():
        
        # Checo se pesq_nome_formatado está contido em nome_prof
        if pesq_nome_formatado in nome_prof:

            # Se sim, adiciono todos os professores que tem esse nome na lista de professores
            lista_professores += Professores.nomes[nome_prof]

    # Se algum professor satisfaz a busca
    if lista_professores:
        
        # Retorno a lista de professores
        return lista_professores

    # Caso contrário, retorno um erro de chave
    raise KeyError 

def busca_exibindo_escolhendo_resultados(lista_professores, Professores, Disciplinas):
    
    print('\nOs(as) professores(as) que satisfazem sua busca são:')

    # Exibo todos os professores que satisfazem ao nome digitado
    for matricula_prof in lista_professores:

        dados_prof = [matricula_prof, Professores.lista[matricula_prof]]

        disciplinas_ministradas = []

        if matricula_prof in Disciplinas.professores:
            disciplinas_ministradas = Disciplinas.professores[matricula_prof]
        
        print('\nExibindo professor:')
        exibir(dados_prof, disciplinas_ministradas, True)

    # Pego o código do professor
    while True:
        print('\nEscolha um(a) dos(as) professores(as) mostrados acima e digite sua matrícula.', end = '')
        
        matricula_prof = recebe_matricula()
        
        if matricula_prof in lista_professores:
            return matricula_prof
        else:
            print('Digite uma das matrículas dos professores(as) mostrados(as) acima.')

def busca_matricula(Professores, Disciplinas):

    try:
        # Leio a matricula que foi digitada
        pesq_matricula = recebe_matricula()

        # Monto uma lista com os codigos dos professores que satisfazem a busca
        lista_professores = pesquisa_matricula(pesq_matricula, Professores)

        # Exibo todos na tela e escolho o professor desejado
        return busca_exibindo_escolhendo_resultados(lista_professores, Professores, Disciplinas) 
    except KeyError:
        # Caso o código não exista        
        print(f'Nenhum resultado encontrado para a matrícula: {pesq_matricula}.')

def busca_nome(Professores, Disciplinas):
    try:
        # Leio o nome que foi digitado
        pesq_nome = recebe_nome()

        # Monto uma lista com os codigos dos professores que satisfazem a busca
        lista_professores = pesquisa_nome(pesq_nome, Professores)

        # Exibo todos na tela e escolho o professor desejado
        return busca_exibindo_escolhendo_resultados(lista_professores, Professores, Disciplinas) 
    except KeyError:
        # Caso o nome não exista
        print(f'Nenhum resultado encontrado para o nome "{pesq_nome}".')
        
def busca(opcao, Professores, Disciplinas):

    # Se opcao = 4, iremos realizar uma busca por matrícula.
    # Se opcao = 5, iremos realizar uma busca por nome.
    
    matricula_prof = int()

    if opcao == 4: 
        # Busca por matrícula
        print('\nBusca por matrícula', end = '')
        matricula_prof = busca_matricula(Professores, Disciplinas)
    else: 
        # Busca por nome
        print('\nBusca por nome', end = '')
        matricula_prof = busca_nome(Professores, Disciplinas)
    
    if matricula_prof:

        dados_prof = [matricula_prof, Professores.lista[matricula_prof]]

        disciplinas_ministradas = []

        if matricula_prof in Disciplinas.professores:
            disciplinas_ministradas = Disciplinas.professores[matricula_prof]
        
        print('\nExibindo professor:')
        exibir(dados_prof, disciplinas_ministradas, True)

def recebe_busca(pergunta_menu, Professores, Disciplinas):
        
    # opções de busca pelo professor
    menu_busca_professor = [
        '1. Buscar Professor por Número.',
        '2. Buscar Professor por Nome.'
    ]

    opcao = geral.valida_opcao_menu(menu_busca_professor, pergunta_menu)

    matricula_prof = int()

    if opcao == 1: 
        # Buscar por código
        matricula_prof = busca_matricula(Professores, Disciplinas)
    else: 
        # Buscar por nome
        matricula_prof = busca_nome(Professores, Disciplinas)

    return matricula_prof

def modificar(Professores, Disciplinas):
    while True:
        # Defino a pergunta que será exibida junto com o menu de busca
        pergunta_menu = '\nComo deseja achar o(a) professor(a) que você irá modificar?'

        # Realizo a busca para saber qual professor vai ser alterado
        matricula_prof = recebe_busca(pergunta_menu, Professores, Disciplinas)

        # Checo se o professor existe de fato
        if Professores.checar_matricula(matricula_prof):
            
            # Leio a alteração no professor
            novo_nome_prof = recebe_nome()

            # Exibo o professor com a alteração
            print('\nExibindo professor(a) após as alterações:')
            exibir([matricula_prof, novo_nome_prof])

            # Checo se é para confirmar a modificação
            if geral.perguntar('\nConfirmar modificação? (s/n)'):
                
                # Se sim, altero o professor
                Professores.alterar(matricula_prof, novo_nome_prof)
                print('Modificando professor(a)...')
                # Paro o loop
                break

        # Caso alguma das checagens anteriores não seja verdadeira,
        # Checo se não é para modificar um professor
        if not geral.perguntar('\nDeseja modificar um(a) professor(a)? (s/n)'):
            # Se sim, paro o loop
            break
        
        # Caso contrario repetimos o loop

    return Professores

def remover(Professores, Disciplinas):
    while True:
        # Defino a pergunta que será exibida junto com o menu de busca
        pergunta_menu = '\nComo deseja achar o professor que você irá remover?'

        # Realizo a busca para saber qual professor vai ser removido
        matricula_prof = recebe_busca(pergunta_menu, Professores, Disciplinas)

        # Checo se o professor existe de fato
        if Professores.checar_matricula(matricula_prof):
            # Exibo o professor antes de remove-lo

            print('\nExibindo o(a) professor(a):')
            exibir([matricula_prof, Professores.lista[matricula_prof]])

            # Checo se é para confirmar a remoção
            if geral.perguntar('\nConfirmar remoção? (s/n)'):
                # Se sim, removo o professor

                if matricula_prof in Disciplinas.professores:
                    
                    lista_disciplinas = []

                    for codigo_disciplina in Disciplinas.professores[matricula_prof]:
                        lista_disciplinas.append(codigo_disciplina)

                    for codigo in lista_disciplinas:
                        Disciplinas.deletar_professor(codigo, matricula_prof)

                Professores.deletar(matricula_prof)
                print('Removendo professor(a)...')
                # Paro o loop
                break
                
        # Caso alguma das checagens anteriores não seja verdadeira,
        # Checo se não é para remover um professor

        if not geral.perguntar('\nDeseja remover um(a) professor(a)? (s/n)'):
            
            # Se sim, paramos o loop
            break

        # Caso contrario, repetimos o loop

    return [Professores, Disciplinas]

def recebe_disciplina(lista_disciplinas, Disciplinas):
    while geral.perguntar('\nDeseja associar alguma disciplina à esse professor? (s/n)'):
        # Defino a pergunta que será exibida junto com o menu de busca
        pergunta_menu = '\nComo deseja achar a disciplina que o professor irá ministrar?'

        # Realizo a busca para saber qual disciplina será ministrada
        codigo_disciplina = disciplina.recebe_busca(pergunta_menu, Disciplinas)

        # Checo se a disciplina existe de fato
        if not Disciplinas.checar_codigo(codigo_disciplina):
            print('Por favor, digite uma disciplina válida.')
            continue

        dias_horarios = Disciplinas.lista[codigo_disciplina][1]
        matricula_prof = Disciplinas.lista[codigo_disciplina][2]

        if matricula_prof:
            print('Essa disciplina já tem um professor associado.')
            continue        
        
        # Se os horarios da disciplina chocarem com os do professor
        if not disciplina.checar_disponibilidade(lista_disciplinas, dias_horarios, Disciplinas):
            # Exibimos uma mensagem de erro e rodamos o loop de novo
            print('Os horários do(a) professor(a) chocam com o da disciplina.')
            continue
        
        nome_disciplina, dias_horarios, matricula_prof, local, num_vagas = Disciplinas.lista[codigo_disciplina]
        
        alunos_matriculados = []
        
        if codigo_disciplina in Disciplinas.matriculas:
            alunos_matriculados = Disciplinas.matriculas[codigo_disciplina]

        dados_disciplina = [codigo_disciplina, nome_disciplina, dias_horarios, matricula_prof, local, num_vagas, alunos_matriculados]

        print('\nVocê esta associando a seguinte disciplina ao professor(a):')
        disciplina.exibir(dados_disciplina)

        # Se for para cadastrar
        if geral.perguntar('\nConfirma? (s/n)'):
            # Retorno o codigo da disciplina
            return codigo_disciplina
        
        # Caso contrário o loop ira se repetir

def associar(Professores, Disciplinas):

    while True:
        # Defino a pergunta que será exibida junto com o menu de busca
        pergunta_menu = '\nComo deseja achar o(a) professor(a) que você irá associar a uma disciplina?'

        # Realizo a busca para saber qual professor vai ser removido
        matricula_prof = recebe_busca(pergunta_menu, Professores, Disciplinas)

        # Checo se o professor existe de fato
        if Professores.checar_matricula(matricula_prof):
            
            # Exibo o professor que você ira cadastrar
            print('\nVocê esta selecionando o seguinte professor(a):')
            exibir([matricula_prof, Professores.lista[matricula_prof]])

            # Se não for esse professor, rodo o loop de novo
            if not geral.perguntar('\nConfirma? (s/n)'):
                continue

            lista_disciplinas = []

            if matricula_prof in Disciplinas.professores:
                # Fazemos uma lista com as disciplinas que ele ministra
                lista_disciplinas = Disciplinas.professores[matricula_prof]

            codigo_disciplina = recebe_disciplina(lista_disciplinas, Disciplinas)
            
            if codigo_disciplina:
                
                Disciplinas.adicionar_professor(codigo_disciplina, matricula_prof)
                print('Associando professor à disciplina...')
                break
                
        # Caso alguma das checagens anteriores não seja verdadeira,
        # Checo se não é para associar um professor

        if not geral.perguntar('\nDeseja associar um(a) professor(a) a alguma disciplina? (s/n)'):
            
            # Se sim, paramos o loop
            break

        # Caso contrario, repetimos o loop

    return Disciplinas

def setup():
    Professores = entidade_professor()
    
    try:

        with open('professores.csv', 'r', encoding='UTF-8') as arq:
            max_mat_prof = 0

            for dados in arq:

                dados = dados.split(',')
                matricula = int(dados[0])
                nome = dados[1].rstrip()
                
                if matricula > max_mat_prof:
                    max_mat_prof = matricula
            
                Professores.adicionar(matricula, nome)
            
            Professores.ultima_matricula = max_mat_prof     
    except FileNotFoundError:
        print('Não tem nenhum professor(a) gravado em disco.')
    
    return Professores

def converte_prof_csv(dados_prof):
    prof_csv = ','.join([str(dados_prof[0]), dados_prof[1]])
    return str(prof_csv + '\n')

def converte_csv(Professores):
    with open('professores.csv', 'w', encoding='UTF-8') as arq:
        
        if Professores.lista:
            for matricula in Professores.lista:
                arq.write(converte_prof_csv([matricula, Professores.lista[matricula]]))
