def fib(num):
    a=0
    b=1
    for i in range(num+1):
        yield a
        c=a+b
        a=b
        b=c
        
for x in fib(19):
    print(x)
    
def fib2(num):
    a=0
    b=1
    lis=[]
    for i in range(num+1):
        lis.append(a)
        c=a+b
        a=b
        b=c
    return lis

print(fib2(19))
