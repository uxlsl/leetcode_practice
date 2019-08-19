class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) <=1:
            ret = 0
            return
        ret = 2
        m = {}
        for i in range(len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                if diff not in m:
                    m[diff] = []
                # bug ，如果连接等差一样，但不同
                for k in m[diff]:
                    if k[-1] == j:
                        k.append(i)
                        if len(k) > ret:
                            print(k)
                            ret = len(k)
                        break
                else:
                    m[diff].append([j, i])
        return ret


class Solution:
    def longestArithSeqLength(self, A):
        # 以每个元素作为等差数列终点，计算出该数列长度，选择出最大值返回即可。
        ret,arr=1,[{} for i in range(len(A))]
        for i in range(1,len(A)):
            for j in range(i):
                d=A[i]-A[j]
                n=arr[j].get(d,1)+1
                arr[i][d]=n
            ret=max(ret,max(arr[i].values()))
        print(arr)
        return ret

