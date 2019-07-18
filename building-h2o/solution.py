import queue

class H2O:
    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()
        self.q1.put('')
        self.q1.put('H')


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:

        # releaseHydrogen() outputs "H". Do not change or remove this line.
        c = self.q1.get()
        if c == 'H':
            self.q2.put('')
        releaseHydrogen()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:

        # releaseOxygen() outputs "O". Do not change or remove this line.
        self.q2.get()
        releaseOxygen()
        self.q1.put('')
        self.q1.put('H')


from threading import Thread


def releaseHydrogen():
    print("H", end="")


def releaseOxygen():
    print("O", end="")



def t1(h2o):
    while True:
        h2o.hydrogen(releaseHydrogen)


def t2(h2o):
    while True:
        h2o.oxygen(releaseOxygen)


h2o = H2O()
t1 = Thread(target=t1, args=(h2o,))
t2 = Thread(target=t2, args=(h2o,))
t1.start()
t2.start()
t1.join()
t2.join()
