import _thread
import time

lockA, lockB = _thread.allocate_lock(), _thread.allocate_lock()


def thread1():
    lockA.acquire()
    print("T1 adquiriu lockA")
    time.sleep(0.05)
    print("T1 tentando adquirir lockB")
    lockB.acquire()
    print("T1 concluiu")
    lockB.release()
    lockA.release()


def thread2():
    lockB.acquire()
    print("T2 adquiriu lockB")
    time.sleep(0.05)
    print("T2 tentando adquirir lockA")
    lockA.acquire()
    print("T2 concluiu")
    lockA.release()
    lockB.release()


_thread.start_new_thread(thread1, ())
_thread.start_new_thread(thread2, ())

time.sleep(5)
if lockA.locked() and lockB.locked():
    print("T1 e T2 travaram")

