class Solution(object):
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
        x = f(s)
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
