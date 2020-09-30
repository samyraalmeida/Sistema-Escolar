import geral
import professor
import aluno

'''
Disciplina contém:

    * Código da Disciplina.
    * Nome da Disciplina.
    * Lista de dias e horários da disciplina (por exemplo: seg 10-12, qua 14-16, sex 10-12)
    * Professor que ministra a disciplina.
    * Local.
    * Número de Vagas.
    * Lista de Alunos Matriculados.
'''

class entidade_disciplina():
    
    def __init__(self):
        self.lista = {}
        self.nomes = {}
        self.locais = {}
        self.alunos = {}
        self.professores = {}
        self.matriculas = {}

    def checar_codigo(self, codigo_disciplina):
        # Checo se o código da disciplina existe
        if codigo_disciplina in self.lista:
            # Se sim, retorno verdadeiro
            return True
        else:
            # Se não, retorno falso
            return False
    
    def adicionar_nome(self, codigo_disciplina, nome_disciplina):

        # Adiciono o nome da disciplina a lista de nomes
        nome_disciplina = geral.formata_nome(nome_disciplina)

        if not nome_disciplina in self.nomes:
            self.nomes[nome_disciplina] = []

        self.nomes[nome_disciplina].append(codigo_disciplina)

    def deletar_nome(self, codigo_disciplina, nome_disciplina):

        # Deleto o nome da disciplina a lista de nomes
        nome_disciplina = geral.formata_nome(nome_disciplina)

        self.nomes[nome_disciplina].remove(codigo_disciplina)

        if not self.nomes[nome_disciplina]:
            self.nomes.pop(nome_disciplina)

    def adicionar_local(self, codigo_disciplina, local):
        # Adiciono o local da disciplina a lista de locais
        local = geral.formata_nome(local)

        if not local in self.locais.keys():
            self.locais[local] = []
        
        self.locais[local].append(codigo_disciplina)

    def deletar_local(self, codigo_disciplina, local):
        # Deleto o local da disciplina a lista de locais
        local = geral.formata_nome(local)

        self.locais[local].remove(codigo_disciplina)
        
        if not self.locais[local]:
            self.locais.pop(local)

    def adicionar_professor(self, codigo_disciplina, matricula_prof):
        
        # Adiciono um professor a uma disciplina
        self.lista[codigo_disciplina][2] = matricula_prof

        if matricula_prof:
            if not matricula_prof in self.professores:
                self.professores[matricula_prof] = []

            self.professores[matricula_prof].append(codigo_disciplina)

    def deletar_professor(self, codigo_disciplina, matricula_prof):
        # Deleto um professor de uma disciplina
        self.lista[codigo_disciplina][2] = int()
        
        if matricula_prof:
            self.professores[matricula_prof].remove(codigo_disciplina)

            if not self.professores[matricula_prof]:
                self.professores.pop(matricula_prof)
    
    def adicionar_aluno(self, codigo_disciplina, matricula_aluno):
        # Adiciono um aluno a algunma disciplina
        if not codigo_disciplina in self.matriculas:
            self.matriculas[codigo_disciplina] = []

        self.matriculas[codigo_disciplina].append(matricula_aluno)

        if not matricula_aluno in self.alunos:
            self.alunos[matricula_aluno] = []

        self.alunos[matricula_aluno].append(codigo_disciplina)

    def deletar_aluno(self, codigo_disciplina, matricula_aluno):
        # Deleto um aluno a alguma disciplina
        if matricula_aluno:
            
            self.alunos[matricula_aluno].remove(codigo_disciplina)

            self.matriculas[codigo_disciplina].remove(matricula_aluno)

            if not self.alunos[matricula_aluno]:
                self.alunos.pop(matricula_aluno)

            if not self.matriculas[codigo_disciplina]:
                self.matriculas.pop(codigo_disciplina)

    def adicionar(self, dados_disciplina):
        # Adiciono a disciplina a estrutura
        codigo_disciplina, nome_disciplina, dias_horarios, matricula_prof, local, num_vagas, alunos_matriculados = dados_disciplina

        self.lista[codigo_disciplina] = [nome_disciplina, dias_horarios, matricula_prof, local, num_vagas]

        self.adicionar_nome(codigo_disciplina, nome_disciplina)
        self.adicionar_professor(codigo_disciplina, matricula_prof)
        self.adicionar_local(codigo_disciplina, local)
        
        if alunos_matriculados:
            for aluno in alunos_matriculados:
                self.adicionar_aluno(codigo_disciplina, aluno)

    def deletar(self, codigo_disciplina):
        # Deleto o aluno da estrutura
        nome_disciplina = self.lista[codigo_disciplina][0]
        matricula_prof = self.lista[codigo_disciplina][2]
        local = self.lista[codigo_disciplina][3]

        self.deletar_nome(codigo_disciplina, nome_disciplina)
        self.deletar_professor(codigo_disciplina, matricula_prof)
        self.deletar_local(codigo_disciplina, local)

        if codigo_disciplina in self.matriculas:
            alunos_matriculados = []
            for aluno in self.matriculas[codigo_disciplina]:
                alunos_matriculados.append(aluno)

            for aluno in alunos_matriculados:
                self.deletar_aluno(codigo_disciplina, aluno)
        
        self.lista.pop(codigo_disciplina)

    def alterar(self, novos_dados):
        codigo_disciplina, nv_nome_disciplina, nv_dias_horarios, nv_matricula_prof, nv_local, nv_num_vagas = novos_dados
        # Altero os dados da disciplina
        
        # Pego os antigos dados e os deleto da estrutura
        ant_nome_disciplina, ant_dias_horarios, ant_matricula_prof, ant_local, ant_num_vagas = self.lista[codigo_disciplina]

        self.deletar_nome(codigo_disciplina, ant_nome_disciplina)
        self.deletar_professor(codigo_disciplina, ant_matricula_prof)
        self.deletar_local(codigo_disciplina, ant_local)

        # Adiciono os novos dados à estrutura

        self.adicionar_nome(codigo_disciplina, nv_nome_disciplina)
        self.adicionar_professor(codigo_disciplina, nv_matricula_prof)
        self.adicionar_local(codigo_disciplina, nv_local)

        self.lista[codigo_disciplina] = [nv_nome_disciplina, nv_dias_horarios, nv_matricula_prof, nv_local, nv_num_vagas]

def converte_horarios_str(dias_horarios):

    dias_semana = []

    for dia in dias_horarios.keys():
        if dias_horarios[dia]:
            
            dia_atual = dia + ': ' + ', '.join(dias_horarios[dia])
            dias_semana.append(dia_atual)

    return dias_semana

def converte_dias_horarios_str(dias_horarios, separe = '\n'):
    exibir_dias_horarios = converte_horarios_str(dias_horarios)
    exibir_dias_horarios = separe.join(exibir_dias_horarios)

    if not exibir_dias_horarios:
        exibir_dias_horarios = 'Essa disciplina não acontece em nenhum dia e horário.'

    return exibir_dias_horarios

def exibir(dados_disciplina):
    
    codigo_disciplina, nome_disciplina, dias_horarios, matricula_prof, local, num_vagas, alunos_matriculados = dados_disciplina

    # Ajeito a data para a exibição
    dias_horarios = converte_dias_horarios_str(dias_horarios, '\n                                ')

    if not matricula_prof:
        matricula_prof = 'Essa disciplina não possui nenhum professor cadastrado.'

    # Ajeito a lista dos alunos para a exibição
    alunos_matriculados = list(map(str, alunos_matriculados))
    alunos_matriculados = ' '.join(alunos_matriculados)
    
    if not alunos_matriculados:
        alunos_matriculados = 'Essa disciplina não possui nenhum aluno matriculado.'

    # Exibo os dados da disciplina
    print(f"Código:                         {codigo_disciplina}")
    print(f"Nome:                           {nome_disciplina}")
    print(f"Dias e Horários:                {dias_horarios}")
    print(f"Código Professor:               {matricula_prof}")
    print(f"Local:                          {local}")
    print(f"Número de vagas:                {num_vagas}")
    print(f"Codigo dos alunos matriculados: {alunos_matriculados}")

def recebe_codigo():
    while True:
        try:
            # Leio o código digitado
            print('\nDigite o código da disciplina:')
            codigo_disciplina = input('> ')
            
            if not codigo_disciplina.isalnum():
                raise ValueError
            
            codigo_disciplina = geral.tirar_acentos(codigo_disciplina)
            
            # Se o código da disciplina estiver no padrão, retorno o codigo
            return codigo_disciplina
        except ValueError:
            print('O código deve ser formado por letras e/ou números.')
            print('Você digitou:', codigo_disciplina)

def valida_nome(nome_disciplina):

    separar_nome = nome_disciplina.split(' ')
    
    # Checo se o nome so é composto por letras do alfabeto
    for nome in separar_nome: 
        if not nome.isalnum(): # Caso não seja, ok recebe falso
            raise ValueError
    
    # Se o código chegou até aqui, significa que o nome é valido
    return True

def recebe_nome():

    while True:
        try:
            # Leio o nome da disciplina
            print('\nDigite o nome da disciplina:')
            nome_disciplina = input('> ')
            
            # Checo se o formato do nome esta ok
            if valida_nome(nome_disciplina):

                # Se sim, retorno o nome
                return nome_disciplina
        except ValueError:
            
            # Se deu erro, exibo uma mensagem que deu erro
            print('O nome da disciplina precisa ser composto somente por letras e números.')
            print('Você digitou:', nome_disciplina)

def valida_horario(horario, tipo):
    
    # Checo se o horario = -1 e estamos checando o horario final da aula, o horario é inválido
    if horario == '-1':
        if tipo == 1:
            print('Os horários devem seguir a formatação: HH:MM, ex: 09:30, 10:00.')
            raise ValueError
        else:
            return True

    horas, minutos = ['','']
    
    if ':' in horario:
        horas, minutos = horario.split(':')
    else:
        horas = horario

    # Se o horario está vazio, o horario é inválido
    if not horas and not minutos:
        print('Os horários devem seguir a formatação: HH:MM, ex: 09:30, 10:00.')
        raise ValueError
    
    if horas == '':
        horas = '0'
    
    if minutos == '':
        minutos = '0'

    if len(minutos) == 1:
        minutos += '0'
    
    # Se o horario não é númerico, o horario é inválido
    if not horas.isnumeric() or not minutos.isnumeric():
        print('As horas e os minutos devem ser compostos por números.')


    horas = int(horas)
    minutos = int(minutos)

    # Nos proximos if's iremos checar se a hora e os minutos digitado são validos.

    if 1 < horas > 23:
        print('As horas devem estar entre 0 e 23 horas.')
        raise ValueError
    
    if 1 < minutos > 59:
        print('Os minutos devem estar entre 0 e 59 minutos.')
        raise ValueError

    return True

def formate_horario(horario):

    if horario != '-1':
        
        horas, minutos = ['','']
        if ':' in horario:
            horas, minutos = horario.split(':')
        else:
            horas = horario
        
        # Formato a hora

        if horas == '':
            horas = '0'
        
        if minutos == '':
            minutos = '0'

        if len(minutos) == 1:
            minutos += '0'

        horas = int(horas)
        minutos = int(minutos)
    
        if 0 <= horas <= 9:
            horas = f'0{horas}'

        if 0 <= minutos <= 9:
            minutos = f'0{minutos}'

        # Concateno o horario
        horario = f'{horas}:{minutos}'
    
    return horario

def recebe_horario(tipo):
    # se tipo = 0, estamos lendo o horario de inicio da aula 
    # se tipo = 1, estamos lendo o horario de final da aula
    distincao = ['\nHorário do INICIAL da aula: ', '\nHorário do FINAL da aula: ']

    while True:
        try:
            print(distincao[tipo])
            horario = input('> ')

            # Checo se a hora é válida
            if valida_horario(horario, tipo):

                return formate_horario(horario)
        except ValueError:
            print('Você digitou:', horario)

def checar_sobreposicao_horarios(horario1, horario2):

    inicio1, final1 = horario1.split('-')
    inicio2, final2 = horario2.split('-')

    # Note que podemos utilizar a ordem lexografica para saber se um horario vem antes de outro, daí:
    # Iremos testar se não existe sobreposição de horarios
    return (inicio1 < final1 <= inicio2) or (inicio2 < final2 <= inicio1)

def valida_dias_horarios(dias_horarios):

    grade = False

    for dia in dias_horarios.keys():
    
        dias_horarios[dia].sort()

        num_horarios = len(dias_horarios[dia])

        if num_horarios:
            grade = True

        for num in range(0, num_horarios - 1, 1):
        
            if not checar_sobreposicao_horarios(dias_horarios[dia][num], dias_horarios[dia][num + 1]):
                return False

    return grade

def recebe_dias_horarios():

    while True:
        print('\nLendo a grade de dias e horários:')
        # Vamos ler os dias e os hórarios de uma disciplina
        dias_horarios = {}
        dias_semana = ['dom','seg','ter','qua','qui','sex','sab']

        for dia in dias_semana:
            
            print('\nCaso desejar não cadastrar mais nenhum horário, digite -1.')
            print(f'{dia}: ', end = '')
            
            dias_horarios[dia] = []

            while True:
                inicio = recebe_horario(0)
            
                if inicio == '-1':
                    break
            
                final = recebe_horario(1)

                if inicio < final:
                    dias_horarios[dia].append(f'{inicio}-{final}')
                else:
                    print('O inicio da aula precisa acontecer antes que seu termino.')

        if valida_dias_horarios(dias_horarios):
            print('\nA disciplina acontecerá nos seguintes dias e horários:')
            print(converte_dias_horarios_str(dias_horarios))
            
            if geral.perguntar('\nConfirmar o cadastro desses horários? (s/n)'):
                return dias_horarios
        
        print('Por favor, digite uma grade de horários válida com no mínimo um horário cadastrado e sem sobreposições.')
        # Caso algum dos if's seja falso, repetimos o loop de novo

def checar_disponibilidade(lista_disciplinas, dias_horarios, Disciplinas):
    
    # Se o professor ministra alguma disciplina, vamos checar se não há conflitos de horários
    dias_semana = ['dom','seg','ter','qua','qui','sex','sab']

    # Passo por todas as disciplinas que o professor ministra
    for disciplina in lista_disciplinas:
        
        # Para cada dia da semana
        for dia in dias_semana:

            # Passo por todos os horarios da disciplina no dia
            for horario1 in Disciplinas.lista[disciplina][1][dia]:
                
                # Passo por todos os horarios da nova disciplina no dia
                for horario2 in dias_horarios[dia]:
                    
                    # Se os horarios coincidem, o professor não pode ministrar essa disciplina 
                    # retorno False
                    if not checar_sobreposicao_horarios(horario1, horario2):
                        return False

    # Depois de realizar todos as checagens, não houve nenhuma sobreposição de horarios, 
    # logo o professor pode ministrar essa disciplina. Retorno True
    return True

def recebe_professor(dias_horarios, Disciplinas, Professores):
    while geral.perguntar('\nVocê deseja cadastrar um(a) professor(a) à essa disciplina?'):
        # Definimos a pergunta que será exibida com o menu de busca pelo professor
        pergunta_menu = '\nComo deseja achar o professor que você irá cadastrar?'

        matricula_prof = professor.recebe_busca(pergunta_menu, Professores, Disciplinas)

        # Se o professor não existe rodamos o loop de novo
        if not matricula_prof:
            print('Por favor, digite um professor válido.')
            continue

        # Se o chegamos até aqui significa que o código do professor digitado é válido.
        # Se o professor já ministra alguma aula, checamos sua disponibilidade.

        if matricula_prof in Disciplinas.professores:
            # Fazemos uma lista com as disciplinas que ele ministra
            lista_disciplinas = Disciplinas.professores[matricula_prof]

            # Se o professor não tiver disponibilidade
            if not checar_disponibilidade(lista_disciplinas, dias_horarios, Disciplinas):
                # Exibimos uma mensagem de erro e rodamos o loop de novo
                print('Os horários do(a) professor(a) chocam com o da disciplina.')
                continue
        
        # Exibo o professor que você ira cadastrar
        print('\nVocê esta cadastrando o seguinte professor(a) à disciplina:')
        professor.exibir([matricula_prof, Professores.lista[matricula_prof]])

        # Se for para cadastrar
        if geral.perguntar('\nConfirmar cadastro? (s/n)'):
            # Retorno a matricula do professor
            return matricula_prof
        
        # Caso contrário o loop ira se repetir

def valida_local(local):
    separar_local = local.split(' ')
    
    # Checo se o nome so é composto por letras do alfabeto
    for nome in separar_local: 
        if not nome.isalnum(): # Caso não seja, ok recebe #falso
            raise ValueError
    
    # Se o código chegou até aqui, significa que o nome do local é válido
    return True

def recebe_local(dias_horarios, Disciplinas):
    while True:
        try:
            # Leio o nome do local
            print('\nDigite o local da disciplina:')
            local = input('> ')

            # Checo se o nome digitado é um nome válido
            if valida_local(local):

                # Se o local ja tiver cadastrado, checaremos sua disponibilidade
                local_formatado = geral.formata_nome(local)

                if local_formatado in Disciplinas.locais.keys(): 
                    lista_disciplinas = Disciplinas.locais[local_formatado]
                    
                    # Se o local não tiver disponibilidade
                    if not checar_disponibilidade(lista_disciplinas, dias_horarios, Disciplinas):                        
                        print('Os horários em que o local está sendo utilizado chocam com o da disciplina.')
                        # Rodamos tudo de novo
                        continue

                # Se chegarmos até aqui, significa que é um lugar novo ou que o local possui disponibilidade,
                # portanto, retornamos local
                return local
        except ValueError:
            print('O nome do local só deve conter letras e/ou números.')
            print('Você digitou:', local)

def recebe_vagas(minimo_vagas = 1):

    while True:
        try:
            # Leio o número de vagas
            print('\nDigite o número de vagas da disciplina:')
            vagas = input('> ')
            vagas = int(vagas)

            # Se chegamos aqui, significar que vagas é um número inteiro
            # Daí, checamos se vagas >= que o numero minimo de vagas
            if vagas >= minimo_vagas:
                # Se sim, retornamos vagas
                return vagas
            else:
                # Se chegamos aqui, significar que vagas <= 0
                raise ValueError
        except ValueError:
            print(f'O número de vagas precisa ser um número inteiro maior ou igual a {minimo_vagas}.')
            print('Você digitou:', vagas)

def recebe_aluno(dias_horarios, Disciplinas, Alunos):
    while geral.perguntar('\nDeseja matricular um(a) aluno(a) à essa disciplina?'):
        # Definimos a pergunta que será exibida com o menu de busca pelo aluno
        pergunta_menu = '\nComo deseja achar o aluno que você irá matricular?'        

        matricula_aluno = aluno.recebe_busca(pergunta_menu, Alunos, Disciplinas)

        # Se o aluno não existe rodamos o loop de novo
        if not matricula_aluno:
            print('Por favor, digite um aluno válido.')
            continue
        
        # Se o chegamos até aqui significa que a matricula do aluno digitado é válida.
        # Se o aluno já assiste alguma aula, checamos sua disponibilidade.

        if matricula_aluno in Disciplinas.alunos:
            # Fazemos uma lista com as disciplinas que ele assiste
            lista_disciplinas = Disciplinas.alunos[matricula_aluno]

            if not checar_disponibilidade(lista_disciplinas, dias_horarios, Disciplinas):
                # Exibimos uma mensagem de erro e rodamos o loop de novo
                print('Os horários do(a) aluno(a) chocam com o da disciplina.')
                continue
        
        # Exibo o aluno que você ira matricular
        nome_aluno, email, data_nasc = Alunos.lista[matricula_aluno]

        dados_aluno = [matricula_aluno, nome_aluno, email, data_nasc]

        # Exibo o aluno que você ira cadastrar
        print('\nVocê esta matriculando o(a) seguinte aluno(a) à disciplina:')
        aluno.exibir(dados_aluno)

        # Se for para cadastrar
        if geral.perguntar('\nConfirmar matrícula? (s/n)'):
            # Retorno a matricula do aluno
            return matricula_aluno
        
        # Caso contrário o loop ira se repetir

def recebe_alunos(dias_horarios, num_vagas, Disciplinas, Alunos):

    alunos_matriculados = []
    vagas_disponiveis = num_vagas

    # Repetirermos o loop enqunato houver vagas disponiveis
    while vagas_disponiveis:
        
        matricula_aluno = recebe_aluno(dias_horarios, Disciplinas, Alunos)

        # Se matricula_aluno == None
        if not matricula_aluno:
            # Paro de cadastrar novos alunos
            break
        
        # Checo se o aluno ja não esta na lista de alunos
        if matricula_aluno in alunos_matriculados:
            print('O aluno já será matriculado na disciplina.')
            continue

        # Caso contrario
        # Adiciono a matricula do aluno a lista de alunos
        alunos_matriculados.append(matricula_aluno)
        # Diminuiu a quantidade de vagas disponiveis
        vagas_disponiveis -= 1

    # Retorno os alunos que seram matriculados na disciplina
    return alunos_matriculados    
    
def cadastrar(Disciplinas, Professores, Alunos):
    while True:
        # Leio o codigo
        codigo_disciplina = recebe_codigo()

        # Peço o código enquanto o codigo que foi digitado ja estiver cadastrado
        while Disciplinas.checar_codigo(codigo_disciplina):
            print('Esse código já foi cadastrado em outra disciplina.')

            codigo_disciplina = recebe_codigo()

        # Leio o nome da disciplina
        nome_disciplina = recebe_nome()

        # Leio os dias e horarios em que a disciplina irá acontecer
        dias_horarios = recebe_dias_horarios()

        # Leio o professor que ira ministrar essa disciplina
        matricula_prof = recebe_professor(dias_horarios, Disciplinas, Professores)
        
        # Leio o local da disciplina
        local = recebe_local(dias_horarios, Disciplinas)

        # Leio o número de vagas
        num_vagas = recebe_vagas()

        # Leio os alunos que serão matriculados nessa disciplina
        alunos_matriculados = recebe_alunos(dias_horarios, num_vagas, Disciplinas, Alunos)

        # Crio uma lista com os dados da disciplina, afim de facilitar nossa vida
        dados_disciplina = [codigo_disciplina, nome_disciplina, dias_horarios, matricula_prof, local, num_vagas, alunos_matriculados]

        print('\nVocê está criando a seguinte disciplina:')
        exibir(dados_disciplina)

        if geral.perguntar('\nConfirmar cadastro? (s/n)'):
            
            # Se sim, cadastro a disciplina
            Disciplinas.adicionar(dados_disciplina)
            print('Cadastrando disciplina...')

            # Paro o loop 
            break
        
        # Caso contrário,
        # Checo se não é para cadastrar uma disciplina

        if geral.perguntar('\nDeseja cadastrar uma disciplina? (s/n)'):
            
            # Se sim, paro o loop
            break
        
        # Caso contrário o looo ira se repetir

    return Disciplinas

def pesquisa_codigo(pesq_codigo, Disciplinas):

    # Irei buscar todas os códigos das disciplinas que contem 'pesq_codigo'
    # Essa lista vai conter todos os códigos que se encaixam da condição anterior
    lista_disciplinas = []

    # Transformo pesq_codigo em uma string, a fim de facilitar as proximas checagens
    pesq_codigo_str = str(pesq_codigo)

    # Passo por todos os códigos das disciplinas
    for codigo_disciplina in Disciplinas.lista.keys():

        codigo_disciplina_str = str(codigo_disciplina)

        # checo se pesq_codigo esta contida em  codigo_disciplina

        if pesq_codigo_str in codigo_disciplina_str:
            # Se sim, adiciono codigo_disciplina a lista das disciplinas
            lista_disciplinas.append(codigo_disciplina)

    # Se alguma disciplina satisfaz a busca
    if lista_disciplinas:

        # Retorno a lista de disciplinas
        return lista_disciplinas

    # Caso contrário, retorno um erro de chave
    raise KeyError

def pesquisa_nome(pesq_nome, Disciplinas):
    # Irei buscar todas os códigos das disciplinas que contem nos quais seus nomes contem 'pesq_nome'

    # Essa lista vai conter todos os códigos que se encaixam da condição anterior
    lista_disciplinas = []

    # Formato o nome digitado, ou seja, tiro os acentos e coloco todos os caracteres minusculos
    pesq_nome_formatado = geral.formata_nome(pesq_nome)

    # Passo por todos os códigos das disciplinas
    for nome_disciplina in Disciplinas.nomes.keys():
        
        # Checo se pesq_nome_formatado está contido em nome_disciplina
        if pesq_nome_formatado in nome_disciplina:

            # Se sim, adiciono todos as disciplinas que tem esse nome na lista de disciplinas
            lista_disciplinas += Disciplinas.nomes[nome_disciplina]

    # Se alguma disciplina satisfaz a busca
    if lista_disciplinas:
        
        # Retorno a lista de disciplinas
        return lista_disciplinas

    # Caso contrário, retorno um erro de chave
    raise KeyError

def busca_exibindo_escolhendo_resultados(lista_disciplinas, Disciplinas):

    print('\nAs disciplinas que satisfazem sua busca são:')

    # Exibo todos as disciplinas que satisfazem ao nome digitado
    for codigo_disciplina in lista_disciplinas:
        
        nome_disciplina, dias_horarios, matricula_prof, local, num_vagas = Disciplinas.lista[codigo_disciplina]
        
        alunos_matriculados = []
        
        if codigo_disciplina in Disciplinas.matriculas:
            alunos_matriculados = Disciplinas.matriculas[codigo_disciplina]

        dados_disciplina = [codigo_disciplina, nome_disciplina, dias_horarios, matricula_prof, local, num_vagas, alunos_matriculados]

        print('\nExibindo disciplina:')
        exibir(dados_disciplina)

    # Pego o código da disciplina
    while True:
        print('\nEscolho uma das disciplinas mostradas acima e digite o seu código.', end = '')

        codigo_disciplina = recebe_codigo()

        if codigo_disciplina in lista_disciplinas:
            return codigo_disciplina
        else:
            print('Digite um dos códigos das disciplinas mostradas acima.')

def busca_codigo(Disciplinas):
    try:
        # Leio o código que foi digitado
        pesq_codigo = recebe_codigo()

        # Monto uma lista com os codigos das disciplinas que satisfazem a busca
        lista_disciplinas = pesquisa_codigo(pesq_codigo, Disciplinas)

        # Exibo todos na tela e escolho a disciplina desejada
        return busca_exibindo_escolhendo_resultados(lista_disciplinas, Disciplinas)
    except KeyError:
        # Caso o código não exista
        print(f"Nenhum resultado encontrado para o código {pesq_codigo}.")

def busca_nome(Disciplinas):
    try:
        # Leio o nome que foi digitado
        pesq_nome = recebe_nome()

        # Monto uma lista com os codigos das disciplinas que satisfazem a busca

        lista_disciplinas = pesquisa_nome(pesq_nome, Disciplinas)

        # Exibo todos na tela e escolho a disciplina desejada
        return busca_exibindo_escolhendo_resultados(lista_disciplinas, Disciplinas)
    except KeyError:
        # Caso o nome não exista
        print(f'Nenhum resultado encontrado para o nome "{pesq_nome}".')

def busca(opcao, Disciplinas):
    # Se opcao = 6, iremos realizar uma busca por matrícula.
    # Se opcao = 7, iremos realizar uma busca por nome.

    codigo_disciplina = str()

    if opcao == 6: 
        # Busca por matrícula
        print('\nBusca por matrícula', end = '')
        codigo_disciplina = busca_codigo(Disciplinas)
    else: 
        # Busca por nome
        print('\nBusca por nome', end = '')
        codigo_disciplina = busca_nome(Disciplinas)

    if codigo_disciplina:
        nome_disciplina, dias_horarios, matricula_prof, local, num_vagas = Disciplinas.lista[codigo_disciplina]
        
        alunos_matriculados = []
        
        if codigo_disciplina in Disciplinas.matriculas:
            alunos_matriculados = Disciplinas.matriculas[codigo_disciplina]

        dados_disciplina = [codigo_disciplina, nome_disciplina, dias_horarios, matricula_prof, local, num_vagas, alunos_matriculados]

        print('\nExibindo disciplina:')
        exibir(dados_disciplina)

def recebe_busca(pergunta_menu, Disciplinas):

    # Opções de busca pelo aluno
    menu_busca_disciplina = [
        '1. Buscar Disciplina por Código.',
        '2. Buscar Disciplina por Nome.'
    ]

    opcao = geral.valida_opcao_menu(menu_busca_disciplina, pergunta_menu)

    codigo_disciplina = str()

    if opcao == 1: 
        # Busca por matrícula
        codigo_disciplina = busca_codigo(Disciplinas)
    else: 
        # Busca por nome
        codigo_disciplina = busca_nome(Disciplinas)

    return codigo_disciplina

def recebe_modificacoes(opcao, codigo_disciplina, Disciplinas, Professores):

    # Checo qual alteração está sendo feita nesse momento
    if opcao == 0:
        # Modifico o nome da disciplina
        return recebe_nome()
    elif opcao == 1:
        # Modifico a lista de dias e horarios
        dias_horarios = Disciplinas.lista[codigo_disciplina][1]
        matricula_prof = Disciplinas.lista[codigo_disciplina][2]
        alunos_matriculados = []

        if codigo_disciplina in Disciplinas.matriculas:
            alunos_matriculados = Disciplinas.matriculas[codigo_disciplina]

        if not matricula_prof and not alunos_matriculados:
            return recebe_dias_horarios()
        else:
            print('Você não pode modificar a grade horária de uma disciplina que já possui alunos matriculados e/ou o professor cadastrado.')
            return dias_horarios
    elif opcao == 2:
        # Modifico o professor
        dias_horarios = Disciplinas.lista[codigo_disciplina][1]
        return recebe_professor(dias_horarios, Disciplinas, Professores)
    elif opcao == 3:
        # Modifico o local
        dias_horarios = Disciplinas.lista[codigo_disciplina][1]
        return recebe_local(dias_horarios, Disciplinas)
    elif opcao == 4:
        # Modifico o numero de vagas
        alunos_matriculados = []

        if codigo_disciplina in Disciplinas.matriculas:
            alunos_matriculados = Disciplinas.matriculas[codigo_disciplina]

        return recebe_vagas(len(alunos_matriculados))
    
def modificar(Disciplinas, Professores):
    while True:
        # Defino a pergunta que será exibida junto com o menu de busca
        pergunta_menu = '\nComo deseja achar a disciplina que você irá modificar?'

        # Realizo a busca para saber qual disciplina vai ser alterada
        codigo_disciplina = recebe_busca(pergunta_menu, Disciplinas)

        # Checo se a disciplina existe de fato:
        if Disciplinas.checar_codigo(codigo_disciplina):
            
            # Crio uma lista com as possiveis modificações na disciplina
            opcoes_modificacoes_disciplina = [
                '\nDeseja modificar o Nome da Disciplina?',
                '\nDeseja modificar a Lista de dias e horários?',
                '\nDeseja modificar o Professor que ministra a disciplina?',
                '\nDeseja modificar o Local?',
                '\nDeseja modificar o Número de Vagas?'
            ]

            # Crio um vetor que vai conter os novos dados da disciplina
            novos_dados = [codigo_disciplina]

            # Percorro a lista de possiveis modificações, checando se é ou não para alterar esse dado da disciplina
            for opcao in range(5):

                # A pergunta a alteracao em questão
                pergunta_modificar = opcoes_modificacoes_disciplina[opcao]

                # O valor do dado que será adicionado a disciplina ou o mesmo que antes se não alterarmos nada
                adicionar = Disciplinas.lista[codigo_disciplina][opcao]

                # Checo se é para alterar o dado
                if geral.perguntar(pergunta_modificar):
                    # Se sim realizo a alteração
                    adicionar = recebe_modificacoes(opcao, codigo_disciplina, Disciplinas, Professores)
                
                # Adiciono o dado na lista atualizado na disciplina
                novos_dados.append(adicionar)

            alunos_matriculados = []
            
            if codigo_disciplina in Disciplinas.matriculas:
                alunos_matriculados = Disciplinas.matriculas[codigo_disciplina]

            novos_dados.append(alunos_matriculados)

            print('\nExibindo disciplina após as alterações:')
            exibir(novos_dados)

            # Checo se é para confirmar a modificação
            if geral.perguntar('\nConfirmar modificação? (s/n)'):
                novos_dados.remove(alunos_matriculados)

                # Se sim, altero a disciplina
                Disciplinas.alterar(novos_dados)
                print('Modificando disciplina...')
                # Paro o loop
                break

        # Caso alguma das checagens anteriores não seja verdadeira,
        # Checo se não é para modificar uma disciplina
        if not geral.perguntar('\nDeseja modificar uma disciplina? (s/n)'):
            
            # Se sim, paro o loop
            break
        
        # Caso contrario o loop irá se repetir

    return Disciplinas

def converte_dias_horarios_estrutura(dados):
    dias_horarios = {}
    dias_semana = ['dom','seg','ter','qua','qui','sex','sab']

    dados = dados.split(';')

    for dia in dias_semana:
        dias_horarios[dia] = []
    
    for horario in dados:
        horario = horario.split(': ')
        
        dia_sem = horario[0]
        
        intervalo = horario[1].split('-')
        inicio, final = intervalo
    
        inicio = formate_horario(inicio)
        final = formate_horario(final)

        dias_horarios[dia_sem].append(f"{inicio}-{final}")

    return dias_horarios

def remover(Disciplinas):
    while True:
        # Defino a pergunta que será exibida junto com o menu de busca
        pergunta_menu = '\nComo deseja achar a disciplina que você irá remover?'

        # Realizo a busca para saber qual disciplina vai ser removida
        codigo_disciplina = recebe_busca(pergunta_menu, Disciplinas)

        # Checo se a disciplina existe de fato
        if Disciplinas.checar_codigo(codigo_disciplina):
            nome_disciplina, dias_horarios, matricula_prof, local, num_vagas = Disciplinas.lista[codigo_disciplina]
            
            alunos_matriculados = []
            
            if codigo_disciplina in Disciplinas.matriculas:
                alunos_matriculados = Disciplinas.matriculas[codigo_disciplina]

            dados_disciplina = [codigo_disciplina, nome_disciplina, dias_horarios, matricula_prof, local, num_vagas, alunos_matriculados]
            
            print('\nExibindo disciplina:')
            exibir(dados_disciplina)

            # Checo se é para confirmar a remoção
            if geral.perguntar('\nConfirmar remoção? (s/n)'):
                # Se sim, removo a disciplina
                Disciplinas.deletar(codigo_disciplina)
                print('Removendo disciplina...')
                # Paro o loop
                break
        
        # Caso alguma das checagens anteriores não seja verdadeira,
        # Checo se não é para remover uma disciplina
        if not geral.perguntar('\nDeseja remover uma disciplina? (s/n)'):
            
            # Se sim, paro o loop
            break
        
        # Caso contrario o loop irá se repetir

    return Disciplinas

def setup():

    Disciplinas = entidade_disciplina()
    
    try:
        with open('disciplinas.csv', 'r', encoding='UTF-8') as arq:
            
            for dados in arq:

                dados = dados.split(',')
                dados[2] = converte_dias_horarios_estrutura(dados[2])
                dados[3] = int(dados[3])
                dados[5] = int(dados[5].rstrip())
                dados.append([])

                Disciplinas.adicionar(dados)
        
        with open('matriculas.csv', 'r', encoding='UTF-8') as arq:
            
            for dados in arq:
                
                dados = dados.split(',')
                
                dados[1] = dados[1].rstrip()
                
                if dados[1]:
                    dados[1] = dados[1].split(' ')
                    dados[1] = list(map(int, dados[1]))
                else:
                    dados[1] = list()
                
                for aluno in dados[1]:
                    Disciplinas.adicionar_aluno(dados[0], aluno)
    except FileNotFoundError:
        print('Não tem nenhuma disciplina gravada em disco.')

    return Disciplinas

def converte_dias_horarios_csv(dias_horarios):
    dias_horarios_csv = []

    for dia in dias_horarios.keys():

        if dias_horarios[dia]:
            
            for horario in dias_horarios[dia]:
                dias_horarios_csv.append(f"{dia}: {horario}")
    
    dias_horarios_csv = ';'.join(dias_horarios_csv)

    return dias_horarios_csv
    
def converte_disciplina_csv(dados_disciplinas):
    dados_disciplinas[2] = converte_dias_horarios_csv(dados_disciplinas[2])
    if not dados_disciplinas[3]:
        dados_disciplinas[3] = 0

    dados_disciplinas = list(map(str, dados_disciplinas))

    disc_csv = ','.join(dados_disciplinas)
    return str(disc_csv + '\n')

def converte_matriculas_csv(codigo_disicplina, alunos_matriculados):
    alunos_matriculados = list(map(str, alunos_matriculados))
    
    alunos_matriculados = ' '.join(alunos_matriculados)
    matriculas_csv = ','.join([codigo_disicplina, alunos_matriculados])

    return str(matriculas_csv + '\n')

def converte_csv(Disciplinas):
    with open('disciplinas.csv', 'w', encoding='UTF-8') as arq:
        if Disciplinas.lista:
            for codigo in Disciplinas.lista:

                nome_disciplina, dias_horarios, matricula_prof, local, num_vagas = Disciplinas.lista[codigo]

                dados_disciplina = [codigo, nome_disciplina, dias_horarios, matricula_prof, local, num_vagas]
                arq.write(converte_disciplina_csv(dados_disciplina))
    
    with open('matriculas.csv', 'w', encoding='UTF-8') as arq_mat:

        if Disciplinas.lista:
            for codigo in Disciplinas.lista:
            
                alunos_matriculados = []
        
                if codigo in Disciplinas.matriculas:
                    alunos_matriculados = Disciplinas.matriculas[codigo]
                
                arq_mat.write(converte_matriculas_csv(codigo, alunos_matriculados))
