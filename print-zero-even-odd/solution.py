import queue

class ZeroEvenOdd(object):
    def __init__(self, n):
        self.n = n
        self.x = 0
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()
        self.q3 = queue.Queue()
        self.q1.put('')

	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(self.n):
            self.q1.get()
            printNumber(0)
            if i % 2 == 0:
                self.q3.put('')
            else:
                self.q2.put('')

    def even(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(1,self.n+1):
            if i % 2 == 0:
                self.q2.get()
                printNumber(i)
                self.q1.put('')


    def odd(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(1,self.n+1):
            if i % 2 == 1:
                self.q3.get()
                printNumber(i)
                self.q1.put('')
