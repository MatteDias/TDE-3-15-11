import _thread
import time

lockA, lockB = _thread.allocate_lock(), _thread.allocate_lock()

def thread1():
    lockA.acquire()
    print("T1 concluiu acquireA\n")
    time.sleep(0.05)
    lockB.acquire()
    print("T1 concluiu acquireB\n")
    lockB.release()
    print("T1 concluiu releaseB\n")
    lockA.release()
    print("T1 concluiu releaseA\n")


def thread2():
    lockA.acquire()
    print("T2 concluiu acquireA\n")
    time.sleep(0.05)
    lockB.acquire()
    print("T2 concluiu acquireB\n")
    lockB.release()
    print("T2 concluiu releaseB\n")
    lockA.release()
    print("T2 concluiu releaseA\n")


_thread.start_new_thread(thread1, ())
_thread.start_new_thread(thread2, ())

time.sleep(1)
if lockA.locked() and lockB.locked():
    print("T1 e T2 travaram\n")
else:
    print("DEu boa\n")
