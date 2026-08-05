#  Q.1

s = input("Enter the string: ")     
f = s[::-1] 
if(s == f):
    print("It is palindrome")
else:
    print("it is not palindrome")

# Q.2
num = [1,2,3,4,5]
total = 0
for val in num:
    total = (total+val)
avg = total/len(num)
print(avg)

# Q.3
list1 = list(map(int,input("enter the element of list1  ").split()))
list2 = list(map(int,input("enter the elements of list2 ").split()))
p = list1+list2
print(p)
p.sort()
print(p)


