import threading
import time
import random

N = 5 

# um Lock para cada garfo (so uma pessoa pode usar por vez)
garfos = []
for i in range(N):
    garfos.append(threading.Lock())

# estado de cada filosofo
estado = []
tem_garfo_esquerdo = []
for i in range(N):
    estado.append("pensando")
    tem_garfo_esquerdo.append(False)


def mostrar(p, mensagem):
    print("Filosofo", p, "->", mensagem)


def filosofo(p):
    esquerda = p            # garfo i fica entre os filosofos i e (i+1)
    direita = (p + 1) % N

    for rodada in range(3):
        # PENSANDO
        estado[p] = "pensando"
        mostrar(p, "pensando")
        time.sleep(random.uniform(0.1, 0.5))

        # COM FOME
        estado[p] = "com fome"
        mostrar(p, "com fome")

        # pega o garfo da esquerda
        garfos[esquerda].acquire()
        tem_garfo_esquerdo[p] = True
        mostrar(p, "pegou o garfo da esquerda (" + str(esquerda) + ")")

        # pausa para deixar os outros pegarem o garfo deles
        # (isso faz o deadlock aparecer sempre)
        time.sleep(1)

        # tenta pegar o garfo da direita (fica esperando se estiver ocupado)
        mostrar(p, "esperando o garfo da direita (" + str(direita) + ")")
        garfos[direita].acquire()

        # COMENDO
        estado[p] = "comendo"
        mostrar(p, "COMENDO (refeicao " + str(rodada + 1) + ")")
        time.sleep(random.uniform(0.1, 0.5))

        # devolve os garfos
        garfos[direita].release()
        garfos[esquerda].release()
        tem_garfo_esquerdo[p] = False


threads = []
for p in range(N):
    t = threading.Thread(target=filosofo, args=(p,))
    t.daemon = True  # permite encerrar o programa mesmo com threads travadas
    threads.append(t)
    t.start()

#  verifica a cada segundo se ocorreu deadlock
deadlock = False
for segundo in range(20):
    time.sleep(1)

    # todos com fome, todos segurando o garfo esquerdo?
    todos_com_fome = True
    todos_com_esquerdo = True
    for p in range(N):
        if estado[p] != "com fome":
            todos_com_fome = False
        if tem_garfo_esquerdo[p] == False:
            todos_com_esquerdo = False

    if todos_com_fome and todos_com_esquerdo:
        # confirma esperando mais 2 segundos 
        time.sleep(2)
        ainda = True
        for p in range(N):
            if estado[p] != "com fome":
                ainda = False
        if ainda:
            deadlock = True
            break

    # terminou sem problemas?
    vivos = 0
    for t in threads:
        if t.is_alive():
            vivos = vivos + 1
    if vivos == 0:
        break

print()
if deadlock:
    print("*** DEADLOCK! Todos estao com fome, cada um segurando o garfo")
    print("*** da esquerda e esperando o da direita. Ninguem progride.")
else:
    print("Terminou sem deadlock desta vez.")