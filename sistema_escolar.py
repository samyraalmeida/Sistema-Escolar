import aluno
import professor
import disciplina

import geral

def setup():
	print('Estamos lendo e processando os arquivos de entrada, aguarde alguns instantes...')

	Alunos = aluno.setup()
	Professores = professor.setup()
	Disciplinas = disciplina.setup()
    
	return [Alunos, Professores, Disciplinas]

def gravar_disco(Alunos, Professores, Disciplinas):
	# Gravo em disco as alterações feitas nas estruturas

	aluno.converte_csv(Alunos)
	professor.converte_csv(Professores)
	disciplina.converte_csv(Disciplinas)

	print('Salvando...')

def busca(Alunos, Professores, Disciplinas):

	menu_busca = [
		'1. Buscar Aluno por Matrícula.',
		'2. Buscar Aluno por Nome.',
		'3. Buscar Aluno por email.',
		'4. Buscar Professor por Número.',
		'5. Buscar Professor por Nome.',
		'6. Buscar Disciplina por Código.',
		'7. Buscar Disciplina por Nome.',
		'8. Voltar ao menu principal.'
	]

	while True:
		# Leio e valido a opcao
		opcao = geral.valida_opcao_menu(menu_busca, '')
		
		if 1 <= opcao <= 3: # Aluno
			aluno.busca(opcao, Alunos, Disciplinas)
		elif 4 <= opcao <= 5: # Professor
			professor.busca(opcao, Professores, Disciplinas)
		elif 6 <= opcao <= 7: # Disciplina
			disciplina.busca(opcao, Disciplinas)
		else:
			print('\nVoltando para o menu...')
			return None

def main():
	# Leio os arquivos iniciais
	Alunos, Professores, Disciplinas = setup()
	
	menu_principal = [
		'1. Cadastrar Disciplina.',
		'2. Remover Disciplina.',
		'3. Modificar Dados de Disciplina.',
		'4. Cadastrar Aluno.',
		'5. Remover Aluno.',
		'6. Modificar Dados de Aluno.',
		'7. Matricular Aluno em Disciplina.',
		'8. Cadastrar Professor.',
		'9. Remover Professor.',
		'10. Modificar Dados de Professor.',
		'11. Associar Professor à Disciplina.',
		'12. Buscas.',
		'13. Gravar Alterações em Disco.',
		'14. Sair do Programa.'
	]

	while True:
		
		opcao = geral.valida_opcao_menu(menu_principal, '')

		if opcao == 1: 
			Disciplinas = disciplina.cadastrar(Disciplinas, Professores, Alunos)
		elif opcao == 2:
			Disciplinas = disciplina.remover(Disciplinas)
		elif opcao == 3:
			Disciplinas = disciplina.modificar(Disciplinas, Professores)
		elif opcao == 4:
			Alunos = aluno.cadastrar(Alunos)
		elif opcao == 5:
			Alunos, Disciplinas = aluno.remover(Alunos, Disciplinas)
		elif opcao == 6:
			Alunos = aluno.modificar(Alunos, Disciplinas)
		elif opcao == 7:
			Disciplinas = aluno.matricular(Alunos, Disciplinas)
		elif opcao == 8:
			Professores = professor.cadastrar(Professores)
		elif opcao == 9:
			Professores, Disciplinas = professor.remover(Professores, Disciplinas)
		elif opcao == 10:
			Professores = professor.modificar(Professores, Disciplinas)
		elif opcao == 11:
			Disciplinas = professor.associar(Professores, Disciplinas)
		elif opcao == 12:
			busca(Alunos, Professores, Disciplinas)
		elif opcao == 13:
			gravar_disco(Alunos, Professores, Disciplinas)
		else:
			print('\nSaindo do programa...')
			break

if __name__ == "__main__":
	main()
