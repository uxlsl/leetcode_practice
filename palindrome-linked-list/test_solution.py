from solution import Solution, ListNode


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
    l = make_list([1,2,3,2,1])
    assert s.isPalindrome(l)

