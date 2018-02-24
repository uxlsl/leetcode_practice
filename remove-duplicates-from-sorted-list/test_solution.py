from solution import Solution, ListNode


def make_list(lst):
    head = None
    n = None

    for i in lst:
        if head is None:
            n = head = ListNode(i)
        else:
            n.next = ListNode(i)
            n = n.next

    return head

def cmp_list(l1, l2):

    n1 = l1
    n2 = l2

    while n1 != None:
        if n1.val != n2.val:
            return False
        n1 = n1.next
        n2 = n2.next

    return True


def print_list(l):
    n = l
    while n != None:
        print(n.val)
        n = n.next


def test_solution():
    s = Solution()
    l1 = make_list([1, 1, 2])
    l2 = make_list([1, 2])
    assert cmp_list(s.deleteDuplicates(l1), l2)

    l1 = make_list([1, 1, 2, 3, 3])
    l2 = make_list([1, 2, 3])
    assert cmp_list(s.deleteDuplicates(l1), l2)

    l1 = make_list([1, 1])
    l2 = make_list([1])
    assert cmp_list(s.deleteDuplicates(l1), l2)


    l1 = make_list([1, 2, 3])
    l2 = make_list([1, 2, 3])
    assert cmp_list(s.deleteDuplicates(l1), l2)
