list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
start=0
end=len(list1)-1

n=int(input("Enter number you want to search : "))
while(start<=end):
    mid=(start+end)//2
    print(mid)
    if list1[mid]==n:
        print(f"number found at index {mid}")
        break
    elif list1[mid]<n:
        start=mid+1
    else:
        end=mid-1

if start>end:
    print("Number not found ")