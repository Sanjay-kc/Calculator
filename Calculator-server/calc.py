
def calc(expr):
    step =[]
    op = ['/','*','+','-']
    res = 0
    # print(expr)
    while '(' in expr:
        start = expr.index('(')
        end = expr.index(')')
        res,s = calc(expr[start+1:end])
        del expr[start:end+1]
        step = step + s
        expr.insert(start,res)
    print("calc %s" % step)
    while len(expr)>1:
        for i in op:
            while i in expr:
                j = expr.index(i)
                step.append("".join(str(x) for x in expr[j-1:j+2]))
                res = eval(step[-1])
                del expr[j-1:j+2]
                expr.insert(j-1,res)
                # print(expr)

    return res, step
