class Solution(object):
    def calculateii(self, s):
        stack = []
        x = iter(s)
        while True:
            try:
                c = next(x)
                if c == '*':
                    a = stack.pop()
                    b = next(x)
                    c = a * b
                    stack.append(c)
                elif c == '/':
                    a = stack.pop()
                    b = next(x)
                    c = a // b
                    stack.append(c)
                else:
                    stack.append(c)
            except StopIteration:
                break
        result = 0
        while stack:
            a = stack.pop()
            if not stack:
                return result + a
            op = stack.pop()
            if op == '+':
                result += a
            if op == '-':
                result -= a
        return result

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def f(s):
            c = ''
            for i in s:
                if i.isspace():
                    continue
                if i.isnumeric():
                    c += i
                else:
                    if c != '':
                        yield int(c)
                        c = ''
                    yield i
            if c != '':
                yield int(c)

        stack = []
        for c in f(s):
            if c == ')':
                l = []
                while True:
                    a = stack.pop()
                    if a == '(':
                        break
                    l.append(a)
                l = l[::-1]
                x = self.calculateii(l)
                stack.append(x)
            else:
                stack.append(c)
        return self.calculateii(stack)
