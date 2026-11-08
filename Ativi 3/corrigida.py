import _thread


# Pseudocódigo de referência (versão corrigida — hierarquia)
# Regra global: sempre adquirir LOCK_A antes de LOCK_B,
# em TODAS as threads.
# Thread 1 e Thread 2:
# adquirir(LOCK_A)
# adquirir(LOCK_B)
# // secao critica
# liberar(LOCK_B)
# liberar(LOCK_A)