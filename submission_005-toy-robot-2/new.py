def sprint(n):
    if n == 1:
        print(n-n+1)
        return n
    else:
        print(n)
        return n + sprint(n-1)

if __name__ == '__main__':
    print(sprint(5))

