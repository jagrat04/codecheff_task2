# my series starts with 0 not 1


# task 2.1
def fib(l):
    if l==0:
        return(0)

    else:
        i= 0
        j=1
        n=0
        while n+1<=l:
            k=i+j
            i=j
            j=k
            n=n+1
            
        return(i)


# task2.2
def golden_ratio(n):
    if n<2:
        return("invalid input ")
    else:
        return (float(fib(n)) / float(fib(n-1)))



# task 2.3
n=int(input("N th no of fib/golden ratio:-"))
l=0
while l!=n+1:
    print (fib(l))
    l=l+1
print("golden no. calculated form above series is "+ str(golden_ratio(l)))
