import threading

def f1():
    import tg_bot
def f2():
    import vk_bot


t1 = threading.Thread(target=f1)
t2 = threading.Thread(target=f2)

t1.start()
t2.start()