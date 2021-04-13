from exe115.lib.a_interface import *

arq = 'cursoemvídeo.txt'

cabeçalho('SISTEMA ARQUIVO v1.1')
if arquivoExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    criarArquivo(arq)
menu(['Ver pessoas cadastradas', 'Cadastrar pessoas novas', 'Sair do programa'], arq)