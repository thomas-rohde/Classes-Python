from time import sleep

# a -> bruto do sistema
def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def leianum(msg):
    while True:
        try:
            i = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO! Digite um nº inteiro válido\033[m')
        else:
            if i > 3 and msg == 'Sua opção: ':
                print(f'\033[31mERRO! Digite um nº inteiro válido\033[m')
            else:
                return i


def menu(lista, arq):
    while True:
        cabeçalho('MENU PRINCIPAL')
        for c, item in enumerate(lista):
            print(f'{c + 1} - {item}')
        print(linha())
        r = leianum('Sua opção: ')
        if r != 3:
            sleep(1)
            cabeçalho(lista[r - 1])
        sleep(0.5)
        if r == 1:
            # Opção de listar o conteúdo de um arquivo.
            lerArquivo(arq)
        elif r == 2:
            # Opção de sair do sistema.
            nome = str(input('Nome: '))
            idade = leianum('Idade: ')
            cadastrar(arq, nome, idade)
        else:
            break


# b -> Arquivos
def arquivoExiste(arquivo):
    try:
        a = open(arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()



# c -> Adicionando nomes ao arquivo
def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO ao escrever os dados!')
        else:
            print('Novo registro de nome adicionado!')
