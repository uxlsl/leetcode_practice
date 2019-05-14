from solution import Solution

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def make_node(lst):
    head = p = ListNode(lst[0])
    for i in lst[1:]:
        p.next = ListNode(i)
        p = p.next
    return head

def print_node(head):
    p = head
    s = ''
    while p:
        s += '{}>'.format(p.val)
        p = p.next
    print(s)

def test_solution():
    s = Solution()
    head = make_node([1,4,3,2,5,2])
    s.partition(head, 3)
