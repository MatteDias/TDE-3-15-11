import threading
import time
import random

N = 5

garfos = []
for i in range(N):
    garfos.append(threading.Lock())

estado = []
tem_garfo_esquerdo = []
for i in range(N):
    estado.append("pensando")
    tem_garfo_esquerdo.append(False)

def mostrar(p, mensagem):
    print("Filosofo", p, "->", mensagem)

def filosofo(p):
    esquerda = p
    direita = (p + 1) % N

    for rodada in range(3):
        estado[p] = "pensando"
        mostrar(p, "pensando")
        time.sleep(random.uniform(0.1, 0.5))

        estado[p] = "com fome"
        mostrar(p, "com fome")

        garfos[esquerda].acquire()
        tem_garfo_esquerdo[p] = True
        mostrar(p, "pegou o garfo da esquerda (" + str(esquerda) + ")")
        time.sleep(1)

        mostrar(p, "esperando o garfo da direita (" + str(direita) + ")")
        garfos[direita].acquire()

        estado[p] = "comendo"
        mostrar(p, "COMENDO (refeicao " + str(rodada + 1) + ")")
        time.sleep(random.uniform(0.1, 0.5))

        garfos[direita].release()
        garfos[esquerda].release()
        tem_garfo_esquerdo[p] = False


threads = []
for p in range(N):
    t = threading.Thread(target=filosofo, args=(p,))
    t.daemon = True  # permite encerrar o programa mesmo com threads travadas
    threads.append(t)
    t.start()

deadlock = False
for segundo in range(20):
    time.sleep(1)

    todos_com_fome = True
    todos_com_esquerdo = True
    for p in range(N):
        if estado[p] != "com fome":
            todos_com_fome = False
        if tem_garfo_esquerdo[p] == False:
            todos_com_esquerdo = False

    if todos_com_fome and todos_com_esquerdo:
        time.sleep(2)
        ainda = True
        for p in range(N):
            if estado[p] != "com fome":
                ainda = False
        if ainda:
            deadlock = True
            break

    vivos = 0
    for t in threads:
        if t.is_alive():
            vivos = vivos + 1
    if vivos == 0:
        break

print()
if deadlock:
    print("* Todos estao com fome, cada um segurando o garfo")
    print("* Da esquerda e esperando o da direita. Ninguem avanca.")
else:
    print("Terminou sem deadlock desta vez.")