import _thread
import time

lockA, lockB = _thread.allocate_lock(), _thread.allocate_lock()


def thread1():
    lockA.acquire()
    print("T1 adquiriu lockA\n")
    time.sleep(0.05)    
    print("T1 tentando adquirir lockB\n")
    lockB.acquire()
    print("T1 concluiu\n")
    lockB.release()
    lockA.release()


def thread2():
    lockB.acquire()
    print("T2 adquiriu lockB\n")
    time.sleep(0.05)
    print("T2 tentando adquirir lockA\n")
    lockA.acquire()
    print("T2 concluiu\n")
    lockA.release()
    lockB.release()


_thread.start_new_thread(thread1, ())
_thread.start_new_thread(thread2, ())

time.sleep(5)
if lockA.locked() and lockB.locked():
    print("T1 e T2 travaram\n")

