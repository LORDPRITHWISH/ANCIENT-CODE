def holder(x) :
    def power(n) :
        print(x**n)
    return power
base=holder(10)
base(3)
print(base)
