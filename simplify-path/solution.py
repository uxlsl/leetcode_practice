class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        dirname = ''
        stack = []
        for c in path:
            if c == '/':
                if dirname == '..':
                    if len(stack) >= 2:
                        stack.pop()
                        stack.pop()
                    else:
                        stack = ['/']
                elif dirname != '.' and dirname != '':
                    stack.append(dirname)
                dirname = ''
                if len(stack) == 0 or (len(stack) > 0 and stack[-1] != '/'):
                    stack.append('/')
            else:
                dirname += c
        if dirname == '..':
            if len(stack) >= 2:
                stack.pop()
                stack.pop()
            else:
                stack = ['/']
        elif dirname != '.' and dirname != '':
            stack.append(dirname)
        if len(stack) > 1 and stack[-1] == '/':
            stack.pop()
        return ''.join(stack)
