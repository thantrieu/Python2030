def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


k = int(input("Enter an interger number >= 0: "))
print(f"F{k} = {fibo(k)}")
