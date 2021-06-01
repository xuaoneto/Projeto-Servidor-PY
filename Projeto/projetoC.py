#!/usr/bin/env python3
import socket
import sys
import Class

TAM_MSG = 1024 # Tamanho do bloco de mensagem
HOST = '127.0.0.1' # IP do Servidor
PORT = 40000 # Porta que o Servidor escuta
if len(sys.argv) > 1:
    HOST = sys.argv[1]
print('Servidor:', HOST+':'+str(PORT))
serv = (HOST, PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(serv)
print('Para sair use QUIT, Ctrl+D ou CTRL+C\n')
while True:
    print('''
         [1] - Cadastrar Novo modelo 
         [2] - Pesquisar Modelos 
         [3] - QUIT 
        ''')
    try:
        cmd = input('Loja> ')
    except:
        cmd = '5'
    if cmd[0] == '1':

        marca = input('Digite a MARCA do Relógio:')
        modelo = input('Digite o MODELO do Relógio:')
        cor = input('Digite a COR do Relógio:')
        preco = input('Digite o PREÇO do Relógio:')
        descricao = input('Digite uma DESCRIÇÃO para o Relógio:')
        disponibilidade = input('Quantas Unidades estão disponíveis:')

        if input('Deseja Cadastrar? S/N: ').upper() == 'S':

            sock.send(str.encode('CNM {}, {}, {}, {}, {}, {}\n'.format(marca, modelo, cor, preco, descricao, disponibilidade)))

            dados = sock.recv(TAM_MSG)
            if not dados: break
            msg_status = dados.decode().split()

            if msg_status[0] == '+OK':
                print('Cadastro Realizado!')
            else:
                print('Erro ao Cadastrar!', msg_status[1:])
        


    elif cmd[0] == '2':
        modelo = input('Digite o MODELO do Relógio:')
        sock.send(str.encode('{} {}'.format('PM',modelo)))

        dados = sock.recv(TAM_MSG)
        if dados.decode() != '-ERR':
            linha = dados.decode().split(',')
            bonito = Class.Relogio(linha[0],linha[1],linha[2],linha[3],linha[4],linha[5])
            print(bonito)
        else:
            print('Modelo não emcontrado!')

    elif cmd[0] == '3':
        break

    
sock.close()

