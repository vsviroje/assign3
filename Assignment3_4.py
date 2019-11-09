def Frequency(arr,a):
    s=0
    for i in range(0,len(arr),1):
        if arr[i]==a:
            s+=1;
    return s


def main():
    no=int(input("Enter number of element"));
    arr=list()

    for i in range(0,no,1):
        n=int(input())
        arr.append(n)
    a=int(input("Enter number to search"));
    res=Frequency(arr,a);
    print(res)

if __name__ == '__main__':
    main();


