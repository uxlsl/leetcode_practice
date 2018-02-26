from solution import Solution

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def make_list(lst):
    h = None
    p = None
    for i in lst:
        if p is None:
            h = p = ListNode(i)
        else:
            p.next = ListNode(i)
            p = p.next
    return h


def print_list(node):
    p = node
    while p != None:
        print(p.val)
        p = p.next



def test_solution():
    s = Solution()
    lst1 = make_list([1,2])
    lst2 = s.reverseList(lst1)
    print_list(lst2)
