# O codigo se inicia a partir do if__main__=='__main__'

import random
n = 255
# Criptografia
#=============================================
# A função de criptografia exige do usuario uma frase
# Sera criado frase&chave.txt em que a frase e a chave gerada pelo programa seram salvas
def criptografar():
    print("Voce escolheu Criptografar")
    mensagem = str(input('Digite a mensagem: '))
    arquivo = open('frase&chave.txt', 'w' , encoding="utf-8")

    frase = ''
    chave = []
    # Pega as letras da mensagem
    for letra in mensagem:
        indice = ord(letra) # Encontra o valor ASCII equivalente da letra
        num = random.randint(0, n) # gera uma variavel entre 0 e 255
        chave.append(num) # adiciona num a lista/chave criada anteriormente
        '''A formula para uma novo numero pode ser facilmente alterada e compartilhada com o recptor'''
        num_novo = num + indice % n # o novo indice da letra recebe a soma do indice com num sobre sobre modulo de n
        # testa se o novo valor está na tabela ASCII
        try: 
            chr_val = chr(num_novo)
        except Exception as e:
            print('Error:', e)
        letra_nova = chr(num_novo)
        frase = frase + letra_nova # adiciona o novo valor a frase gerando uma frase criptografada

    chave = '/'.join(map(str, chave)) # adiciona / entre os valores da chave

        
    print(f'Frase Criptografada: {frase}')
    print(f'Chave: {chave}')
    arquivo.writelines(f'{frase} \n{chave}') # insere frase e chave no arquivo

#=============================================
# Descriptografia 
#=============================================
# A função de descriptografia exige do usuario uma frase e uma chave com o mesmo numero de elementos
def descriptografar():
    print("Voce escolheu Descriptografar")
    # Pegar e preparar as entradas 
    opcao = int(input('Digite[0] | Usar um arquivo txt[1]'))
    if opcao != 0 and opcao != 1:
        print('[Error]')
# Input por Digitação
    elif opcao == 0:
        mensagem = str(input('Digite a Mensagem: '))
        chaveInput = str(input('Digite a Chave: '))
        chaveInput = chaveInput.split('/')
        # Caso o tamanho das entradas não sejam correspondentes
        if len(chaveInput) > len(mensagem) or len(chaveInput) < len(mensagem):
            print("[ERROR]Chave Invalida")
# Input por arquivo txt
    elif opcao == 1:
        mensagem = ''
        chaveInput = ''
        arquivo = open('frase&chave.txt', 'r', encoding="utf-8")# Abre o arquivo
        linhas = arquivo.readlines() # Le o arquivo
        mensagem = mensagem + linhas[0] # pega a linha de mensagem
        chaveInput = chaveInput + linhas[1] # pega a linha de chave
        chaveInput = chaveInput.split('/') # limpa a chave
    return mensagem, chaveInput # manda para a proxima etapa(traduzir)
        
# Tradução Dos Numeros
# Recebe a mensagem, e a chave prontas para a operação
def traduzir(mensagem, chaveInput):
    chave = list(map(int, chaveInput))# transforma a chave em lista
    i = 0
    num = []
    resultNumber = []
    # Para cada letra 
    for letra in mensagem:
        num_orig = ord(letra)# pega o valor atual
        num.append(num_orig)# adiciona em uma lista
    # Quando i for menor que o tamanho da chave
    while i < len(chave):
            """Adiciona a alteração correspondente"""
            resultNumber.append(num[i] - chave[i] % n)# realiza a operação inversa da criptografia
            i += 1
    return resultNumber# manda para a proxima etapa(transform)

# Tradução dos Numeros em Letras
# Recebe a mensagem, e a chave prontas para a operação
def transform(resultNumber):
    frase = ''
    # Para cada numero
    for num in resultNumber:
        letra_orig = chr(num)# pega a letra ASCII correspondente ao valor
        frase = frase + letra_orig# monta a frase final
    return frase, resultNumber# retorna o a frase original, e seus valores ASCII

# A partir do valor inserido pelo usuario o programa executa determinada função
def switch(valor):
    # Envia uma mensagem de erro em caso de valor invalido
    if valor != 0 and valor != 1:
      return f'[ERRO]Valor {valor} Invalido' 
    elif valor == 0:
    # 0 para criptografia
      criptografar()
    # 1 para descriptografia
    else:
        frase, chave =  descriptografar()
        frase_orig, chave_orig = transform(traduzir(frase, chave))
        print(frase_orig,chave_orig)

# Inicia o programa, e executa a função switch que recebe o valor da escolha do usuario 
# valor == 0/1
if __name__ =='__main__':
    valor = int(input('Criptografar[0] | Descriptografar[1]'))
    switch(valor)