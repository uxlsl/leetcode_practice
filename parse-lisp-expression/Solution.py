class Solution:
    def evaluate(self, expression: str) -> int:

        def getTag(lst:list):
            if not lst:
                return ""

            if lst[0] == '(':
                return lst.pop(0)
            
            i = 1
            tag = ''

            while lst:
                c = lst.pop(0)
                if c == ' ':
                    break
                if c == ')' and tag != "":
                    lst.insert(0,c)
                    break
                tag += c

            return tag

            
        scopes = [{}]
        expression = list(expression)


        def expr(expression:list):
            tag = getTag(expression)
            if tag == '(':
                value = expr(expression)
                tag2 = getTag(expression)
                print('tag2', tag2)
                return value
            elif tag == ')':
                return ')'
            if tag == 'let':
                new_scope = {}

                while True:
                    name = getTag(expression)
                    if name == '(':
                        scopes.append(new_scope)
                        value= expr(expression)
                        scopes.pop()
                        return value
                    else:
                        scopes.append(new_scope)
                        value = expr(expression)
                        scopes.pop()
                        if value == ')':
                            return new_scope[name]
                        new_scope[name] = int(value)

            elif tag == 'add':
                x = expr(expression)
                y = expr(expression)
                return  x + y

            elif tag == 'mult':
                x = expr(expression)
                y = expr(expression)
                return  x * y
            else:
                if tag.isnumeric():
                    return int(tag)
                else:
                    for scope in reversed(scopes):
                        if tag in scope:
                            return scope[tag]
        
        ret = expr(expression)
        return ret
