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

def to_list(node):
    lst = []
    p = node
    while p != None:
        lst.append(p.val)
        p = p.next
    return lst


def test_solution():
    s = Solution()

    l1 = make_list([1,3,4])
    l2 = make_list([2,5,6])
    l3 = to_list(s.mergeTwoLists(l1, l2))
    assert l3 == [1,2,3,4,5,6]

    l1 = make_list([1])
    l2 = make_list([2])
    l3 = to_list(s.mergeTwoLists(l1, l2))
    assert l3 == [1,2]

    l1 = make_list([5])
    l2 = make_list([1,2,4])
    l3 = to_list(s.mergeTwoLists(l1, l2))
    assert l3 == [1,2,4,5]
