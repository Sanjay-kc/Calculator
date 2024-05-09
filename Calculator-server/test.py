import re

step =[]
def calc(expr):
    op = ['/','*','+','-']
    res = 0
    # print(expr)
    while '(' in expr:
        start = expr.index('(')
        end = expr.index(')')
        res,s = calc(expr[start+1:end])
        del expr[start:end+1]
        expr.insert(start,res)

    # print(expr)
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

def main():
    expr = "4 + (5-7)/2 + 1"
    op = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3, ')': 3}
    r=[]
    list_expr = re.split(r'(\+|-|\*|/|\(|\))', expr)
    list_expr = [i for i in list_expr if i.strip()] 
    res,steps= calc(list_expr)
    for i in range(len(steps)):
        r.append(eval(steps[i]))
    #         steps[i] = steps[i] + " = " + str(r)
    print(res,steps,r)
    print(list_expr[0])

if __name__ == '__main__':
    main()