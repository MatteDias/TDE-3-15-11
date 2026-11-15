# Vou importar as bibliotecas necessárias
import threading
import time

# Criar variáveis para uso
contador = 0
numero_de_threads = 8 # porteiro
incrementos = 200000 # numero de acoes por porteiro
lista_de_threads = [] # lista de threads
semaforo = threading.Semaphore(1) # criando o semáforo

# somar o contador com semáforo (escrever no quadro) V2
def soma_com_semaforo (numerodevezes):
    global contador
    for i in range(numerodevezes):
        semaforo.acquire() # pega a caneta, se uma thread estiver usando, a outra espera
        try:
            verificar = contador # comparação com a função sem semáforo
            time.sleep(0) # comparação
            contador = verificar + 1 # comparar
        finally:
            semaforo.release() # devolve a caneta sempre, mesmo se der erro, para não travar o programa


start_time = time.perf_counter() # verificar quanto tempo demora para executar
# Criar as threads (que farão a funcão de somar(escrever no quadro))
for i in range(numero_de_threads):
    thread = threading.Thread(target=soma_com_semaforo, args=(incrementos,)) # passa o que vai fazer e quantas vezes 
    lista_de_threads.append(thread) # adiciona a thread na lista
    thread.start() # inicia


for thread in lista_de_threads: 
    thread.join() # espera a thread terminar

print("O valor final do contador é: ", contador) # imprime o valor final do contador
print("O valor esperado do contador é: ", numero_de_threads * incrementos) # imprime o valor esperado do contador
print(f"Demorou {time.perf_counter() - start_time:.2f} s") # imprime o tempo que demorou para executar

