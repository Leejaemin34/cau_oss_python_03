def arithmetic_ops(op):
    num1 = int(input("input 1st number: "))
    num2 = int(input("input 2nd number: "))
    return num1, num2, op(num1, num2)

def add(x, y): return x+y
def sub(x, y): return x-y

while True:
    op = input()
    if op == "end" :
        break
    elif op == "+" :
        ret = arithmetic_ops(add)
 