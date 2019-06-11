# leetcode 949
# https://leetcode-cn.com/problems/largest-time-for-given-digits/
# 也可以使用排列组合,列下所有可能,然后匹配条件


class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        # x = []
        # for i in range(4):
            # if i == 0:
                # for j in [2,1,0]:
                    # if j in A:
                        # x.append(j)
                        # A.remove(j)
                        # break
                # else:
                    # return ""
            # elif i == 1:
                # if x[0] == 2:
                    # for i in range(3,-1,-1):
                        # if i in A:
                            # x.append(i)
                            # A.remove(i)
                            # break
                    # else:
                        # return ""
                # elif x[0] in (0,1):
                    # for i in range(9,-1,-1):
                        # if i in A:
                            # x.append(i)
                            # A.remove(i)
                            # break
                    # else:
                        # return ""
                # else:
                    # pass

            # elif i == 2:
                # for i in range(5,-1,-1):
                    # if i in A:
                        # x.append(i)
                        # A.remove(i)
                        # break
                # else:
                    # return ""
            # else:
                # if 0 <= A[0] <= 9:
                    # x.append(A[0])
                # else:
                    # return False
        # return '{}{}:{}{}'.format(x[0], x[1], x[2], x[3])

        # 使用递归处理
        def f(A, path, level):
            if level == 0:
                for i in [2,1,0]:
                    if i in A:
                        path.append(i)
                        A.remove(i)
                        ret = f(A, path, level+1)
                        if ret:
                            return True
                        else:
                            A.append(i)
                            path.pop()

            elif level == 1:
                if path[-1] == 2:
                    for i in range(3,-1,-1):
                        if i in A:
                            path.append(i)
                            A.remove(i)
                            ret = f(A, path, level+1)
                            if ret:
                                return True
                            else:
                                A.append(i)
                                path.pop()
                elif path[-1] in (0,1):
                    for i in range(9,-1,-1):
                        if i in A:
                            path.append(i)
                            A.remove(i)
                            ret = f(A, path, level+1)
                            if ret:
                                return True
                            else:
                                A.append(i)
                                path.pop()
                else:
                    return False
            elif level == 2:
                for i in range(5,-1,-1):
                    if i in A:
                        path.append(i)
                        A.remove(i)
                        ret = f(A, path, level+1)
                        if ret:
                            return True
                        else:
                            A.append(i)
                            path.pop()
            else:
                if 0 <= A[0] <= 9:
                    path.append(A[0])
                    return True
                else:
                    return False

        path = []
        level = 0
        if f(A, path, level):
            return '{}{}:{}{}'.format(path[0],path[1],path[2], path[3])
        else:
            return ''
