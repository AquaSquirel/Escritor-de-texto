import os as sistema
from datetime import datetime

#armazena o nome do usuario atual na variavel usuario
usuario = sistema.getlogin()

#cria um arquivo de texto com o nome do usuario atual
arquivo = open(f'texto_de_{usuario.lower()}.txt', 'w')

#faz a pergunto do que deve ser escrito no arquivo
texto = input('O que quer escrever no arquivo?\n')

# Divida o texto em palavras
palavras = texto.split()

# Agrupe as palavras em grupos de 5
grupos_de_palavras = [palavras[n:n+10] for n in range(0, len(palavras), 10)]

# Junte as palavras em cada grupo e adicione uma nova linha entre os grupos
texto_formatado = '\n'.join(' '.join(grupo) for grupo in grupos_de_palavras)

#escreve o texto no arquivo
arquivo.write(f'Texto de {usuario.capitalize()}\n\n{texto_formatado.capitalize()}\n')

#pega a data e hora atual e armazena na variavel data_e_hora_atuais
data_e_hora_atuais = datetime.now()

#formata a data e hora atual e armazena na variavel data_e_hora_em_texto
data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')

#escreve a data e hora no arquivo
arquivo.write('\n'+str(data_e_hora_em_texto))