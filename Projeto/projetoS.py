#!/usr/bin/env python3
import socket
import os
import threading
import Class


TAM_MSG = 1024 # Tamanho do bloco de mensagem
HOST = '0.0.0.0' # IP do Servidor
PORT = 40000 # Porta que o Servidor escuta

def processar_cliente(con, cliente):
    print('Cliente conectado', cliente)
    while True:
        msg = con.recv(TAM_MSG)
        if not msg: break
        msg = msg.decode().split(' ')
        campos = ' '.join(msg[1:])


        if msg[0].upper() == 'PM':
            arq = open('ListRelogio.csv', 'r')
            txt = arq.readlines()
            l = False
            for k in range(len(txt)):
                linha = txt[k].split(',')
                if linha[1].replace(' ','') == campos:
                    l = True
                    con.send(str.encode(txt[k]))
                    break
                    
            if l == False:
                con.send(str.encode('-ERR'))
            arq.close()


        elif msg[0].upper() == 'CNM':
            try:
                arqr = open('ListRelogio.csv', 'a+')
                arqr.write(campos)
                arqr.close()
                con.send(str.encode('+OK'))
            except Exception as e:
                con.send(str.encode('-ERR {}'.format(e)))
   


        elif msg[0].upper() == 'QUIT':
            con.send(str.encode('+OK\n'))
            break
        else:
            con.send(str.encode('-ERR Invalid command\n'))
    con.close()
    print('Cliente desconectado', cliente)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv = (HOST, PORT)
sock.bind(serv)
sock.listen(50)
while True:
    try:
        con, cliente = sock.accept()
    except: break
    threading.Thread(target=processar_cliente, args=(con, cliente)).start()
    
sock.close()