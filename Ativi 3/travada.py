import _thread

LOCK_A, LOCK_B = _thread.allocate_lock(), _thread.allocate_lock()


# Pseudocódigo de referência (versão que trava)
# LOCK_A, LOCK_B = locks distintos
# Thread 1:
# adquirir(LOCK_A)
# dormir(50ms) // aumenta a chance do deadlock
# adquirir(LOCK_B)
# imprimir "T1 concluiu"
# liberar(LOCK_B)
# liberar(LOCK_A)
# Thread 2:
# adquirir(LOCK_B)
# dormir(50ms)
# adquirir(LOCK_A)
# imprimir "T2 concluiu"
# liberar(LOCK_A)
# liberar(LOCK_B)
