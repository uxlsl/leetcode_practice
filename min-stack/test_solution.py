from solution import MinStack


def test_solution():
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(3)
    print(obj.stack)
    print(obj.getMin())
    print(obj.pop())
    print(obj.top())
    print(obj.getMin())
