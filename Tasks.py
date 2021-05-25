def func():
    str = input()
    a,x,b,c = map(int, str.split(' '))
    print(a*x*x +b*x + c)

def odd_even():
    str = input()
    a,b,c = map(int, str.split(' '))
    if a%2 == b%2 and b%2==c%2:
        print('WIN')
    else:
        print('FAIL')

def neib_matrix():
    n = int(input())
    m = int(input())
    matrix = []
    result = []
    for i in range (0,n):
        matrix.append([int(j) for j in input().split()])
    a0 = int(input())
    b0 = int(input())
    if a0 == 0:
        if b0 == 0:
            if n!=1:
                result.append(matrix[1][0])
            if m!=1:
                result.append(matrix[0][1])
        elif b0!=0 and b0!=m-1:
            result.append(matrix[a0][b0-1])
            result.append(matrix[a0+1][b0])
            result.append(matrix[a0][b0+1])
        elif b0==m-1:
            result.append(matrix[0][m-2])
            result.append(matrix[1][m-1])
    elif b0 == 0:    
        if a0 == n-1:
            result.append(matrix[n-1][1])
            result.append(matrix[n-2][0])
        elif a0!=0 and a0!=n-1:
            result.append(matrix[a0-1][b0])
            result.append(matrix[a0][b0+1])
            result.append(matrix[a0+1][b0])
    elif a0 == n-1:
        if b0 == m-1:
            result.append(matrix[n-1][m-2])
            result.append(matrix[n-2][m-1])
        elif b0 != 0 and b0 != m-1:
            result.append(matrix[a0-1][b0])
            result.append(matrix[a0][b0+1])
            result.append(matrix[a0][b0-1])
    elif b0 == m-1 and a0!=0 and a0!=n-1:
        result.append(matrix[a0+1][m-1])
        result.append(matrix[a0-1][m-1])
        result.append(matrix[a0][m-2])

    else:
        result.append(matrix[a0-1][b0])
        result.append(matrix[a0][b0-1])
        result.append(matrix[a0+1][b0])
        result.append(matrix[a0][b0+1])
    result.sort()
    print(' '.join([str(elem) for elem in result]))

def weather():
    n = int(input())
    arr = list(map(int,input().split()))
    count = 0
    if n == 1 or (n==2 and arr[0]!=arr[1]):
        print(1)
    else:
        for j in range(0, n-2):
            a = (arr[j])
            b = (arr[j+1])
            c = (arr[j+2])
            if (b>a and b>c) or (a>b and j==0) or (c>b and j+3==n):
                count = count+1
        print(count)


# neib_matrix()
# def merge_sort():
#     pass
#     # arr = [1, 2, 4, 5, 59, 33]
#     # for k in range(1, n):
#     #     if A(i)< B(j)

def long_word():
    n = int(input())
    arr = input().split()
    long_word = ''
    for i in arr:
        if len(long_word)<len(i):
            long_word = i
    print(long_word)
    print(len(long_word))

def to_10():
    n=int(input())
    str_ =''
    while n>0:
        str_ += str(n%2)
        n = n//2
    print(str_[::-1])



