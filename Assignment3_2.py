def Maxofarray(arr):
    s=0

    for i in range(0,len(arr),1):
        if arr[i]>s:
            s=arr[i];

    return s


def main():
    no=int(input("Enter number of element"));
    arr=list()

    for i in range(0,no,1):
        n=int(input())
        arr.append(n)

    res=Maxofarray(arr);
    print(res)

if __name__ == '__main__':
    main();


