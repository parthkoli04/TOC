#Description: Tokenization of a string

a=input("Enter the string: ")  #print('Hello World')

list="""()[]{}' +:,."""

x=[]

s=''  
for i in a:
    if i not in list:
        s=s+i

    if i in list:
        if s!='':
            x.append(s)
        s=''
        if i!=" ":
            x.append(i)

print(x)