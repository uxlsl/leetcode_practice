from solution import Solution


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return 'ListNode({})->{}'.format(self.val,self.next)

def make(lst):
    p = head = ListNode(lst[0])
    for i in lst[1:]:
        p.next = ListNode(i)
        p = p.next
    return head

def print_list(head):
    p = head
    while p:
        print(p.val, end="->")
        p = p.next
    print()

def test_solution():
    s = Solution()
