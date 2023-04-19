# Description: Practical 2 - Python Programming


st=input("Enter String: ")
# st="ab/A"
dict={
'A' : 'b',
'B' : 'a'
}
arr=[]
for i in st:
    if i!='/' and i not in dict:
        arr.append(i)
    if i in dict and i!='/':
        x=dict.get(i)
        arr.append(x)
print(arr)
print("".join(arr))