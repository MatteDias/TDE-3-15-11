import _thread
import time

lockA, lockB = _thread.allocate_lock(), _thread.allocate_lock()

def thread1():
    lockA.acquire()
    print("T1 concluiu acquireA")
    time.sleep(0.05)
    lockB.acquire()
    print("T1 concluiu acquireB")
    lockB.release()
    print("T1 concluiu releaseB")
    lockA.release()
    print("T1 concluiu releaseA")


def thread2():
    lockA.acquire()
    print("T2 concluiu acquireA")
    time.sleep(0.05)
    lockB.acquire()
    print("T2 concluiu acquireB")
    lockB.release()
    print("T2 concluiu releaseB")
    lockA.release()
    print("T2 concluiu releaseA")


_thread.start_new_thread(thread1, ())
_thread.start_new_thread(thread2, ())

time.sleep(1)
if lockA.locked() and lockB.locked():
    print("T1 e T2 travaram")
else:
    print("DEu boa")
