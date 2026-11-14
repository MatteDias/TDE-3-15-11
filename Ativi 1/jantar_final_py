import threading
import time
import random

N = 5
REFEICOES = 3

garfos = []
for i in range(N):
    garfos.append(threading.Lock())

vezes_comeu = []
for i in range(N):
    vezes_comeu.append(0)

def mostrar(p, mensagem):
    print("Filosofo", p, "->", mensagem)

def filosofo(p):
    garfo_a = p            # garfo da esquerda
    garfo_b = (p + 1) % N  # garfo da direita

    if garfo_a < garfo_b:
        menor = garfo_a
        maior = garfo_b
    else:
        menor = garfo_b
        maior = garfo_a

    for rodada in range(REFEICOES):
        mostrar(p, "pensando")
        time.sleep(random.uniform(0.1, 0.5))

        mostrar(p, "com fome")

        garfos[menor].acquire()
        mostrar(p, "pegou o garfo " + str(menor))

        garfos[maior].acquire()
        mostrar(p, "pegou o garfo " + str(maior))

        vezes_comeu[p] = vezes_comeu[p] + 1
        mostrar(p, "COMENDO (refeicao " + str(vezes_comeu[p]) + ")")
        time.sleep(random.uniform(0.1, 0.5))

        garfos[maior].release()
        garfos[menor].release()
        mostrar(p, "largou os garfos " + str(maior) + " e " + str(menor))


threads = []
for p in range(N):
    t = threading.Thread(target=filosofo, args=(p,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print()
print("Todos terminaram! Nenhum deadlock.")
print("Quantas vezes cada filosofo comeu:")
for p in range(N):
    print("  Filosofo", p, ":", vezes_comeu[p], "vezes")

todos_iguais = True
for p in range(N):
    if vezes_comeu[p] != REFEICOES:
        todos_iguais = False

if todos_iguais:
    print("Justica OK: todos comeram o mesmo numero de vezes (sem inanicao).")
else:
    print("Atencao: alguem nao comeu o suficiente!")