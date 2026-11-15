# Vou importar as bibliotecas necessárias
import threading
import time

# Criar variáveis para uso
contador = 0
numero_de_threads = 8 # porteiro
incrementos = 200000 # numero de acoes por porteiro
lista_de_threads = [] # lista de threads


# Função para somar o contador (escrever no quadro) V0
def soma (numerodevezes):
    global contador
    for i in range(numerodevezes):
        contador += 1

# somar o contador sem semáforo (escrever no quadro) V1
def soma_sem_semaforo (numerodevezes):
    global contador
    for i in range(numerodevezes):
        verificar = contador
        time.sleep(0) # pausa para dar a chance de troca das threads
        contador = verificar + 1
        
start_time = time.perf_counter() # verificar quanto tempo demora para executar
# Criar as threads (que farão a funcão de somar(escrever no quadro))
for i in range(numero_de_threads):
    thread = threading.Thread(target=soma_sem_semaforo, args=(incrementos,)) # passa o que vai fazer e quantas vezes 
    lista_de_threads.append(thread) # adiciona a thread na lista
    thread.start() # inicia


for thread in lista_de_threads: 
    thread.join() # espera a thread terminar

print("O valor final do contador é: ", contador) # imprime o valor final do contador
print("O valor esperado do contador é: ", numero_de_threads * incrementos) # imprime o valor esperado do contador
print(f"Demorou {time.perf_counter() - start_time:.2f} s") # imprime o tempo que demorou para executar


